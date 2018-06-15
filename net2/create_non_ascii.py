import codecs

with codecs.open('nonascii.bin', 'w', encoding='utf-8') as out:  
    out.write(u'testing ansible basic net_put \ufffd \r\n\n\r')
