with open('setup-sdd-project-v6.py', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('Write-SddFile -Path ".specify\\memory\\constitution.md"')
if pos != -1:
    print(text[pos:pos+3000])
