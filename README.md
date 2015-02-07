This is Metasploit's pattern_create.rb rewritten by phillips321 - modified to work as in an import for exploit scripts in Python.

```Python
import pattern_create

print pattern_create.pattern_create(1000)
```
Arguments to the pattern_create function are:
pattern_create(length, set_a, set_b, set_c)

Where length is the length of the pattern, and sets a through c are character sets to use in pattern generation(optional)
The pattern is returned as a string object.
