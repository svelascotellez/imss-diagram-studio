import re

with open('setup-sdd-project-v6.ps1', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's find all Write-SddFile blocks
# Pattern: Write-SddFile -Path "..." -Lines @(...)
# Or Write-SkillFile
pattern = r'(Write-SddFile\s+-Path\s+"([^"]+\.md)"\s+-Lines\s+@\(([\s\S]*?)\)\s*(?:-Force)?)'
matches = re.findall(pattern, text)
print(f"Found {len(matches)} Write-SddFile markdown blocks")

total_violations = 0
for full, path, lines_content in matches:
    # Extract string items inside @(...)
    # Each item is typically 'line',
    raw_lines = lines_content.split('\n')
    lines = []
    for rl in raw_lines:
        rl_s = rl.strip()
        if rl_s.startswith("'") and rl_s.endswith("',"):
            lines.append(rl_s[1:-2])
        elif rl_s.startswith("'") and rl_s.endswith("'"):
            lines.append(rl_s[1:-1])
        elif rl_s.startswith('"') and rl_s.endswith('",'):
            lines.append(rl_s[1:-2])
        elif rl_s.startswith('"') and rl_s.endswith('"'):
            lines.append(rl_s[1:-1])
        elif rl_s == "''" or rl_s == '""' or rl_s == "''," or rl_s == '"",':
            lines.append("")
        elif rl_s == "":
            pass
        else:
            # fallback
            lines.append(rl_s)
    
    file_issues = []
    for i, line in enumerate(lines):
        if re.match(r'^\s{0,3}#{1,6}\s+', line):
            # check below
            if i < len(lines) - 1:
                next_l = lines[i+1].strip()
                if next_l != '' and not re.match(r'^\s*$', next_l):
                    file_issues.append((i+1, 'below', line, next_l))
            # check above
            if i > 0:
                prev_l = lines[i-1].strip()
                if prev_l != '' and not re.match(r'^\s*$', prev_l):
                    file_issues.append((i+1, 'above', line, prev_l))
    
    if file_issues:
        print(f"\n{path}: {len(file_issues)} violations")
        for num, typ, h, other in file_issues[:5]:
            print(f"  [{typ}] line {num}: {h} -> {other}")
        total_violations += len(file_issues)

print(f"\nTotal violations across all template files: {total_violations}")


# Let's check Write-SkillFile
skill_matches = re.findall(r'(Write-SkillFile\s+-SkillName\s+"([^"]+)"\s+-Lines\s+@\(([\s\S]*?)\)\s*)', text)
print(f"\nFound {len(skill_matches)} Write-SkillFile blocks")
for full, name, lines_content in skill_matches:
    raw_lines = lines_content.split('\n')
    lines = []
    for rl in raw_lines:
        rl_s = rl.strip()
        if rl_s.startswith("'") and rl_s.endswith("',"):
            lines.append(rl_s[1:-2])
        elif rl_s.startswith("'") and rl_s.endswith("'"):
            lines.append(rl_s[1:-1])
        elif rl_s.startswith('"') and rl_s.endswith('",'):
            lines.append(rl_s[1:-2])
        elif rl_s.startswith('"') and rl_s.endswith('"'):
            lines.append(rl_s[1:-1])
        elif rl_s in ["''", '""', "'',", '"",']:
            lines.append("")
        else:
            lines.append(rl_s)
            
    file_issues = []
    for i, line in enumerate(lines):
        if re.match(r'^\s{0,3}#{1,6}\s+', line):
            if i < len(lines) - 1:
                next_l = lines[i+1].strip()
                if next_l != '' and not re.match(r'^\s*$', next_l):
                    file_issues.append((i+1, 'below', line, next_l))
            if i > 0:
                prev_l = lines[i-1].strip()
                if prev_l != '' and not re.match(r'^\s*$', prev_l):
                    file_issues.append((i+1, 'above', line, prev_l))
    if file_issues:
        print(f"Skill {name}: {len(file_issues)} violations")
        for num, typ, h, other in file_issues[:3]:
            print(f"  [{typ}] line {num}: {h} -> {other}")


skill_matches2 = re.findall(r'Write-SddSkill\s+-SkillName\s+"([^"]+)"\s+-Lines\s+@\(([\s\S]*?)\)(?=\s*(?:Write-SddSkill|\r?\n\s*#|\r?\n\s*Write-Host))', text)
print(f"\nFound {len(skill_matches2)} Write-SddSkill blocks")
for name, lines_content in skill_matches2:
    raw_lines = lines_content.split('\n')
    lines = []
    for rl in raw_lines:
        rl_s = rl.strip()
        if (rl_s.startswith("'") and rl_s.endswith("',")) or (rl_s.startswith('"') and rl_s.endswith('",')):
            lines.append(rl_s[1:-2])
        elif (rl_s.startswith("'") and rl_s.endswith("'")) or (rl_s.startswith('"') and rl_s.endswith('"')):
            lines.append(rl_s[1:-1])
        elif rl_s in ["''", '""', "'',", '"",']:
            lines.append("")
        else:
            lines.append(rl_s)
    
    file_issues = []
    for i, line in enumerate(lines):
        if re.match(r'^\s{0,3}#{1,6}\s+', line):
            if i < len(lines) - 1:
                next_l = lines[i+1].strip()
                if next_l != '' and not re.match(r'^\s*$', next_l):
                    file_issues.append((i+1, 'below', line, next_l))
            if i > 0:
                prev_l = lines[i-1].strip()
                if prev_l != '' and not re.match(r'^\s*$', prev_l):
                    file_issues.append((i+1, 'above', line, prev_l))
    if file_issues:
        print(f"Skill {name}: {len(file_issues)} violations")
        for num, typ, h, other in file_issues[:2]:
            print(f"  [{typ}] line {num}: {h} -> {other}")
