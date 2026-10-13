# Background Remover

Ek simple Flask web app jo image ka background remove karta hai. Ye project **open source workshop** ke liye bana hai, yahan aap apna pehla Pull Request bana sakte ho.

Teen tareeke support hote hain:

| Method | Kaise kaam karta hai | API key? |
|---|---|---|
| `rembg` | Python library, locally chalti hai | Nahi chahiye |
| `removebg` | [remove.bg](https://www.remove.bg/api) API | Chahiye |
| `clipdrop` | [ClipDrop](https://clipdrop.co/apis) API | Chahiye |

## Requirements

- **Python 3.12** (3.13 / 3.14 par rembg ke dependencies fail ho sakte hain)
- Git

## Setup

**Windows (PowerShell):**
```powershell
git clone https://github.com/<USERNAME>/bg-remover.git
cd bg-remover
py -3.12 -m venv venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

**Mac / Linux:**
```bash
git clone https://github.com/<USERNAME>/bg-remover.git
cd bg-remover
python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

Browser me kholo: http://127.0.0.1:5000

## Model download (rembg)

App chhota model `u2netp` (~4 MB) use karta hai. Agar auto-download atak jaye (slow ya blocked network), to manually karo:

1. Download: https://github.com/danielgatis/rembg/releases/download/v0.0.0/u2netp.onnx
2. File ko `C:\Users\<naam>\.u2net\` (Windows) ya `~/.u2net/` (Mac/Linux) me rakho.

## API keys (optional)

```bash
cp .env.example .env     # Windows: copy .env.example .env
```
`.env` me keys daalo, phir server restart karo. **`.env` kabhi commit mat karna.**

## Project structure

```
bg-remover/
├── app.py                # Flask server + background removal functions
├── templates/index.html  # Frontend (HTML + CSS + JS)
├── requirements.txt      # Python libraries
├── .env.example          # API keys ka sample
├── CONTRIBUTING.md       # Contribute karne ka guide
└── .github/              # Issue aur PR templates
```

## Contribute karna

Pehle [CONTRIBUTING.md](CONTRIBUTING.md) padho, phir **Issues** tab me `good first issue` label wala koi issue chuno.

## License

[MIT](LICENSE)
