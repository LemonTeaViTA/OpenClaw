import json
import sys

# Read and fix JSON encoding
try:
    # Try with utf-8-sig first (handles BOM)
    try:
        with open('.random-review-state.json', 'r', encoding='utf-8-sig') as f:
            data = json.load(f)
    except UnicodeDecodeError:
        with open('.random-review-state.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
    
    # Clean up any corrupted strings
    def clean_str(s):
        if isinstance(s, str):
            # Remove or replace corrupted characters
            return ''.join(c if ord(c) < 0xD800 or ord(c) > 0xDFFF else '?' for c in s)
        return s
    
    def clean_dict(d):
        if isinstance(d, dict):
            return {k: clean_dict(v) for k, v in d.items()}
        elif isinstance(d, list):
            return [clean_dict(i) for i in d]
        elif isinstance(d, str):
            return clean_str(d)
        return d
    
    cleaned = clean_dict(data)
    
    # Write back with proper UTF-8
    with open('.random-review-state.json', 'w', encoding='utf-8-sig') as f:
        json.dump(cleaned, f, ensure_ascii=False, indent=2)
    
    print("✓ Fixed .random-review-state.json")
except Exception as e:
    print(f"✗ Error: {e}", file=sys.stderr)
    sys.exit(1)

try:
    try:
        with open('.review-tracker.json', 'r', encoding='utf-8-sig') as f:
            data = json.load(f)
    except UnicodeDecodeError:
        with open('.review-tracker.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
    
    with open('.review-tracker.json', 'w', encoding='utf-8-sig') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print("✓ Fixed .review-tracker.json")
except Exception as e:
    print(f"✗ Error: {e}", file=sys.stderr)

try:
    try:
        with open('.context-snapshot.json', 'r', encoding='utf-8-sig') as f:
            data = json.load(f)
    except UnicodeDecodeError:
        with open('.context-snapshot.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
    
    with open('.context-snapshot.json', 'w', encoding='utf-8-sig') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print("✓ Fixed .context-snapshot.json")
except Exception as e:
    print(f"✗ Error: {e}", file=sys.stderr)

print("\nAll JSON files fixed!")
