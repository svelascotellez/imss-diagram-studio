with open('setup-sdd-project-v6.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
# Find ValidateSet in sdd.ps1
m = re.findall(r'(\[ValidateSet\([^)]+\)\])', text)
print("ValidateSets found:", m)

# Find around Check 6
pos = text.find('6. Guia de Usuario:')
if pos != -1:
    print("Found '6. Guia de Usuario:':")
    print(repr(text[pos:pos+300]))
