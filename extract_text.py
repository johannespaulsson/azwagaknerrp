import os
import re
import docx
from pathlib import Path

def extract_docx(path):
    try:
        doc = docx.Document(path)
        return "\n".join([p.text for p in doc.paragraphs])
    except Exception as e:
        return f"Error reading {path}: {e}"

def extract_doc(path):
    # Very crude extraction for .doc files
    try:
        with open(path, 'rb') as f:
            content = f.read()
        # Look for strings of at least 4 printable-ish characters
        # .doc files often have text in UTF-16LE or CP1252
        # Let's try to decode as cp1252 and find sequences
        text = content.decode('cp1252', errors='ignore')
        # Clean up: remove most control characters and look for coherent blocks
        # Word docs have a lot of junk. We'll look for blocks that look like sentences.
        blocks = re.findall(r'[\w\s\.,!\?\-]{20,}', text)
        return "\n".join(blocks)
    except Exception as e:
        return f"Error reading {path}: {e}"

def main():
    files = sorted(Path('C:/lol').glob('*.*'))
    os.makedirs('C:/lol/extracted', exist_ok=True)
    
    for f in files:
        if f.suffix.lower() == '.docx':
            text = extract_docx(f)
        elif f.suffix.lower() == '.doc':
            text = extract_doc(f)
        else:
            continue
            
        output_path = Path('C:/lol/extracted') / (f.stem + '.txt')
        with open(output_path, 'w', encoding='utf-8') as out:
            out.write(text)
        print(f"Extracted {f.name}")

if __name__ == "__main__":
    main()
