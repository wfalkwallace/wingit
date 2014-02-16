import urllib
from xml.etree import ElementTree as ET
import xml.dom.minidom
#beer pricing addition
country_name = "New zealand"
new_name = country_name.lower().replace(' ', '_')
print 'new_name: ', new_name
requestURL = 'http://www.pintprice.com/xml.php?country=' + new_name
root = ET.parse(urllib.urlopen(requestURL))#.getroot()
#links = list(root.iter("./location/country"))
# print links
for i in root.findall("./location/"): 
	print i.tag



xml = xml.dom.minidom.parse('/vagrant/xml.php?country=new_zealand')
#items = root.findall('items/item')
print xml.toprettyxml()
# print 'hello'
# items = root.findall('location/country/city')
# print items
# for item in items: 
#      print item.find('name').text
#      print item.find('price').text