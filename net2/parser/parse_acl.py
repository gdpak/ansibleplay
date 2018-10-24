import textfsm
import netaddr

def parse_acl_with_textfsm(parser_file, output):
    import textfsm
    tmp = open(parser_file)
    re_table = textfsm.TextFSM(tmp)
    results = re_table.ParseText(output)
    fsm_results = []
    for item in results:
        facts = {}
        facts.update(dict(zip(re_table.header, item)))
        fsm_results.append(facts)
  
    pd = []
    parsed_acl = []
    # Convert dictionary of terms into flows dictionary
    for term in fsm_results:
        pd_it = {}
        original_terms = {}
        for k,v in term.items():
            if k == 'LINE_NUM' and v == '':
                # Empty line with just name
                continue
            if k == 'SRC_HOST' and v != '':
                pd_it["src"] = v
                original_terms['src'] = v
            if k == 'SRC_NETWORK' and v != '':
                if 'SRC_WILDCARD' in term:
                    src_mask = term['SRC_WILDCARD']
                    src_invert_mask = sum([bin(255 - int(x)).count("1") for x in
                         src_mask.split(".")])
                else:
                    src_invert_mask = '32'
                cidr = "%s/%s" %(v, src_invert_mask)
                src_ip = netaddr.IPNetwork(cidr)
                original_terms['src'] = src_ip
        
        pd.append(pd_it)
        parsed_acl.append(original_terms)

    print (pd)
    print (parsed_acl)
              
    return results

parser = './show_ip_access_list.yaml'
out = "\
Extended IP access list 101\n    10 deny tcp 11.2.2.0 0.0.0.255 any eq www (14 matches)\n    20 deny tcp 11.2.2.0 0.0.0.255 any eq 443 (7 matches)\n    30 permit tcp host 11.2.2.34 any eq www\n    40 permit tcp host 11.3.3.0 any eq www (7 matches)"

parse_acl_with_textfsm(parser, out)
