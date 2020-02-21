import json
import sys

def print_pretty_json(json_str, op_file):
  fd = open(op_file, "a")
  json_object = json.loads(json_str)
  json_formatted_str = json.dumps(json_object, indent=2)
  fd.write(json_formatted_str)

json_str = sys.argv[1]
op_file = sys.argv[2]

print_pretty_json(json_str, op_file)
