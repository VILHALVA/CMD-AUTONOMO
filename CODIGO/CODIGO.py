import customtkinter as ctk
from tkinter import filedialog
import subprocess
import psutil
import threading
import os
import datetime

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("CMD AUTÔNOMO")
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")  
        self.root.resizable(True, True)

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.label_title = ctk.CTkLabel(root, text="CMD AUTÔNOMO", font=("Arial", 32, "bold"))
        self.label_title.pack(pady=10)

        self.entry_pasta = ctk.CTkEntry(root, width=600, placeholder_text="SELECIONE O ARQUIVO!", state="readonly")
        self.entry_pasta.pack(pady=10)

        self.btn_pasta = ctk.CTkButton(root, text="SELECIONAR", command=self.selecionar_pasta)
        self.btn_pasta.pack(pady=10)

        self.status_textbox = ctk.CTkTextbox(root, width=700, height=300, state="disabled")
        self.status_textbox.pack(pady=10)

        self.bottom_frame = ctk.CTkFrame(root)
        self.bottom_frame.pack(pady=5)

        self.log_switch = ctk.CTkSwitch(
            self.bottom_frame, text="LOG OFF", command=self.toggle_log,
            switch_width=40, switch_height=20
        )
        self.log_switch.pack(side="right", padx=20)

        self.logging_enabled = False
        self.log_file = None

        self.frame_buttons = ctk.CTkFrame(root)
        self.frame_buttons.pack(pady=10)

        self.button_start = self.create_button("INICIAR", self.start_execution, "disabled")
        self.button_stop = self.create_button("PARAR", self.stop_execution, "disabled")
        self.button_copy = self.create_button("COPIAR", self.copy_to_clipboard, "disabled")
        self.button_clear = self.create_button("LIMPAR", self.clear_fields, "disabled")

        self.process = None
        self.file_path = ""

    def create_button(self, text, command, state):
        btn = ctk.CTkButton(self.frame_buttons, text=text, command=command, state=state)
        btn.pack(side="left", padx=10)
        return btn

    def selecionar_pasta(self):
        file_path = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
        if file_path:
            self.file_path = file_path
            self.update_entry(self.entry_pasta, file_path)
            self.set_buttons_state(start="normal", clear="normal")

    def start_execution(self):
        if not self.file_path:
            return
        if self.process and self.process.poll() is None:
            self.append_to_textbox("⚠️AVISO: O PROCESSO JÁ ESTÁ EM EXECUÇÃO!\n")
            return

        self.set_textbox_state("normal")
        self.status_textbox.delete("1.0", "end")
        self.set_textbox_state("disabled")

        directory = os.path.dirname(self.file_path)
        file = os.path.basename(self.file_path)
        self.cmd = f'cd /d "{directory}" && python "{file}"'

        self.append_to_textbox(f"🤖[COMANDO]: {self.cmd}\n")

        try:
            self.process = subprocess.Popen(
                self.cmd, shell=True, stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT, text=True, bufsize=1,
                creationflags=subprocess.CREATE_NEW_PROCESS_GROUP
            )
            self.append_to_textbox("👉EM EXECUÇÃO!\n")
            threading.Thread(target=self.read_output_thread, daemon=True).start()

            self.btn_pasta.configure(state="disabled")
            self.set_buttons_state(start="disabled", stop="normal", copy="normal", clear="disabled")

        except Exception as e:
            self.append_to_textbox(f"❌ERRO: {e}\n")

    def read_output_thread(self):
        try:
            for line in self.process.stdout:
                if line:
                    self.append_to_textbox(line)
        except Exception as e:
            self.append_to_textbox(f"❌[ERRO NA LEITURA]: {e}\n")
        finally:
            self.append_to_textbox("👉FINALIZADO!\n")
            self.btn_pasta.configure(state="disabled")
            self.set_buttons_state(start="normal", stop="disabled", copy="normal", clear="normal")

    def append_to_textbox(self, text):
        def append():
            self.set_textbox_state("normal")
            self.status_textbox.insert("end", text)
            self.status_textbox.see("end")
            self.set_textbox_state("disabled")

            if self.logging_enabled and self.log_file:
                try:
                    with open(self.log_file, "a", encoding="utf-8") as f:
                        f.write(text)
                except Exception as e:
                    print(f"Erro ao gravar no log: {e}")
        self.root.after(0, append)

    def stop_execution(self):
        try:
            if self.process:
                proc = psutil.Process(self.process.pid)
                for child in proc.children(recursive=True):
                    child.kill()
                proc.kill()
                self.process.wait(timeout=5)
                self.process = None

                self.append_to_textbox(f"🤖[COMANDO PID]: {proc.pid}\n")
                self.set_buttons_state(start="normal", stop="disabled", copy="normal", clear="normal")
        except Exception as e:
            self.append_to_textbox(f"❌ERRO: {e}\n")

    def copy_to_clipboard(self):
        self.set_textbox_state("normal")
        content = self.status_textbox.get("1.0", "end-1c")
        self.set_textbox_state("disabled")

        if content.strip():
            self.root.clipboard_clear()
            self.root.clipboard_append(content)
            self.root.update()
            self.show_popup("TEXTO COPIADO!")

    def show_popup(self, message):
        popup = ctk.CTkLabel(self.root, text=message, text_color="white", bg_color="#333333", font=("Arial", 14, "bold"))
        popup.place(relx=0.5, rely=0.05, anchor="n")
        self.root.after(3000, popup.destroy)

    def clear_fields(self):
        self.update_entry(self.entry_pasta, "")
        self.status_textbox.configure(state="normal")
        self.status_textbox.delete("1.0", "end")
        self.status_textbox.configure(state="disabled")
        self.file_path = ""
        self.btn_pasta.configure(state="normal")
        self.set_buttons_state(start="disabled", stop="disabled", copy="disabled", clear="disabled")

    def toggle_log(self):
        self.logging_enabled = bool(self.log_switch.get())
        if self.logging_enabled:
            now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            log_dir = os.path.join(os.getcwd(), "LOG")
            os.makedirs(log_dir, exist_ok=True)  
            self.log_file = os.path.join(log_dir, f"CMD AUTONOMO_{now}.txt")
            self.log_switch.configure(text="LOG ON", progress_color="blue")
            self.append_to_textbox(f"📁LOG INICIADO: {self.log_file}\n")
        else:
            self.log_switch.configure(text="LOG OFF")
            self.append_to_textbox("📁LOG DESATIVADO!\n")
            
    def set_buttons_state(self, start=None, stop=None, copy=None, clear=None):
        if start is not None:
            self.button_start.configure(state=start)
        if stop is not None:
            self.button_stop.configure(state=stop)
        if copy is not None:
            self.button_copy.configure(state=copy)
        if clear is not None:
            self.button_clear.configure(state=clear)

    def set_textbox_state(self, state):
        self.status_textbox.configure(state=state)

    def update_entry(self, entry, value):
        entry.configure(state="normal")
        entry.delete(0, "end")
        entry.insert(0, value)
        entry.configure(state="readonly")

if __name__ == "__main__":
    root = ctk.CTk()
    app = App(root)
    root.mainloop()
