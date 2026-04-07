cat >> nxa.py << 'EOF'
if __name__ == "__main__":
    cursor, history = {'x': 30, 'y': 7}, []
    tmr_val, tmr_run, alert, cur_in = 0, False, "", ""
    apps = [{'name': 'clk', 'ui': [], 'minimized': False, 'render_area': (0,0,0,0)},
            {'name': 'cal', 'ui': [], 'minimized': False, 'render_area': (0,0,0,0)}]
    focus_idx, last_t, mode = 0, 0, "OS"
    
    while True:
        now = time.time()
        if mode == "OS" and now - last_t >= 1.0:
            last_t = now
            if tmr_run and tmr_val > 0:
                tmr_val -= 1
                m, s = divmod(tmr_val, 60); h, m = divmod(m, 60)
                apps[0]['ui'] = ["  TIMER ACTIVE", "--------------", f" T- {h:02}:{m:02}:{s:02} "]
                if tmr_val == 0: alert, tmr_run = "\033[1;32m[FINISH!]\033[0m", False
            else: apps[0]['ui'] = ["  CLOCK MODE", "--------------", f" {time.strftime('%H:%M:%S')} "]
            apps[1]['ui'] = ["  CALC HISTORY", "--------------"] + [h_l[:25] for h_l in history[-3:]] + [f"> {cur_in}|"]
            draw(cursor, apps, focus_idx, alert)

        if select.select([sys.stdin], [], [], 0.02)[0]:
            cmd = sys.stdin.readline().strip().lower()
            if mode == "OS":
                if cmd == 'z': mode = "SHUTDOWN"
                elif cmd == 'q': mode = "REBOOT"
                elif cmd == 'c': cur_in, tmr_val, tmr_run, alert = "", 0, False, ""
                elif cmd == 't':
                    for i, a in enumerate(apps):
                        if not a['minimized']:
                            ax, ay, aw, ah = a['render_area']
                            if ax <= cursor['x'] < ax+aw and ay <= cursor['y'] < ay+ah: focus_idx = i; break
                elif cmd == 'x':
                    apps[focus_idx]['minimized'] = True
                    for i, a in enumerate(apps):
                        if not a['minimized']: focus_idx = i; break
EOF
