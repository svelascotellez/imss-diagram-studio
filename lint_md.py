import re
import sys

def lint_markdown(content, filename="<string>"):
    errors = []
    lines = content.splitlines()
    
    # MD047: File should end with single newline
    if not content.endswith("\n") or content.endswith("\n\n") or content.endswith("\r\n\r\n"):
        if not content.endswith("\n"):
            errors.append(f"MD047/single-trailing-newline: File does not end with newline in {filename}")
        else:
            errors.append(f"MD047/single-trailing-newline: File ends with multiple newlines in {filename}")
            
    in_code = False
    in_table = False
    in_list = False
    
    for i, line in enumerate(lines):
        line_num = i + 1
        
        # MD009: Trailing spaces
        if line.endswith(" ") or line.endswith("\t"):
            errors.append(f"MD009/no-trailing-spaces at line {line_num} in {filename}")
            
        # Code fence detection
        if line.strip().startswith("```"):
            fence = line.strip()
            if not in_code:
                in_code = True
                # MD040: Language specified
                lang = fence[3:].strip()
                if not lang:
                    errors.append(f"MD040/fenced-code-language: Missing language at line {line_num} in {filename}")
                # MD031: Blank line before fence (unless line 1)
                if i > 0 and lines[i-1].strip() != "":
                    errors.append(f"MD031/blanks-around-fences: Missing blank line before fence at line {line_num} in {filename}")
            else:
                in_code = False
                # MD031: Blank line after fence (unless last line)
                if i < len(lines) - 1 and lines[i+1].strip() != "":
                    errors.append(f"MD031/blanks-around-fences: Missing blank line after fence at line {line_num} in {filename}")
            continue
            
        if in_code:
            continue
            
        # MD022: Headings blank lines
        if re.match(r"^#{1,6}\s+", line):
            # Check above
            if i > 0 and lines[i-1].strip() != "":
                errors.append(f"MD022/blanks-around-headings: Missing blank line ABOVE heading at line {line_num} in {filename}")
            # Check below
            if i < len(lines) - 1 and lines[i+1].strip() != "":
                errors.append(f"MD022/blanks-around-headings: Missing blank line BELOW heading at line {line_num} in {filename}")
                
        # Table detection
        is_table_row = line.strip().startswith("|") and line.strip().endswith("|")
        if is_table_row:
            if not in_table:
                in_table = True
                # MD058: Blank line before table
                if i > 0 and lines[i-1].strip() != "":
                    errors.append(f"MD058/blanks-around-tables: Missing blank line before table at line {line_num} in {filename}")
            # Check if table ends next line
            if i == len(lines) - 1 or not (lines[i+1].strip().startswith("|") and lines[i+1].strip().endswith("|")):
                in_table = False
                # MD058: Blank line after table
                if i < len(lines) - 1 and lines[i+1].strip() != "":
                    errors.append(f"MD058/blanks-around-tables: Missing blank line after table at line {line_num} in {filename}")
                    
        # List detection
        is_list_item = bool(re.match(r"^\s*([*+-]|\d+\.)\s+", line))
        if is_list_item:
            # MD004: Unordered list style (Expected: dash)
            if re.match(r"^\s*\*\s+", line):
                errors.append(f"MD004/ul-style: Unordered list style [Expected: dash; Actual: asterisk] at line {line_num} in {filename}")
            elif re.match(r"^\s*\+\s+", line):
                errors.append(f"MD004/ul-style: Unordered list style [Expected: dash; Actual: plus] at line {line_num} in {filename}")

            if not in_list:
                in_list = True
                # MD032: Blank line before list
                if i > 0 and lines[i-1].strip() != "":
                    errors.append(f"MD032/blanks-around-lists: Missing blank line before list at line {line_num} in {filename}")
            # Check if list ends
            if i == len(lines) - 1 or (lines[i+1].strip() != "" and not re.match(r"^\s*([*+-]|\d+\.)\s+", lines[i+1]) and not lines[i+1].startswith("  ") and not lines[i+1].startswith("\t")):
                in_list = False
                if i < len(lines) - 1 and lines[i+1].strip() != "":
                    errors.append(f"MD032/blanks-around-lists: Missing blank line after list at line {line_num} in {filename}")
        elif line.strip() == "":
            in_list = False

    return errors

if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r", encoding="utf-8") as f:
            c = f.read()
        errs = lint_markdown(c, sys.argv[1])
        if errs:
            print(f"FAILED with {len(errs)} errors in {sys.argv[1]}:")
            for e in errs:
                print("  ", e)
        else:
            print(f"PASSED (0 errors): {sys.argv[1]}")
