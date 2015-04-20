These are Metasploit's pattern tools (pattern_create and pattern_offset) modified to work as imports for exploit scripts in Python.

```Python
import pattern_tools

print pattern_tools.pattern_create(1000)
"""Pattern prints out here"""

print pattern_tools.pattern_offset('0x69413269')
"""prints [*] Exact match at offset 247"""
```
Arguments for relevant functions are:
`pattern_create(length, set_a, set_b, set_c)`

Where length is the length of the pattern, and sets a through c are character sets to use in pattern generation(optional)
The pattern is returned as a string object.

`pattern_offset(value, length)`

Where value is the string in hex you want to find, and length is the pattern length to search through (default = 8192)
TODO: Partial matching, reverse endianness
