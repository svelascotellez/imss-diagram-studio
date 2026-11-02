with open("proposals_complete.txt", "r", encoding="utf-8") as f:
    text = f.read()

import re
matches = re.findall(r'(###\s*\d+\..*?)(?=\n###|\n---|\Z)', text)
for m in matches:
    print(m.strip().splitlines()[0].encode('ascii', 'replace').decode('ascii'))
