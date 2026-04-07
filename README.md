<div align="center">

# 🌌 NXA-OS: Low-Level Terminal Emulator

</div>

### 📂 **Kernel & Security Protocols**
This system emulates a low-level terminal environment with advanced window management and security protocols. Built for efficiency, it features an automated **Auto-Split** logic for multi-tasking.

### 🛠️ **System Architecture**
<p align="left">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=python,linux,bash,md,apple" />
  </a>
</p>

---

### 📲 **Mobile Installation (iOS/iPadOS)**
To run this system on Apple devices, you must install a Linux-based shell environment:

1. Download the **iSH Shell** app from the Apple App Store.
2. Open iSH and install the necessary dependencies by typing:
   `apk update && apk add python3 git`
3. **Clone the Repository**:
   `git clone https://github.com/lxfx05/CoreOS`
   `cd CoreOS`
   `python3 nxa.py`

  
4. **Emergency Procedure**: If cloning fails, manually create the files (e.g., using nano), then copy and paste the contents of each .py file from the repository one by one.
5. **Execution**: To launch and interact with the operating system, type:
   `python3 nxa.py`

---

### 🕹️ **Navigation & Control**
* **W / S / A / D**: Move the red cursor (X) within the interface.
* **T**: Focus on the window under the cursor (the border turns blue). Required before interacting with or closing an app.
* **X**: Close the currently focused window. Remaining windows will automatically expand to full screen.

### 📂 **Command Line & Apps**
Type the command and press Enter to execute:

* **clk**: Initialize Clock module.
* **cal**: Initialize Calculator module.
* **tmr**: Switch Clock to Timer mode.
    * Input Format: HH/MM/SS (e.g., 0/5/0 for 5 minutes).
    * Alert: A green [FINISH!] tag appears on completion.
    * Reset: Press C to stop the timer and return to Clock mode.

### 🧮 **Calculator Module**
* **Direct Input**: Type operations directly (e.g., 50*2+10).
* **History**: The system automatically logs numerical results, filtering out plain text.

### ⚠️ **System Maintenance**
* **Q (Reboot)**: Initiate the system reboot sequence.
* **Z (Shutdown)**: Initiate the power-down sequence.
* **Confirmation Protocol**: During hibernation or shutdown, you must confirm:
    * **Y**: Confirm Action.
    * **N**: Abort and return to OS.

---

<div align="center">

### 🤝 **The Architect**
<a href="mailto:lucafinaldi3@gmail.com"><img src="https://img.shields.io/badge/MAIL-D14836?style=for-the-badge&logo=gmail&logoColor=white" /></a>
<a href="https://lxfx05.github.io/Website/"><img src="https://img.shields.io/badge/WEBSITE-3b82f6?style=for-the-badge&logo=google-chrome&logoColor=white" /></a>

<br />
<br />

</div>

---
<p align="left">
  <i>Architected by <b>Luca Finaldi</b></i> 
</p>
