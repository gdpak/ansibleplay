import json
from xml.etree.ElementTree import Element, SubElement, tostring, tostringlist
from collections import OrderedDict

#from ElementTree_pretty import prettify

def build_xml (json_obj, root):
    json_obj_type = type(json_obj)
    if (json_obj_type is OrderedDict) or (json_obj_type is dict):
        for tag_name in json_obj:
            sub_obj = json_obj[tag_name]
            container_ele = SubElement(root, tag_name)
            if (type(sub_obj) is int) or (type(sub_obj) is unicode):

                container_ele.text = str(sub_obj)
            else:
                print ("obj={} type={}".format(sub_obj, type(sub_obj)))
                build_xml(sub_obj, container_ele)

    if json_obj_type is list:
        for sub_elem in json_obj:
            build_xml(sub_elem, root)

def read_xpath_dict(xpath_src):
    return True

def main():
    src = 'bgp_edit_config.json'
    with open(src, 'r') as f:
        json_config = f.read()
        j_obj = json.loads(json_config, object_pairs_hook=OrderedDict)
        root = Element("config")
        rs = build_xml(j_obj, root)
        print (tostringlist(root))

if  __name__ == "__main__":
    main()
