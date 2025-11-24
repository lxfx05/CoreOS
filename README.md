# CoreOS 2.0 (Termux) 👨🏻‍💻

CoreOS 2.0 is a lightweight ASCII-based terminal operating system simulation for Android Termux.
It runs directly in Python and supports interactive window movement, apps, and a live clock.

---

## Repository Structure 🗂️

CoreOS/
├─ nxa.py        # Main Python script
├─ screen.nxa    # ASCII display layout
├─ token.nxa     # Key mappings and help
└─ apps/
   └─ clock.nxa # Clock app (text-based)
Os.sh            # Optional setup/run script
token.nxa        # Same as in CoreOS/

---

## Requirements ❓

- Termux on Android
- Python 3 installed
- Storage access granted (`termux-setup-storage`)


## Installation 📥

1. Clone this repository:

```bash
git clone https://github.com/lxfx05/CoreOS.git
````

2. Go to the CoreOS folder:
````
cd CoreOS
````

3. Make sure ````nxa.py```` is executable:
````
chmod +x nxa.py
````

# Running CoreOS 🖲️

Launch CoreOS with:
````
python3 nxa.py
````

Or, if you have a helper script ````Os.sh````
````
./Os.sh
````

# Usage

Window controls🎛️
````
1 → move right
3 → move left
5 → move up
7 → move down
2 → diagonal up-right
4 → diagonal up-left
6 → diagonal down-right
8 → diagonal down-left
C → center window
O → open/close window
H+/H- → increase/decrease window height
W+/W- → increase/decrease window width
Z → open apps menu
? → show this help
Q → quit program
````

# Available apps📦

- Clock: Shows the current time and daNotes

Notes
- clock files are self-contained; no external dependencies are required.

- -All best in Termux home directory (~/CoreOS) to avoid storage permission issues.
