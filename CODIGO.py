import tkinter as tk
import subprocess
from time import sleep
import psutil

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("CMD AUTÔNOMO")
        
        # Frames
        self.frame_path = tk.Frame(self.root)
        self.frame_path.pack(pady=5)
        
        self.frame_file = tk.Frame(self.root)
        self.frame_file.pack(pady=5)
        
        self.frame_buttons = tk.Frame(self.root)
        self.frame_buttons.pack(pady=10)
        
        self.frame_status = tk.Frame(self.root)
        self.frame_status.pack(pady=5)
        
        # Labels
        tk.Label(self.frame_path, text="CAMINHO:").pack(side=tk.LEFT)
        tk.Label(self.frame_file, text="ARQUIVO:").pack(side=tk.LEFT)
        tk.Label(self.frame_status, text="STATUS:").pack(side=tk.LEFT)
        
        # Entries
        self.entry_path = tk.Entry(self.frame_path, width=50)
        self.entry_path.pack(side=tk.LEFT)
        self.entry_path.bind("<KeyRelease>", self.check_fields) 
        
        self.entry_file = tk.Entry(self.frame_file, width=20)
        self.entry_file.pack(side=tk.LEFT)
        self.entry_file.bind("<KeyRelease>", self.check_fields)  
        
        # Status
        self.status_var = tk.StringVar()
        self.status_var.set("PARADO")
        self.status_label = tk.Label(self.frame_status, textvariable=self.status_var)
        self.status_label.pack(side=tk.LEFT)
        
        # Buttons
        self.button_start = tk.Button(self.frame_buttons, text="INICIAR", command=self.start_execution)
        self.button_start.pack(side=tk.LEFT, padx=5)
        self.button_start.config(state="disabled")  
        
        self.button_restart = tk.Button(self.frame_buttons, text="REINICIAR", command=self.restart_execution)
        self.button_restart.pack(side=tk.LEFT, padx=5)
        self.button_restart.config(state="disabled")
        
        self.button_stop = tk.Button(self.frame_buttons, text="PARAR", command=self.stop_execution)
        self.button_stop.pack(side=tk.LEFT, padx=5)
        self.button_stop.config(state="disabled")  
        
        self.process = None
        
    def check_fields(self, event):
        if self.entry_path.get() and self.entry_file.get():
            self.button_start.config(state="active")
        else:
            self.button_start.config(state="disabled")
        
    def start_execution(self):
        path = self.entry_path.get()
        file = self.entry_file.get()
        
        if not file.endswith(".py"):
            file += ".py"
        
        cmd = f'cd /d {path} && python {file}'

        try:
            self.process = subprocess.Popen(cmd, shell=True)
            self.status_var.set("EM EXECUÇÃO!")
            self.entry_path.config(state="disabled")
            self.entry_file.config(state="disabled")
            self.button_restart.config(state="active")
            self.button_stop.config(state="active")
            self.button_start.config(state="disabled")
        except Exception as e:
            self.status_var.set(f"ERRO: {e}")
        
    def restart_execution(self):
        try:
            self.status_var.set("REINICIANDO...")
            self.root.update() 
            sleep(1)
            self.stop_execution()
            self.start_execution()
        except Exception as e:
            self.status_var.set(f"ERRO: {e}")
            
    def stop_execution(self):
        try:
            if self.process is not None:
                parent = psutil.Process(self.process.pid)
                for child in parent.children(recursive=True):
                    child.kill()
                parent.kill()
                self.status_var.set("PARADO")
                self.entry_path.config(state="normal")
                self.entry_file.config(state="normal")
                self.button_restart.config(state="disabled")
                self.button_stop.config(state="disabled")
                self.button_start.config(state="active")
        except Exception as e:
            self.status_var.set(f"ERRO: {e}")

root = tk.Tk()
app = App(root)
root.mainloop()
