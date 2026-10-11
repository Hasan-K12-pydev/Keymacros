import customtkinter as ctk
import keyboard
import threading
import time
import os

# Set global CustomTkinter theme configurations
ctk.set_appearance_mode("Dark")  # Modes: "System", "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue", "green", "dark-blue"

class SpammerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Key Spammer v1.3 (CTk)")
        self.root.geometry("360x420")
        self.root.resizable(False, False)
        
        # Set window icon (checking file existence to prevent errors)
        if os.path.exists('icon.ico'):
            self.root.iconbitmap('icon.ico')
        
        self.running = False
        
        # --- UI Elements ---
        title_label = ctk.CTkLabel(root, text="Custom Keyboard Macro", font=ctk.CTkFont(family="Arial", size=16, weight="bold"))
        title_label.pack(pady=15)
        
        # Key Configuration Frame (Replacing old ttk.LabelFrame)
        key_frame = ctk.CTkFrame(root)
        key_frame.pack(pady=10, fill="x", padx=20)
        
        key_frame_title = ctk.CTkLabel(key_frame, text=" Keys to Activate & Map ", font=ctk.CTkFont(size=12, weight="bold"))
        key_frame_title.pack(anchor="w", padx=10, pady=(5, 5))
        
        # Key 1 Setup
        self.var_1 = ctk.BooleanVar(value=True)
        f1 = ctk.CTkFrame(key_frame, fg_color="transparent")
        f1.pack(anchor="w", fill="x", pady=4, padx=10)
        ctk.CTkCheckBox(f1, text="Key 1:", variable=self.var_1).pack(side="left")
        self.entry_key1 = ctk.CTkEntry(f1, width=70)
        self.entry_key1.insert(0, "q")
        self.entry_key1.pack(side="right")
        
        # Key 2 Setup
        self.var_2 = ctk.BooleanVar(value=True)
        f2 = ctk.CTkFrame(key_frame, fg_color="transparent")
        f2.pack(anchor="w", fill="x", pady=4, padx=10)
        ctk.CTkCheckBox(f2, text="Key 2:", variable=self.var_2).pack(side="left")
        self.entry_key2 = ctk.CTkEntry(f2, width=70)
        self.entry_key2.insert(0, "f")
        self.entry_key2.pack(side="right")
        
        # Key 3 Setup
        self.var_3 = ctk.BooleanVar(value=True)
        f3 = ctk.CTkFrame(key_frame, fg_color="transparent")
        f3.pack(anchor="w", fill="x", pady=4, padx=10)
        ctk.CTkCheckBox(f3, text="Key 3:", variable=self.var_3).pack(side="left")
        self.entry_key3 = ctk.CTkEntry(f3, width=70)
        self.entry_key3.insert(0, "tab")
        self.entry_key3.pack(side="right")
        
        # Speed Delay Frame
        speed_frame = ctk.CTkFrame(root, fg_color="transparent")
        speed_frame.pack(pady=15)
        
        ctk.CTkLabel(speed_frame, text="Key Delay (Seconds):").pack(side="left", padx=5)
        self.speed_entry = ctk.CTkEntry(speed_frame, width=60)
        self.speed_entry.insert(0, "0.1")
        self.speed_entry.pack(side="left", padx=5)
        
        # Status & Toggle Button
        self.status_label = ctk.CTkLabel(root, text="Status: Stopped", text_color="#ff4444", font=ctk.CTkFont(family="Arial", size=12, weight="bold"))
        self.status_label.pack(pady=5)
        
        self.btn_toggle = ctk.CTkButton(root, text="START (F8)", command=self.toggle_spammer, width=160, font=ctk.CTkFont(weight="bold"))
        self.btn_toggle.pack(pady=10)
        
        # Start background polling thread
        self.spammer_thread = threading.Thread(target=self.key_spammer_loop, daemon=True)
        self.spammer_thread.start()
        
        # Register system macro trigger
        keyboard.add_hotkey('f8', self.toggle_spammer)
        
    def toggle_spammer(self):
        self.running = not self.running
        if self.running:
            self.root.focus_set()  # Shifts focus away from entry inputs to prevent loops
            self.status_label.configure(text="Status: RUNNING...", text_color="#00cc66")
            self.btn_toggle.configure(text="STOP (F8)", fg_color="#cc3333", hover_color="#992222")
        else:
            self.status_label.configure(text="Status: Stopped", text_color="#ff4444")
            self.btn_toggle.configure(text="START (F8)", fg_color=["#3B8ED0", "#1F6AA5"], hover_color=["#2B719E", "#144870"]) # Default theme colors

    def key_spammer_loop(self):
        while True:
            if self.running:
                try:
                    delay = float(self.speed_entry.get())
                    if delay < 0.01: delay = 0.01
                except ValueError:
                    delay = 0.1
                
                # Fetch custom mapped keys dynamically
                key1 = self.entry_key1.get().strip()
                key2 = self.entry_key2.get().strip()
                key3 = self.entry_key3.get().strip()
                
                if self.var_1.get() and key1 and self.running:
                    keyboard.send(key1)
                    time.sleep(delay)
                    
                if self.var_2.get() and key2 and self.running:
                    keyboard.send(key2)
                    time.sleep(delay)
                    
                if self.var_3.get() and key3 and self.running:
                    keyboard.send(key3)
                    time.sleep(delay)
            else:
                time.sleep(0.1)

if __name__ == "__main__":
    root = ctk.CTk()
    app = SpammerGUI(root)
    root.mainloop()
