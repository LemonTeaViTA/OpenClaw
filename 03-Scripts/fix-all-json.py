import json
import os

files_to_fix = [
    '.review-tracker.json',
    '.context-snapshot.json'
]

for filename in files_to_fix:
    try:
        data = None
        for encoding in ['utf-8-sig', 'utf-8', 'gbk', 'latin-1']:
            try:
                with open(filename, 'r', encoding=encoding) as f:
                    content = f.read()
                    try:
                        data = json.loads(content)
                        print(f"[OK] Read {filename} with {encoding}")
                        break
                    except:
                        continue
            except:
                continue
        
        if data is None:
            print(f"[ERR] Could not read {filename}")
            continue
        
        with open(filename, 'w', encoding='utf-8-sig') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"[OK] Fixed {filename}")
        
    except Exception as e:
        print(f"[ERR] {filename}: {e}")

print("\nDone!")
