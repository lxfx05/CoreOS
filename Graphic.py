cat > nxa.py << 'EOF'
import os, sys, time, select

def clear_scr(): sys.stdout.write("\033c")

def draw(cursor, apps, focus_idx, alert, popup=None):
    clear_scr()
    grid = [list(" " * 60) for _ in range(16)]
    for c in range(60): grid[0][c], grid[14][c] = "-", "-"
    for r in range(15): grid[r][0], grid[r][59] = "|", "|"
    grid[15] = list(f"| [CLK] [CAL] [TMR] | SYSTEM ONLINE | {alert}".ljust(60))
    
    vis = [a for a in apps if not a['minimized']]
    n = len(vis)
    for idx, app in enumerate(vis):
        color = "\033[1;30m" if popup else ("\033[1;32m" if alert and app['name'] == 'clk' else ("\033[1;34m" if apps.index(app) == focus_idx else "\033[1;30m"))
        if n == 1: aw, ah, ax, ay = 58, 13, 1, 1
        elif n == 2: aw, ah, ax, ay = 28, 13, (1 if idx==0 else 30), 1
        else: aw, ah, ax, ay = 28, 6, (1 if idx%2==0 else 30), (1 if idx<2 else 7)
        app['render_area'] = (ax, ay, aw, ah)
        for r in range(ah):
            for c in range(aw):
                tr, tc = ay + r, ax + c
                if 1 <= tr < 14 and 1 <= tc < 59:
                    if r == 0: char = "="
                    elif r == ah-1: char = "-"
                    elif c == 0 or c == aw-1: char = "|"
                    else:
                        content = app['ui'][r-1] if r-1 < len(app['ui']) else ""
                        char = content[c-1] if c-1 < len(content) else " "
                    grid[tr][tc] = f"{color}{char}\033[0m"

    if popup:
        px, py = 15, 5
        for r in range(5):
            for c in range(30):
                grid[py+r][px+c] = f"\033[1;37m#\033[0m"
        msg = f" {popup} (Y/N) "
        for i, char in enumerate(msg): grid[py+2][px+2+i] = f"\033[1;33m{char}\033[0m"

    if not popup: grid[cursor['y']][cursor['x']] = "\033[1;31mX\033[0m"
    sys.stdout.write("".join(["".join(r) + "\n" for r in grid]))
    sys.stdout.flush()
EOF
