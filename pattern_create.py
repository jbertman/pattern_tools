#!/usr/bin/env python

##Original Description##################################
# Author: phillips321
# Site: www.phillips321.co.uk
# Version 0.1
# Credits: metasploit project
# About: Replicates msf pattern_create.rb
########################################################
# Author: jbertman (nok0) - Modified for use in exploit scripts, patterns are returned as strings

import sys

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
