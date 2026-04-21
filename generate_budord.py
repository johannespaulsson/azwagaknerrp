import json
import random

def load_data():
    with open('C:/lol/data.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def main():
    budord = [
        "Det är förbjudet att fritera ankskägg på måndagar.",
        "Müslin är inte ätbar, den är bara prydnad.",
        "Whiskyn skall användas för att skölja hålfotsinläggen.",
        "Lungsjuka måste renas med blysocker och juice.",
        "Zebrahuden bakom kassan är 'fejk' (officiellt).",
        "Inga kaskelotter i fikarummet efter kl 15:00.",
        "All förtäring av blåbärsmuffins sker på egen risk och under tystnadsplikt.",
        "Om du ser en giraff med slips, låtsas som att det regnar.",
        "Prygel utdelas endast till de som stavar 'kebab' med tre b.",
        "Vinkelslipar får ej användas för att skära lussebullar i maj."
    ]
    
    with open('C:/lol/budord.json', 'w', encoding='utf-8') as f:
        json.dump(budord, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    main()
