#!/usr/bin/env python3
import os
import sys
import time
import select
from datetime import datetime
import shutil

BLUE = "\033[34m"
RED = "\033[31m"
RESET = "\033[0m"

def clear():
    print("\033c", end="")

def type_print(lines, delay=0.01):
    for line in lines:
        for ch in line:
            print(ch, end="", flush=True)
            time.sleep(delay)
        print()

def type_print_slow(lines, duration=2.0):
    total_chars = sum(len(l) for l in lines)
    delay = duration / total_chars if total_chars > 0 else 0.01
    for line in lines:
        for ch in line:
            print(ch, end="", flush=True)
            time.sleep(delay)
        print()

def load_screen(path="screen.nxa"):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read().splitlines()
    return [" " * 80]

def load_tokens(path="token.nxa"):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    return "File token.nxa mancante!"

# -------------------------
# Render
# -------------------------
max_width = 80
def render_screen(lines, x, y, w, h, open_window=True):
    global max_width
    max_width = max(max_width, *(len(l) for l in lines))
    display = lines.copy()
    for i in range(len(display)):
        if len(display[i]) < max_width:
            display[i] += " " * (max_width - len(display[i]))
    clear()
    color = BLUE if open_window else RED
    display2 = display.copy()
    for i in range(h):
        row = y + i
        if 0 <= row < len(display2):
            line = list(display2[row])
            for j in range(w):
                col = x + j
                if 0 <= col < len(line):
                    if i == 0 or i == h-1:
                        line[col] = "-"
                    elif j == 0 or j == w-1:
                        line[col] = "|"
                    else:
                        line[col] = " "
            display2[row] = "".join(line)
    for l in display2:
        print(f"{color}{l}{RESET}")

# -------------------------
# Movement & animation
# -------------------------
MOVE_MAP = {
    "1": (1,0), "3": (-1,0), "5": (0,-1), "7": (0,1),
    "2": (1,-1), "4": (-1,-1), "6": (1,1), "8": (-1,1)
}

def animate_move(x, y, tx, ty, w, h, lines, ow, speed=0.05):
    while x != tx or y != ty:
        if x < tx: x += 1
        elif x > tx: x -= 1
        if y < ty: y += 1
        elif y > ty: y -= 1
        render_screen(lines, x, y, w, h, ow)
        time.sleep(speed)
    return x, y

# -------------------------
# Boot bar & system check
# -------------------------
def windows7_bar(duration=2.2):
    import sys
    clear()
    type_print(["CoreOS is loading files..."], delay=0.02)
    steps = 30
    step_time = duration / steps
    for i in range(steps+1):
        hashes = "■" * i
        spaces = " " * (steps - i)
        sys.stdout.write(f"\r[{hashes}{spaces}]")
        sys.stdout.flush()
        time.sleep(step_time)
    print("\n")

def check_system():
    checks = ["Checking RAM...", "Checking file Integrity...", "Checking PC status...", "Logging in..."]
    for c in checks:
        type_print([c], delay=0.02)
        time.sleep(0.3)

# -------------------------
# Neofetch
# -------------------------
NEOFETCH_LINES = [
"\033[1;36m            +--------+\033[0m",
"\033[1;35m           /  CORE  /|\033[0m",
"\033[1;34m          +--------+ |\033[0m",
"\033[1;33m          |  OS 2.0 | +\033[0m",
"\033[1;32m          |  TERMUX |/\033[0m",
"\033[1;31m          +---------+\033[0m",
"",
"\033[1;37mcoreOS@termux\033[0m",
"\033[1;36m-------------------------------\033[0m",
"\033[1;35mOS: Core OS 2.0 (Python)\033[0m",
"\033[1;34mDevice: Android (Termux)\033[0m",
"\033[1;33mTerminal: Virtual ASCII TTY\033[0m",
"\033[1;32mPackages: 1 app installed\033[0m",
"\033[1;31mShell: nxa.py interactive\033[0m",
"\033[1;37mTheme: default.json\033[0m",
"\033[1;36mResolution: 80x24\033[0m",
"",
"\033[1;33mWelcome back, operator.\033[0m"
]

