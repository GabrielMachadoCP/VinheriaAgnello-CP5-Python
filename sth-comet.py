import json
import requests
import matplotlib.pyplot as plt

# Define the URL and headers as in your original code
url = "http://46.17.108.113:8666/STH/v1/contextEntities/type/Lamp/id/urn:ngsi-ld:Lamp:054/attributes/luminosity?aggrMethod=occur&aggrPeriod=minute&dateFrom=2023-09-21T15:00:00.000&dateTo=2023-09-21T15:15:00.000&lastN=15"
headers = {
    'fiware-service': 'smart',
    'fiware-servicepath': '/'
}

# Send the GET request and get the JSON response
response = requests.get(url, headers=headers)

# Parse the JSON response
data = json.loads(response.text)

# Extract luminosity values
luminosity_values = [entry['attrValue'] for entry in data['contextResponses'][0]['contextElement']['attributes'][0]['values']]

# Create a list of timestamps for the x-axis (assuming 'recvTime' field represents time)
timestamps = [entry['recvTime'] for entry in data['contextResponses'][0]['contextElement']['attributes'][0]['values']]

# Convert timestamps to datetime objects (if needed)
# Create a plot
plt.figure(figsize=(10, 6))
plt.plot(timestamps, luminosity_values, marker='o')
plt.xlabel('Timestamp')
plt.ylabel('Luminosity Value')
plt.title('Luminosity vs. Timestamp')
plt.xticks(rotation=45)# You may need to import datetime for this conversion


plt.grid(True)

# Show or save the plot
plt.tight_layout()
plt.show()
# If you want to save the plot as an image file, use plt.savefig('luminosity_plot.png')
