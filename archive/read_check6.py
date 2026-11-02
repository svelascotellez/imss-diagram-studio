with open('setup-sdd-project-v6.py', 'r', encoding='utf-8') as f:
    text = f.read()

pos = 98720
pos6 = text.find('6. Guia de Usuario', pos)
print(text[pos6:pos6+2500])
