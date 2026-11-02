import re

with open('setup-sdd-project-v6.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Match PowerShell here-strings: @" ... "@ or @' ... '@
herestrings = re.findall(r'(Set-Content\s+-[^\n]*?\.(?:md|markdown)[\'"]?\s+-Value\s+(@["\'][\s\S]*?^["\']@))', code, re.MULTILINE)
print(f"Found {len(herestrings)} here-string markdown blocks")

md022_issues = []
for full_cmd, hstring in herestrings:
    lines = hstring.split('\n')
    for i, line in enumerate(lines):
        # Check if line is a markdown heading
        m = re.match(r'^\s{0,3}#{1,6}\s+', line)
        if m:
            # Check below
            if i < len(lines) - 1:
                next_l = lines[i+1].rstrip('\r\n')
                if next_l.strip() != '' and not next_l.startswith('"@') and not next_l.startswith("'@"):
                    md022_issues.append(('below', full_cmd.split('\n')[0], i+1, line.strip(), next_l.strip()))
            # Check above
            if i > 0:
                prev_l = lines[i-1].rstrip('\r\n')
                if prev_l.strip() != '' and not prev_l.startswith('@"') and not prev_l.startswith("@'"):
                    md022_issues.append(('above', full_cmd.split('\n')[0], i+1, line.strip(), prev_l.strip()))

print(f"Total MD022 issues in setup-sdd-project-v6.py markdown templates: {len(md022_issues)}")
for typ, cmd, line_num, h, other in md022_issues[:25]:
    print(f"  [{typ}] {cmd} (line in block {line_num}): {h} -> {other}")
