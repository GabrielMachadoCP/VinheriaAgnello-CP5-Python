import requests

import matplotlib.pyplot as plt

from datetime import datetime

 

url="http://46.17.108.113:8666/STH/v1/contextEntities/type/Lamp/id/urn:ngsi-ld:Lamp:001/attributes/luminosity?hLimit=100&hOffset=1&dateFrom=2023-09-22T10:00:00.000&dateTo=2023-09-22T10:15:00.000"

 

payload = {}

headers = {

  'fiware-service': 'smart',

  'fiware-servicepath': '/'

}

 

response = requests.get(url, headers=headers)

 

if response.status_code == 200:

    data = response.json()

    values = [entry['attrValue'] for entry in data['contextResponses'][0]['contextElement']['attributes'][0]['values']]

    timestamps = [datetime.strptime(entry['recvTime'], '%Y-%m-%dT%H:%M:%S.%fZ') for entry in data['contextResponses'][0]['contextElement']['attributes'][0]['values']]

   

    # Agora, vamos criar o gráfico.

    plt.figure(figsize=(10, 6))

    plt.plot(timestamps, values, marker='o', linestyle='-')

    plt.xlabel('Timestamp')

    plt.ylabel('Luminosity')

    plt.title('Luminosity Over Time')

    plt.grid(True)

    plt.xticks(rotation=45)

    plt.tight_layout()

   

    # Exibir o gráfico

    plt.show()

else:

    print(f"Failed to fetch data. Status code: {response.status_code}")
