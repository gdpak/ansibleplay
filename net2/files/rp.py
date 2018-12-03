import re

CONFIG_BLOCKS_FORCED_IN_DIFF = [
    {
        'start' : re.compile(r'route-policy'),
        'end' : re.compile(r'end-policy')
    }
]

rp_sample =\
"route-policy static-to-bgp\n \
  if destination in cust-no-export then \
    apply cust2bgp \
    set community cust-no-export additive \
  elseif destination in cust-announce then \
    apply cust2bgp \
    set community cust-announce additive \
  elseif destination in cust-announce-backup then \
    apply cust2bgp \
    set local-preference 98 \
    set weight 0 \
    set community cust-announce additive \
  elseif destination in cust-no-export-backup then \
    apply cust2bgp \
    set local-preference 98 \
    set weight 0 \
    set community cust-no-export additive \
  else \
    drop \
  endif \
end-policy \
"

def sanitize_config_blocks_from_diffs(config):
    index_start = []
    index_end   = []
    lines = config.split("\n")
    for regex in CONFIG_BLOCKS_FORCED_IN_DIFF:
        startblock = False
        for index, line in enumerate(lines):
            startre = regex['start'].search(line)
            if startre and startre.group(0):
                index_start.append(index + 1)
                print (line)
            else:
                print (line)
                endre = regex['end'].search(line)
                if endre and endre.group(0):
                    print (index -1)
                    index_end.append(index - 1)
        print (index_start)
        print (index_end)
        for start in index_start:
           for end in index_end:
               lines[start:end] = lines[start:end] + "ansible"

    res = ("\n").join(lines)
    return res


p = sanitize_config_blocks_from_diffs(rp_sample)
print (p)
