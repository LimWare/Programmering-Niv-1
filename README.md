# Git, Branches, Push/Pull & Flowchart Quiz (Programmering 1)

Detta repository innehåller ett komplett, interaktivt quiz och instuderingsmaterial baserat på:
- **Lektion 10:** Git Grunder, Installation, Konfiguration & Lokalt arbeidsflöde (`init`, `add`, `commit`, `status`, `log`, `checkout`)
- **Lektion 11:** Branches (`git branch`, `checkout -b`, `switch -c`, `branch -d`) samt Fjärr-repo (`push`, `pull` & behörigheter inför nästa lektion)
- **Lektion 13:** Flowchart / Flödesscheman (Symboler, verktyg och övningsexempel 1–4)

## Innehåll i repot
1. **`index.html`** – Ett snyggt, interaktivt webb-quiz med **30 frågor**, kategorifilter och direkt feedback. Kan öppnas direkt i din webbläsare eller publiceras gratis via **GitHub Pages**!
2. **`quiz.py`** – Ett körbart terminal-quiz skrivet i Python (`python quiz.py`).

## Så här laddar du upp detta projekt till ditt GitHub-konto
Öppna terminalen (t.ex. Git Bash eller din inbyggda terminal) i mappen där dessa filer ligger och kör:

```bash
git init
git add .
git commit -m "Lägg till Git, Push/Pull och Flowchart quiz"
git branch -M main
git remote add origin <DIN-GITHUB-REPO-URL>
git push -u origin main
```
