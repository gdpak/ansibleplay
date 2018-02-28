import json

def json_to_xml(json_obj, line_padding=""):                                                                                               
    result_list = []                                                                                                                      
                                                                                                                                          
    json_obj_type = type(json_obj)                                                                                                        
                                                                                                                                          
    if json_obj_type is list:                                                                                                             
       for sub_elem in json_obj:                                                                                                          
           result_list.append(json_to_xml(sub_elem, line_padding))                                                                        
       return "\n".join(result_list)                                                                                                      
                                                                                                                                          
    if json_obj_type is dict:                                                                                                             
       for tag_name in json_obj:                                                                                                          
           sub_obj = json_obj[tag_name]                                                                                                   
           result_list.append("%s<%s>" % (line_padding, tag_name))                                                                        
           result_list.append(json_to_xml(sub_obj, "\t"+line_padding))                                                                    
           result_list.append("%s<%s>" % (line_padding, tag_name))                                                                        
                                                                                                                                          
       return "\n".join(result_list)                                                                                                      
                                                                                                                                          
    return "%s%s" % (line_padding, json_obj) 

def main():
    with open('bgp_edit_config.json', 'r') as f:
         json_config = f.read()
         j = json.loads(json_config)
         xml = json_to_xml(j)
         print (xml)


if __name__ == "__main__":
    main()
                   
