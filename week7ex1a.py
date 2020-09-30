from lxml import etree

#f=open("show_security_zones.xml")
with open("show_security_zones.xml") as f:
    xml_data=f.read()
xml_object=etree.fromstring(xml_data)

if __name__=="__main__":
    print (xml_object)
    print (type(xml_object))
