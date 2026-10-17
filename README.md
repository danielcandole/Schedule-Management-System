# Schedule-Management-System 2025

## Developers
Daniel Candole  
Joreese Clyde  
Novem Austria

## Installation
```bash
Linux: use pip3, python3
Windows: use pip, py

Note: check "Source-Code" folder. E run lang to (F5). No need na ang run.py.
Naa didto akoang gi buhat nga experiment ug testing
```

**Clone the repository:**

```bash
git clone https://github.com/DanielCSjs/Schedule-Management-System.git
cd Schedule-Management-System
```
Create a virtual environment:
```
py -m venv vir-e         (windows)
python3 -m venv vir-e    (linux)
```

# Linux / macOS
```
source vir-e/bin/activate
```
# Windows
```
.\vir-e\Scripts\activate
```

Install required packages (if any, e.g., PIL for images):
```
pip install -r requirements.txt     (windows)
pip3 install -r requirements.txt    (linux)
```
Run the app:
```
py run.py         (windows)
python3 run.py    (linux)
```

Creating an Executable (.exe)
To turn the app into a standalone Windows executable:
Install PyInstaller:
```
pip install pyinstaller
```
Build the .exe:
```
pyinstaller --onefile --windowed main.py
```

```
--onefile → creates a single .exe file.
--windowed → hides the console window (GUI apps only).
```

Optional: Add an icon:
```
pyinstaller --onefile --windowed --icon=myicon.ico main.py
```

Find the .exe:
After building, your executable will be in the dist folder:
```
dist/
 └─ main.exe
```
Note
If your app uses images, fonts, or other files, include them using --add-data:

```
pyinstaller --onefile --windowed --add-data "assets;assets" main.py
(MAO NI ANG SECOND OPTION)
pyinstaller --noconsole --onefile --add-data "authActivity;authActivity" --add-data "assets;assets" --add-data "utils;utils" main.py
```
Always test the .exe on a computer without Python installed to ensure it works.

Happy Coding!
---
