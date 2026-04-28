# Azwaga Knerrp Publishing House

Välkommen till det officiella arkivet för **Azwaga Knerrp** – ett surrealistiskt litterärt universum som spänner över tid, rum och charkuterivaror. Projektet är en samling av kapitel, karaktärsstudier och historiska dokument från Kebabylonien till Undulatköping.

## 📖 Om projektet

Projektet fungerar som en statisk webbplats som dokumenterar berättelsen om Hans-Poker Magdalenasson, Luguber, Stig-Cindy Bakplåtspapper och de andra varelserna i Azwaga Knerrp-universumet.

### Innehåll:
- **Kapitel:** Berättelsen i kronologisk (och ibland surrealistisk) ordning.
- **Karaktärswiki:** Detaljerad information om alla varelser och deras kopplingar.
- **Platser & Artefakter:** Dokumentation av heliga objekt som De tio getstenarna och Bergens kran.

## 🛠 Teknisk struktur

Webbplatsen byggs med ett Python-baserat genereringssystem som omvandlar råtext och JSON-data till snyggt formaterade HTML-sidor.

- `data.json`: Den centrala databasen för karaktärer, platser och artefakter.
- `generate.py`: Huvudskriptet som genererar alla HTML-sidor för kapitel och karaktärer.
- `extract_text.py`: Verktyg för att extrahera text från källfiler (.doc/.docx).
- `chapters/` & `characters/`: Innehåller de genererade HTML-filerna.
- `search.js` & `search_data.js`: Hanterar sökfunktionen på sidan.

## 🚀 Arbetsflöde

### 1. Lägga till nytt innehåll
1. Skapa eller uppdatera textfiler i rotmappen eller uppdatera `data.json`.
2. Kör genereringsskriptet:
   ```bash
   python generate.py
   ```
3. Detta uppdaterar alla HTML-filer och sökindexet.

### 2. Publicera ändringar (GitHub Pages)
För att skicka upp dina ändringar till webben:
```bash
git add .
git commit -m "Beskrivning av dina ändringar"
git push origin master
```

---
*© 632 f. Kr. - 2026 Azwaga Knerrp Publishing House*
