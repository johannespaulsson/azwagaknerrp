import json
import os
import re

def load_data():
    with open('C:/lol/data.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def find_appearances(data):
    extracted_dir = 'C:/lol/extracted'
    files = sorted([f for f in os.listdir(extracted_dir) if f.endswith('.txt')])
    
    for char in data['characters']:
        appearances = []
        # Create a list of names to search for (full name + aliases)
        names = [char['name']] + char.get('aliases', [])
        # Extract just the first name for more casual mentions if applicable
        if ' ' in char['name']:
            names.append(char['name'].split(' ')[0])
            
        # Clean up names for regex
        name_patterns = [re.escape(n) for n in names if len(n) > 2]
        pattern = re.compile(r'\b(' + '|'.join(name_patterns) + r')\b', re.IGNORECASE)
        
        for filename in files:
            file_path = os.path.join(extracted_dir, filename)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                if pattern.search(content):
                    # Strip .txt and maybe shorten the chapter name for display
                    chapter_display = filename.replace('.txt', '')
                    appearances.append(chapter_display)
        
        char['appearances'] = appearances
        print(f"Character {char['name']} found in {len(appearances)} chapters.")
    
    return data

def main():
    data = load_data()
    updated_data = find_appearances(data)
    with open('C:/lol/data.json', 'w', encoding='utf-8') as f:
        json.dump(updated_data, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    main()
