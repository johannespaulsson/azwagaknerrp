import json
import os

def load_data():
    with open('C:/lol/data.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def generate_header(title, is_subpage=False):
    prefix = '../' if is_subpage else ''
    return f"""
<!DOCTYPE html>
<html lang="sv">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Kebabylon Wiki</title>
    <link rel="stylesheet" href="{prefix}style.css">
</head>
<body>
    <header>
        <h1>Kebabylonien & Köttmakarens Krönikor</h1>
        <p>Den officiella encyklopedin över getter, kebabsås och kosmiskt kaos</p>
    </header>
    <nav>
        <a href="{prefix}index.html">Hem</a>
        <a href="{prefix}chapters.html">Kapitel</a>
        <a href="{prefix}characters.html">Karaktärer</a>
        <a href="{prefix}locations.html">Platser</a>
        <a href="{prefix}artifacts.html">Artefakter</a>
    </nav>
    <main>
"""

def generate_footer():
    return """
    </main>
    <footer>
        &copy; 632 f. Kr. - 2026 Azwaga Knerrp Publishing House
    </footer>
</body>
</html>
"""

def main():
    data = load_data()
    os.makedirs('C:/lol/characters', exist_ok=True)
    os.makedirs('C:/lol/chapters', exist_ok=True)
    
    # Generate Chapter pages
    extracted_dir = 'C:/lol/extracted'
    files = sorted([f for f in os.listdir(extracted_dir) if f.endswith('.txt')])
    
    chapter_list = []
    for filename in files:
        chapter_id = filename.replace('.txt', '').replace(' ', '_').replace('.', '')
        chapter_title = filename.replace('.txt', '')
        file_path = os.path.join(extracted_dir, filename)
        
        with open(file_path, 'r', encoding='utf-8') as f:
            full_text = f.read()
            
        # Clean up the text for HTML (replace newlines with <br> or wrap in <p>)
        html_text = full_text.replace('\n', '<br>')
        
        content = generate_header(chapter_title, is_subpage=True)
        content += f"<h2>{chapter_title}</h2>"
        content += f"<div class='chapter-text'>{full_text}</div>"
        content += generate_footer()
        
        with open(f"C:/lol/chapters/{chapter_id}.html", 'w', encoding='utf-8') as f:
            f.write(content)
        
        chapter_list.append({'id': chapter_id, 'title': chapter_title})

    # Generate Chapters Index
    content = generate_header("Kapitel")
    content += "<h2>Krönikorna</h2>"
    content += "<p>Här kan du läsa alla kapitel i sin helhet, från kebabens begynnelse till marmeladens återkomst.</p>"
    for chap in chapter_list:
        content += f"<div class='character-card'><h3><a href='chapters/{chap['id']}.html'>{chap['title']}</a></h3></div>"
    content += generate_footer()
    with open("C:/lol/chapters.html", 'w', encoding='utf-8') as f:
        f.write(content)
    
    # Generate Character pages (rest of code follows)
    for char in data['characters']:
        content = generate_header(char['name'], is_subpage=True)
        content += f"<h2>{char['name']}</h2>"
        if 'aliases' in char and char['aliases']:
            content += f"<p><em>Även känd som: {', '.join(char['aliases'])}</em></p>"
        
        content += f"<div class='wiki-entry'><p>{char['description']}</p></div>"
        
        if char.get('analysis'):
            content += f"<h3>Djuplodande Analys</h3><div class='wiki-entry'><p>{char['analysis']}</p></div>"
        
        if char.get('traits'):
            content += "<h3>Kännetecken</h3><ul>"
            for trait in char['traits']:
                content += f"<li>{trait}</li>"
            content += "</ul>"
            
        if char.get('family'):
            content += "<h3>Familj</h3><ul>"
            for member in char['family']:
                content += f"<li>{member}</li>"
            content += "</ul>"
            
        if char.get('possessions'):
            content += "<h3>Utrustning & Ägodelar</h3><ul>"
            for item in char['possessions']:
                content += f"<li>{item}</li>"
            content += "</ul>"
            
        if char.get('quotes'):
            content += "<h3>Kända Citat</h3><ul>"
            for quote in char['quotes']:
                content += f"<li><em>\"{quote}\"</em></li>"
            content += "</ul>"
            
        if char.get('appearances'):
            content += "<h3>Förekommer i kapitel</h3><ul>"
            for app in char['appearances']:
                content += f"<li>{app}</li>"
            content += "</ul>"
            
        if char.get('associations'):
            content += "<h3>Kopplingar</h3><p>"
            content += ", ".join(char['associations'])
            content += "</p>"
            
        content += generate_footer()
        
        with open(f"C:/lol/characters/{char['id']}.html", 'w', encoding='utf-8') as f:
            f.write(content)

    # Generate Characters Index
    content = generate_header("Karaktärer")
    content += "<h2>Persongalleri</h2>"
    content += "<h3>Huvudkaraktärer</h3>"
    for char in data['characters']:
        if char['type'] == 'major':
            content += f"<div class='character-card'><h3><a href='characters/{char['id']}.html'>{char['name']}</a></h3><p>{char['description']}</p></div>"
            
    content += "<h3>Bifigurer</h3>"
    for char in data['characters']:
        if char['type'] == 'secondary':
            content += f"<div class='character-card'><h3><a href='characters/{char['id']}.html'>{char['name']}</a></h3><p>{char['description']}</p></div>"
    content += generate_footer()
    with open("C:/lol/characters.html", 'w', encoding='utf-8') as f:
        f.write(content)

    # Generate Artifacts Page
    content = generate_header("Artefakter")
    content += "<h2>Heliga Föremål & Brödrostar</h2>"
    for art in data['artifacts']:
        content += f"<div class='wiki-entry'><h3>{art['name']}</h3><p>{art['description']}</p></div>"
    content += generate_footer()
    with open("C:/lol/artifacts.html", 'w', encoding='utf-8') as f:
        f.write(content)

    # Generate Locations Page
    content = generate_header("Platser")
    content += "<h2>Geografi & Dimensioner</h2>"
    for loc in data['locations']:
        content += f"<div class='wiki-entry'><h3>{loc['name']}</h3><p>{loc['description']}</p></div>"
    content += generate_footer()
    with open("C:/lol/locations.html", 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    main()
