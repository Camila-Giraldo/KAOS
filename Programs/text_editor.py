import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from SessionManager import SessionManager

class TextEditor(tk.Frame):

    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.root.title('Text Editor')
        self.root.geometry('480x400')

        self.session = SessionManager()
        self.gui_inicialize()
    
    def gui_inicialize(self):
        self.text_area = tk.Text(self.root)
        
        frm_buttons = tk.Frame(self.root, relief=tk.RAISED, bd=2)
        btn_open = tk.Button(frm_buttons, text='Open...', command=self.open_file)
        btn_save = tk.Button(frm_buttons, text='Save...', command=self.save_file)

        btn_open.grid(row=0, column=0, sticky='ew', padx=5, pady=5)
        btn_save.grid(row=1, column=0, sticky='ew', padx=5)

        frm_buttons.grid(row=0, column=0, sticky='ns')
        self.text_area.grid(row=0, column=1, sticky='nsew')
    
    def open_file(self):
        info = self.session.load_session()
        file_path = ""
        if info:
            last_user, last_path = list(info.items())[-1]
            path = last_path
            file_path = askopenfilename(initialdir=path, filetypes=[('Archivo de texto', ('*.txt'))])

        if not file_path:
            return
        
        self.text_area.delete(1.0, tk.END)

        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            self.text_area.insert(tk.END, content)
        
        self.root.title(f'Text Editor - {file_path}')

    def open_file_exp(self, path):
        if not path:
            return

        self.text_area.delete(1.0, tk.END)

        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
            self.text_area.insert(tk.END, content)

        self.root.title(f'Text Editor - {path}')

    def save_file(self):
        info = self.session.load_session()
        file_path = ""
        if info:
            last_user, last_path = list(info.items())[-1]
            path = last_path
            file_path = asksaveasfilename(
                initialdir=path,
                defaultextension='txt',
                filetypes=[('Archivos de texto', '*.txt')])

        if not file_path:
            return
        
        with open(file_path, 'wt', encoding='utf-8') as f:
            content = self.text_area.get(1.0, tk.END)
            f.write(content)
        
        self.root.title(f'Text Editor - {file_path}')

def main():
    root = tk.Tk()
    ventana = TextEditor(root)
    ventana.mainloop()

if __name__ == "__main__":
    main()