# -------------------------
# App: clock (solo testo live)
# -------------------------
def app_clock_render():
    try:
        while True:
            clear()
            now = datetime.now()
            time_str = now.strftime("%I:%M:%S %p")
            date_str = now.strftime("%d/%m/%Y")
            term_width = shutil.get_terminal_size().columns
            print("\n" * 5)
            print(" " * ((term_width - len(time_str)) // 2) + time_str)
            print(" " * ((term_width - len(date_str)) // 2) + date_str)
            print("\n" * 5)
            time.sleep(1)
            if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
                inp = sys.stdin.readline().strip().upper()
                if inp == "Q":
                    break
    except KeyboardInterrupt:
        pass

# -------------------------
# Interactive loop
# -------------------------
def run_interactive(lines):
    global max_width
    max_width = max(len(l) for l in lines)
    for i in range(len(lines)):
        if len(lines[i]) < max_width:
            lines[i] += " " * (max_width - len(lines[i]))
    window_x, window_y = 20, 5
    window_w, window_h = 16, 5
    window_open = True
    apps_available = ["clock"]
    type_print_slow(lines, duration=2.0)
    render_screen(lines, window_x, window_y, window_w, window_h, window_open)
    script_dir = os.path.dirname(os.path.realpath(__file__))
    while True:
        try:
            cmd = input("Token (1-8, C, O, H+/H-, W+/W-, ?, Q, Z): ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting...")
            break
        cmd_up = cmd.upper()
        if cmd_up == "Q":
            # gradual window disappearance
            for i in range(max(window_w, window_h)):
                w = max(0, window_w - i)
                h = max(0, window_h - i)
                render_screen(lines, window_x, window_y, w, h, window_open)
                time.sleep(0.05)
            clear()
            break
        elif cmd_up == "?":
            tokens_text = load_tokens().splitlines()
            type_print_slow(tokens_text, duration=2.0)
            input("\nPremi INVIO per continuare...")
            render_screen(lines, window_x, window_y, window_w, window_h, window_open)
        elif cmd_up == "C":
            target_x = max(0, (max_width - window_w)//2)
            target_y = max(0, (len(lines) - window_h)//2)
            window_x, window_y = animate_move(window_x, window_y, target_x, target_y, window_w, window_h, lines, window_open, speed=0.08)
        elif cmd_up == "O":
            window_open = not window_open
            render_screen(lines, window_x, window_y, window_w, window_h, window_open)
        elif cmd_up == "Z":
            print("*App disponibili*")
            for a in apps_available:
                print(f"- {a}")
            choice = input("Digitare app: ").strip().lower()
            if choice in apps_available:
                if choice == "clock":
                    app_clock_render()
                render_screen(lines, window_x, window_y, window_w, window_h, window_open)
            else:
                print("App non trovata.")
                render_screen(lines, window_x, window_y, window_w, window_h, window_open)
        elif cmd_up in MOVE_MAP and window_open:
            dx, dy = MOVE_MAP[cmd_up]
            tx = max(0, min(window_x + dx, max_width - window_w))
            ty = max(0, min(window_y + dy, len(lines) - window_h))
            window_x, window_y = animate_move(window_x, window_y, tx, ty, window_w, window_h, lines, window_open)
        elif cmd_up == "H+":
            window_h = min(len(lines) - window_y, window_h + 1)
        elif cmd_up == "H-":
            window_h = max(3, window_h - 1)
        elif cmd_up == "W+":
            window_w = min(max_width - window_x, window_w + 1)
        elif cmd_up == "W-":
            window_w = max(3, window_w - 1)
        render_screen(lines, window_x, window_y, window_w, window_h, window_open)

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.realpath(__file__))
    windows7_bar(duration=2.2)
    clear()
    check_system()
    time.sleep(0.5)
    clear()
    type_print(NEOFETCH_LINES, delay=0.01)
    time.sleep(1)
    clear()
    screen_lines = load_screen(os.path.join(script_dir, "screen.nxa"))
    run_interactive(screen_lines)
