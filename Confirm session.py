cat >> nxa.py << 'EOF'
                elif cmd in ['clk', 'cal', 'tmr']:
                    if cmd == 'clk': apps[0]['minimized'] = False; tmr_run = False
                    if cmd == 'cal': apps[1]['minimized'] = False; focus_idx = 1
                    if cmd == 'tmr':
                        apps[0]['minimized'] = False; focus_idx = 0
                        sys.stdout.write("\033[1;34m>> TIMER (H/M/S): \033[0m"); sys.stdout.flush()
                        try:
                            t_in = sys.stdin.readline().strip().split("/")
                            tmr_val = int(t_in[0])*3600 + int(t_in[1])*60 + int(t_in[2])
                            tmr_run, alert = True, ""
                        except: pass
                elif cmd in ['w','a','s','d']:
                    if cmd == 'w': cursor['y'] = max(1, cursor['y'] - 1)
                    elif cmd == 's': cursor['y'] = min(13, cursor['y'] + 1)
                    elif cmd == 'a': cursor['x'] = max(1, cursor['x'] - 2)
                    elif cmd == 'd': cursor['x'] = min(57, cursor['x'] + 2)
                else:
                    if any(c.isdigit() for c in cmd):
                        try: history.append(f"{cmd}={eval(cmd)}")
                        except: history.append("Error")
                draw(cursor, apps, focus_idx, alert)
            
            else: # Modalità Popup (Ibernazione)
                if cmd == 'y':
                    if mode == "SHUTDOWN": sys.exit()
                    if mode == "REBOOT": os.execv(sys.executable, ['python3'] + sys.argv)
                elif cmd == 'n': mode = "OS" # Ritorno all'OS
            
        if mode != "OS":
            draw(cursor, apps, focus_idx, alert, popup="SPEGNERE ORA?" if mode == "SHUTDOWN" else "RIAVVIARE ORA?")
EOF
