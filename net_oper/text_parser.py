import textfsm
import getopt, sys
from ansible.module_utils._text import to_text, to_bytes

def parse(parser, content):
    parser_io = open(parser)
    re_table = textfsm.TextFSM(parser_io)
    with open(content) as f:
        cont = f.read()
    text_content = cont
    c = text_content.split('\\n')
    new_str = '\n'.join(c)
    fsm_results = re_table.ParseText(new_str)

    print (fsm_results)

def main():
    parser = sys.argv[1]
    content = sys.argv[2]
    print (parser, content)
    parse(parser, content)


if __name__ == "__main__":
    main()
