# Código para obter as leituras de luminosidade por minutos em um intervalo de tempo
import requests
import matplotlib.pyplot as plt
from datetime import datetime

# Fazer a solicitação à API
url = "http://46.17.108.113:8666/STH/v1/contextEntities/type/Lamp/id/urn:ngsi-ld:Lamp:001/attributes/luminosity?aggrMethod=max&aggrPeriod=minute&dateFrom=2023-09-18T22:30:21.237&dateTo=2023-09-18T22:45:21.237"

headers = {
    'fiware-service': 'smart',
    'fiware-servicepath': '/'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    values = data['contextResponses'][0]['contextElement']['attributes'][0]['values'][0]['points']
    origin_value = data["contextResponses"][0]["contextElement"]["attributes"][0]["values"][0]["_id"]["origin"]
    print(f"Origin: {origin_value}")

    # Extrair os valores de luminosidade e tempos
    luminosidade = [point['max'] for point in values]
    tempos = [point['offset'] for point in values]

    # Plotar o gráfico
    plt.figure(figsize=(12, 6))
    
    # Converter os tempos para o formato desejado (eixo x do gráfico)
    tempos_formatados = [f"2023-09-18T22:{offset:02d}:00.000Z" for offset in tempos]

    plt.plot(tempos_formatados, luminosidade, marker='*', linestyle='-', color='g')
    plt.title('Gráfico de Luminosidade em Função do Tempo')
    plt.xlabel('Tempo')
    plt.ylabel('Luminosidade (Max)')
    plt.grid(True)
    plt.tight_layout()
    plt.xticks(rotation=45)  # Rotacionar rótulos do eixo x para melhor visualização
    plt.show()
else:
    print(f"Erro ao obter dados: {response.status_code}")
