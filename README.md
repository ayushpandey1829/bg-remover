# Background Remover

A simple Flask web app that removes the background from an image. It is built for an open-source workshop, so it is a good place to make your first Pull Request.

## Features

- Upload an image by drag and drop or by clicking to choose a file
- See the original and the result side by side, with the result shown on a checkerboard so transparency is visible
- Download the result as a transparent PNG
- Choose between three ways of removing the background:

| Method | How it works | API key needed? |
|---|---|---|
| `rembg` | Python library, runs locally on your computer | No |
| `removebg` | [remove.bg](https://www.remove.bg/api) API | Yes |
| `clipdrop` | [ClipDrop](https://clipdrop.co/apis) API | Yes |

## Requirements

- **Python 3.12.** Newer versions (3.13 and 3.14) may fail to install the dependencies of `rembg`.
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

**macOS / Linux:**

```bash
git clone https://github.com/<USERNAME>/bg-remover.git
cd bg-remover
python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

Then open http://127.0.0.1:5000 in your browser.

> The first start can take a minute or two while the libraries load. After that, it is much faster.

## Downloading the model (rembg)

The app uses the small `u2netp` model (about 4 MB). It is normally downloaded automatically on first use. If the download hangs because of a slow or restricted network, download it manually:

1. Download the file: https://github.com/danielgatis/rembg/releases/download/v0.0.0/u2netp.onnx
2. Place it in the following folder (create the folder if it does not exist):
   - Windows: `C:\Users\<your-name>\.u2net\`
   - macOS / Linux: `~/.u2net/`

##
