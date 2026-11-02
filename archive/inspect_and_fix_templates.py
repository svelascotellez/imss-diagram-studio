import re

with open('setup-sdd-project-v6.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect where Write-SddFile and Write-SddSkill are in text
# Let's write a parser that specifically processes Lines arrays:
# Pattern: (Write-SddFile\s+-Path\s+"[^"]+\.md"\s+-Lines\s+@\()(.*?)(\)\s*(?:-Force)?)
# or Write-SddSkill

def fix_lines_array(lines_str):
    raw_lines = lines_str.split('\n')
    new_raw_lines = []
    
    # We want to know which raw_line contains a markdown heading
    for i, rl in enumerate(raw_lines):
        stripped = rl.strip()
        # Extract string content from '...' or "..."
        m = re.match(r"^(\s*)(['\"])(#{1,6}\s+.*?)(\2)(,?)\s*$", rl)
        if m:
            indent = m.group(1)
            quote = m.group(2)
            heading_text = m.group(3)
            comma = m.group(5)
            
            # Check if previous item in new_raw_lines was an empty string line: "''" or '""'
            if new_raw_lines:
                prev_item = new_raw_lines[-1].strip()
                # Check if prev_item is empty line
                is_prev_blank = prev_item in ["'',", '""', "''", '"",', "''", '""']
                is_prev_comment = prev_item.startswith('#')
                # Also if it's the very first line of @( then it doesn't need a blank line above
                if not is_prev_blank and not is_prev_comment and prev_item != '@(':
                    new_raw_lines.append(f"{indent}{quote}{quote},")
            
            new_raw_lines.append(rl)
            
            # Check if next line in raw_lines is already a blank string line
            if i + 1 < len(raw_lines):
                next_raw = raw_lines[i + 1].strip()
                is_next_blank = next_raw in ["'',", '""', "''", '"",']
                # If next is closing paren or comment, don't insert blank
                if not is_next_blank and not next_raw.startswith(')') and not next_raw.startswith('#'):
                    new_raw_lines.append(f"{indent}{quote}{quote},")
        else:
            new_raw_lines.append(rl)
            
    return '\n'.join(new_raw_lines)

# Let's test on Write-SddFile and Write-SddSkill
def process_script(script_text):
    # Match Write-SddFile ... -Lines @( ... )
    def repl_file(match):
        header = match.group(1)
        body = match.group(2)
        footer = match.group(3)
        return header + fix_lines_array(body) + footer

    pat_file = r'(Write-SddFile\s+-Path\s+"[^"]+\.md"\s+-Lines\s+@\()([\s\S]*?)(\)\s*(?:-Force)?)'
    res = re.sub(pat_file, repl_file, script_text)
    
    # Match Write-SddSkill ... -Lines @( ... )
    pat_skill = r'(Write-SddSkill\s+-SkillName\s+"[^"]+"\s+-Lines\s+@\()([\s\S]*?)(\)\s*(?=\r?\n\s*(?:Write-SddSkill|Write-Host|#)))'
    res = re.sub(pat_skill, repl_file, res)
    
    return res

new_text = process_script(text)
if new_text != text:
    print("Changes were made!")
    with open('setup-sdd-project-v6.py', 'w', encoding='utf-8') as f:
        f.write(new_text)
else:
    print("No changes were made. Let's inspect why.")
