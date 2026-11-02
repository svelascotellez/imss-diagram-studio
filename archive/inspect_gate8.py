with open('setup-sdd-project-v63.ps1', encoding='utf-8') as f:
    text = f.read()

pos = text.find('Gate 8')
print(repr(text[pos-40:pos+150]))
