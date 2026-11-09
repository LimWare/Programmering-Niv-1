#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Interaktivt Terminal-Quiz: Git, Branches, Push/Pull & Flowcharts
Kurs: Programmering 1 (Python) - JENSEN Education (Lektion 10, 11 & 13)
"""

import random

QUESTIONS = [
    {
        "kategori": "Git Grunder",
        "fraga": "Vad är Git enligt lektionsmaterialet?",
        "alternativ": [
            "En populär och kraftfull versionshanteringsprogramvara för att spåra ändringar i källkod",
            "En molnplattform som ägs av Microsoft för att lagra hemsidor",
            "En textredigerare som bara fungerar i Windows Command Prompt",
            "Ett programmeringsspråk som ersätter Python"
        ],
        "ratt_index": 0,
        "forklaring": "Git är gratis och öppen källkod som spårar ändringar i källkoden och tillåter samarbete samt offline-arbete."
    },
    {
        "kategori": "Git Grunder",
        "fraga": "Vad är skillnaden mellan Working Directory och Repository?",
        "alternativ": [
            "Working Directory är din projektmapp där du gör ändringar; Repository (.git-mappen) lagrar historik och metadata",
            "Working Directory ligger på GitHub medan Repository ligger på skrivbordet",
            "Working Directory innehåller bara raderade filer",
            "Det är exakt samma sak"
        ],
        "ratt_index": 0,
        "forklaring": "Arbetskatalogen (Working Directory) är mappen du jobbar i, medan .git-mappen (Repository) lagrar alla commits och referenser."
    },
    {
        "kategori": "Git Grunder",
        "fraga": "Varför rekommenderas det att använda samma e-postadress för både Git och GitHub?",
        "alternativ": [
            "För att göra det lättare att identifiera dig och din aktivitet i projektet",
            "Annars fungerar inte kommandot git init",
            "För att få gratis lagringsutrymme",
            "Git kräver det för att starta terminalen"
        ],
        "ratt_index": 0,
        "forklaring": "Samma e-postadress via 'git config --global user.email' kopplar dina commits direkt till din identitet på GitHub."
    },
    {
        "kategori": "Git Grunder",
        "fraga": "Vilka kommandon visar dina aktiva Git-konfigurationer respektive tar bort ditt globala user.name?",
        "alternativ": [
            "Visa: 'git config --list' (tryck q för att avsluta) | Ta bort: 'git config --global --unset user.name'",
            "Visa: 'git show all' | Ta bort: 'git delete user.name'",
            "Visa: 'git status -l' | Ta bort: 'git config --remove name'",
            "Visa: 'git help' | Ta bort: 'git reset user.name'"
        ],
        "ratt_index": 0,
        "forklaring": "'git config --list' (eller -l) listar inställningar och '--unset' raderar en specifik variabel."
    },
    {
        "kategori": "Git Grunder",
        "fraga": "I Övning 1 (proj1 med lista.py): Vilken sekvens initierar repot, stagear alla ändringar, committar och visar historiken?",
        "alternativ": [
            "git init -> git add . -> git commit -m "meddelande" -> git log",
            "git start -> git stage . -> git save -m "meddelande" -> git history",
            "git init -> git commit . -> git push -> git status",
            "git branch -> git add . -> git log -> git checkout"
        ],
        "ratt_index": 0,
        "forklaring": "'git init' skapar repot, 'git add .' lägger till i staging area, 'git commit -m' sparar snapshoten och 'git log' visar commit-IDn."
    },
    {
        "kategori": "Git Grunder",
        "fraga": "Vilket kommando används i Övning 1 för att återgå till en tidigare version av koden med hjälp av dess commit-ID?",
        "alternativ": [
            "git checkout <commit-ID>",
            "git return <commit-ID>",
            "git pull <commit-ID>",
            "git init <commit-ID>"
        ],
        "ratt_index": 0,
        "forklaring": "Med 'git log' hittar du commit-IDt och med 'git checkout <commit-ID>' återgår du till den tidigare commiten."
    },
    {
        "kategori": "Branches",
        "fraga": "Vad är syftet med en Branch (gren) i Git?",
        "alternativ": [
            "Att kopiera projektet till en egen väg för att utveckla nya funktioner eller lösa problem utan att ändra huvudkoden",
            "Att radera gammal historik automatiskt",
            "Att spara lösenord i klartext",
            "Att stänga av versionshanteringen tillfälligt"
        ],
        "ratt_index": 0,
        "forklaring": "En branch skapas från en specifik commit så att du kan jobba fritt och sedan slå ihop ändringarna med huvudvägen (main/master)."
    },
    {
        "kategori": "Branches",
        "fraga": "Vilka kommandon används för att: 1) Lista grenar, 2) Skapa + byta till ny gren (klassiskt & modernt), 3) Radera en gren?",
        "alternativ": [
            "1) git branch | 2) git checkout -b <namn> (eller git switch -c <namn>) | 3) git branch -d <namn>",
            "1) git list | 2) git new -b <namn> | 3) git delete <namn>",
            "1) git status | 2) git commit -b <namn> | 3) git branch --unset <namn>",
            "1) git log | 2) git merge -c <namn> | 3) git remove -d <namn>"
        ],
        "ratt_index": 0,
        "forklaring": "Asterisken (*) i 'git branch' visar aktiv gren. 'git checkout -b' / 'git switch -c' skapar och byter gren, och 'git branch -d' raderar."
    },
    {
        "kategori": "Push & Pull",
        "fraga": "Vad gör 'git push' respektive 'git pull' mellan Local Repo och Remote Repository?",
        "alternativ": [
            "git push laddar upp lokala ändringar till fjärr-repot; git pull hämtar ändringar från fjärr-repot och slår samman dem lokalt",
            "git push hämtar filer från GitHub; git pull laddar upp filer till GitHub",
            "Båda raderar lokala filer",
            "De fungerar bara utan internet"
        ],
        "ratt_index": 0,
        "forklaring": "Push skickar dina commits till fjärr-repot (t.ex. GitHub), medan Pull hämtar och slår ihop andras ändringar till ditt lokala repo."
    },
    {
        "kategori": "Push & Pull",
        "fraga": "Vad gäller kring att pusha och pulla enligt sammanfattningen inför nästa lektion (OBS!/IMPORTANT-sliden)?",
        "alternativ": [
            "Alla kan pusha och pulla beroende på deras behörighet (samt: ett repo per projekt och en ny gren per funktion)",
            "Ingen behöver behörighet för att pusha till privata projekt",
            "Man ska ha alla sina skolprojekt i ett enda gemensamt repo utan branches",
            "Endast läraren kan köra git pull"
        ],
        "ratt_index": 0,
        "forklaring": "Behörigheter på fjärr-repot styr vilka användare som har läsrättigheter (pull) respektive skrivrättigheter (push)."
    },
    {
        "kategori": "Flowchart",
        "fraga": "Vilka standardformer används i ett flödesschema (flowchart)?",
        "alternativ": [
            "Oval = Start/Slut (Terminator), Rektangel = Process, Romb/Diamant = Beslut (Ja/Nej), Parallellogram = Indata/Utdata, Pilar = Flödeslinje",
            "Rektangel = Start/Slut, Cirkel = Beslut, Triangel = Indata/Utdata",
            "Romb = Start/Slut, Oval = Beräkning, Parallellogram = Beslut",
            "Alla steg ritas alltid med fyrkanter"
        ],
        "ratt_index": 0,
        "forklaring": "Dessa fem grundsymboler bygger upp flödesscheman för att planera, dokumentera och felsöka processer."
    },
    {
        "kategori": "Flowchart",
        "fraga": "I Övning 3 (Lösenordskontroll) och Övning 4 (Betygssättning): Vad är viktigt kring fel lösenord respektive poängordning?",
        "alternativ": [
            "Vid fel lösenord kollas om försök finns kvar (annars kontolåsning); vid betyg kontrolleras först ogiltig poäng (<0 eller >100) och sedan från högsta betyg (≥90) och nedåt",
            "Kontot låses aldrig vid fel lösenord; betyg testas alltid från lägsta (≥50) först",
            "Flödesscheman läses alltid nerifrån och upp",
            "Ogiltig inmatning behöver aldrig hanteras i flödesscheman"
        ],
        "ratt_index": 0,
        "forklaring": "Flödesscheman går uppifrån och ner: validera gränser först (<0 eller >100) och kontrollera sedan villkoren i fallande ordning (90, 80, 70, 60, 50)."
    }
]

def run_quiz():
    print("=" * 65)
    print("  QUIZ: GIT, BRANCHES, PUSH/PULL & FLOWCHARTS (PROGRAMMERING 1)")
    print("=" * 65)
    poang = 0
    fragor = QUESTIONS.copy()
    random.shuffle(fragor)

    for nr, q in enumerate(fragor, 1):
        print(f"\nFråga {nr}/{len(fragor)} [{q['kategori']}]:")
        print(q["fraga"])
        
        alternativ_med_index = list(enumerate(q["alternativ"]))
        random.shuffle(alternativ_med_index)
        
        ratt_bokstav = ""
        bokstaver = ["A", "B", "C", "D"]
        
        for idx, (orig_idx, text) in enumerate(alternativ_med_index):
            bokstav = bokstaver[idx]
            if orig_idx == q["ratt_index"]:
                ratt_bokstav = bokstav
            print(f"  {bokstav}) {text}")
            
        svar = input("\nDitt svar (A/B/C/D): ").strip().upper()
        if svar == ratt_bokstav:
            print("✅ Rätt svar!")
            poang += 1
        else:
            print(f"❌ Fel! Rätt svar var {ratt_bokstav}.")
        print(f"💡 Förklaring: {q['forklaring']}")
        print("-" * 65)

    print(f"\n🎉 Quiz klart! Du fick {poang} av {len(fragor)} rätt ({round(poang/len(fragor)*100)}%).")

if __name__ == "__main__":
    run_quiz()
