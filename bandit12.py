#!/bin/python3


s = """Gur cnffjbeq vf 5Gr8L4qetPEsPk8htqjhRK8XSP6x2RHh"""

d = {}  
for c in (65, 97):  
    for i in range(26):  
        d[chr(i+c)] = chr((i+13) % 26 + c) 

print("".join([d.get(c, c) for c in s]))

    
