from week7ex1a import xml_object #re-using the variable from another program
from lxml import etree

xml_string=etree.tostring(xml_object).decode()

if __name__=="__main__":
    print(xml_string)


