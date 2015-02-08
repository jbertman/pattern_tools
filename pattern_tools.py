#!/usr/bin/env python

##pattern_create original description###################
# Author: phillips321
# Site: www.phillips321.co.uk
# Version 0.1
# Credits: metasploit project
# About: Replicates msf pattern_create.rb
########################################################
# Author: jbertman (nok0) - Modified for use in exploit scripts, patterns are returned as strings

##pattern_offset########################################
# Author: jbertman (nok0)
# Version 0.1
# Credits: Metasploit project
# About: Replicates msf pattern_offset.rb
########################################################

import sys, struct

def pattern_create(length, set_a=None, set_b=None, set_c=None):
    if not isinstance(length, int):
        raise Exception('[-] Length must be an integer')
        sys.exit(1) 

    if not set_a: seta="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if not set_b: setb="abcdefghijklmnopqrstuvwxyz"
    if not set_c: setc="0123456789"

    string="" ; a=0 ; b=0 ; c=0
    
    while len(string) < length:
        if not set_a and not set_b and not set_c:
            string += seta[a] + setb[b] + setc[c]
            c+=1
            if c == len(setc):c=0;b+=1
            if b == len(setb):b=0;a+=1
            if a == len(seta):a=0
        elif set_a and not set_b and not set_c:
            raise Exception('[-] Error, cannot work with just one set!')
            sys.exit(1)
        elif set_a and set_b and not set_c:
            string += seta[a] + setb[b]
            b+=1
            if b == len(setb):b=0;a+=1
            if a == len(seta):a=0
        elif set_a and set_b and set_c:
            string += seta[a] + setb[b] + setc[c]
            c+=1
            if c == len(setc):c=0;b+=1
            if b == len(setb):b=0;a+=1
            if a == len(seta):a=0
        else:
            raise Exception('[-] Input error, please check your parameters')
            sys.exit(1)

    return string[:length]


def pattern_offset(value, length=8192):
    if len(value) >= 8 and int(value, 16) > 0:
        value = int(value, 16)
    elif len(value) == 4:
        value = struct.unpack('<L', value)[0]
    else:
        value = int(value, 16)

    buf = pattern_create(length)
    offset = buf.find(struct.pack('<L',value))

    if offset == -1:
        found = False
    else:
        found = True
    """    
    while not found:
        print '[*] No exact matches, looking for likely candidates...'
        for idx in range(3):
            for c in range(255):
                nvb = struct.pack('<L',value)
                nvb = nvb.replace(nvb[idx:1],struct.pack('B',c))
                print repr(nvb)
                nvi = struct.unpack('<L',nvb)[0]
                off = buf.find(struct.pack('<L',nvi))
                if off != -1:
                    mle = value - struct.unpack('<L',buf[off:4])[0]
                    mbe = value - struct.unpack('>L',buf[off:4])[0]
                    print '[+] Possible match at offset %i (adjusted [ little-endian: %s | big-endian: %s ] ) byte offset %i' % (off, str(mle), str(mbe), idx)
                    found = True

        if found == True:
            sys.exit(0)

        for idx in range(2):
            for c in range(65535):
                nvb = struct.pack('<L',value)
                nvb = nvb.replace(nvb[idx:2],struct.pack('H',c))
                nvi = struct.unpack('<L',nvb)[0] 
                off = buf.find(struct.pack('<L',nvi))
                if off != -1:
                    mle = value - struct.unpack('<L',buf[off:4])[0]
                    mbe = value - struct.unpack('>L',buf[off:4])[0]
                    print '[+] Possible match at offset %i (adjusted [ little-endian: %s | big-endian: %s ] ) byte offset %i' % (off, str(mle), str(mbe), idx)
                    found = True
    """
    while offset != -1:
        return "[*] Exact match at offset %i" % (offset)
        offset = buf.find(struct.pack('<L',value), offset + 1)
            

    









        

