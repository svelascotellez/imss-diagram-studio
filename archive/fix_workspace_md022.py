import os
import re

def fix_markdown_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        lines = [line.rstrip('\r\n') for line in f]
    
    new_lines = []
    in_code_block = False
    modified = False
    
    for i, line in enumerate(lines):
        # Check code fence
        if re.match(r'^\s*```', line):
            in_code_block = not in_code_block
            new_lines.append(line)
            continue
        
        if in_code_block:
            new_lines.append(line)
            continue
        
        # Check if line is a markdown heading (# to ######)
        if re.match(r'^\s{0,3}#{1,6}\s+', line):
            # Check if previous line in new_lines is not blank (MD022 Above)
            if new_lines and new_lines[-1].strip() != '':
                new_lines.append('')
                modified = True
            
            new_lines.append(line)
            
            # Check if next line in original lines exists and is not blank (MD022 Below)
            if i + 1 < len(lines):
                next_line = lines[i + 1]
                if next_line.strip() != '':
                    new_lines.append('')
                    modified = True
        else:
            new_lines.append(line)
            
    if modified:
        with open(filepath, 'w', encoding='utf-8', newline='\n') as f:
            f.write('\n'.join(new_lines) + '\n')
        print(f"Fixed: {filepath}")
    return modified

if __name__ == '__main__':
    count = 0
    for root, dirs, files in os.walk('.'):
        for f in files:
            if f.endswith('.md'):
                p = os.path.join(root, f)
                if fix_markdown_file(p):
                    count += 1
    print(f"\nTotal markdown files fixed: {count}")
