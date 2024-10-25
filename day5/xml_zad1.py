from xml.dom import minidom

root = minidom.Document()
xml = root.createElement('root')
root.appendChild(xml)

product_child = root.createElement('product')
product_child.setAttribute('name', "Test")
xml.appendChild(product_child)

xml_str = root.toprettyxml(indent="\t")
print(xml_str)

#
# <?xml version="1.0" ?>
# <root>
# 	<product name="Test"/>
# </root>

# zapisanie xml do pliku
with open('xml_dane.xml', "w") as f:
    f.write(xml_str)
