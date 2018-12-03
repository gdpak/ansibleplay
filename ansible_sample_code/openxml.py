#!/usr/bin/python

from lxml import etree
namespace = 'http://openconfig.net/yang/interfaces'

def read_xml():
    tree= etree.parse('/home/vagrant/.ansible/tmp/yang/openconfig-interfaces.xml')
    root = tree.getroot()
    ele = root.findall('{' + namespace + '}' + 'interfaces')
    if ele:
        for items in ele:
           print (etree.tostring(items))
    else:
        print ('can not find root node')
    print (etree.tostring(root, pretty_print=True))


if __name__ == "__main__":
   read_xml()
