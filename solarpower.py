import json
import urllib
import xmltodict

url = 'http://192.168.1.153/measurements.xml'
xmlfile = urllib.request.urlopen(url).read()
content = xmltodict.parse(str(xmlfile, 'utf-8'))
data = json.dumps(content)
json_data = json.loads(data)

power=json_data['root']['Device']['Measurements']['Measurement'][2]['@Value']
if power == '-nan':
    power = 0
print(power)
