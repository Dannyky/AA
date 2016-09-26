from xml.dom import minidom
xmldoc = minidom.parse('items.xml')
itemlist = xmldoc.getElementsByTagName('item')
print(len(itemlist))
print(itemlist[0].attributes['name'].value)
for s in itemlist:
    print(s.attributes['name'].value)
itemlist1 = xmldoc.getElementsByTagName('stem')
print(len(itemlist1))
print(itemlist1[0].attributes['name'].value)
for s in itemlist1:
    print(s.attributes['name'].value)
