import os
import re

def check_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        lines = [line.rstrip('\r\n') for line in f]
    
    issues = []
    in_code_block = False
    
    for i, line in enumerate(lines):
        if re.match(r'^\s*```', line):
            in_code_block = not in_code_block
            continue
            
        if in_code_block:
            continue
            
        # Match markdown headings outside code blocks
        if re.match(r'^\s{0,3}#{1,6}\s+', line):
            # Check below
            if i < len(lines) - 1:
                next_line = lines[i+1]
                if next_line.strip() != '':
                    issues.append({
                        'line': i + 1,
                        'type': 'below',
                        'heading': line,
                        'next_line': next_line
                    })
            # Check above
            if i > 0:
                prev_line = lines[i-1]
                if prev_line.strip() != '':
                    issues.append({
                        'line': i + 1,
                        'type': 'above',
                        'heading': line,
                        'prev_line': prev_line
                    })
    return issues

if __name__ == '__main__':
    md_files = []
    for root, dirs, files in os.walk('.'):
        for f in files:
            if f.endswith('.md'):
                md_files.append(os.path.join(root, f))
    
    total_issues = 0
    file_issue_counts = {}
    for mf in md_files:
        iss = check_file(mf)
        if iss:
            file_issue_counts[mf] = len(iss)
            total_issues += len(iss)
    
    print(f"Total markdown files scanned: {len(md_files)}")
    print(f"Files with MD022 issues: {len(file_issue_counts)}, Total violations: {total_issues}")
    for f, count in sorted(file_issue_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"  {f}: {count} violations")
