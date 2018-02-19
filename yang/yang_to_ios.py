import json

def main():
    json1_file = open('interface.yang')
    json1_str = json1_file.read()
    json1_data = json.loads(json1_str)

    for _, ints_dict in json1_data.items():
        for _, int_val in ints_dict.items():
            for int_identifier, val_int_config in int_val.items():
                for _,int_configs in val_int_config.items():
                    print (int_configs)
    print (json1_data)

if __name__ == '__main__' :
    main()
