import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from SessionManager import SessionManager

class EditorTextoAplicacion(tk.Frame):

    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.root.title('Editor de texto')
        self.root.geometry('480x400')

        self.session = SessionManager()
        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.area_texto = tk.Text(self.root)
        
        frm_botones = tk.Frame(self.root, relief=tk.RAISED, bd=2)
        btn_abrir = tk.Button(frm_botones, text='Abrir...', command=self.abrir_archivo)
        btn_guardar = tk.Button(frm_botones, text='Guardar...', command=self.guardar_archivo)

        btn_abrir.grid(row=0, column=0, sticky='ew', padx=5, pady=5)
        btn_guardar.grid(row=1, column=0, sticky='ew', padx=5)

        frm_botones.grid(row=0, column=0, sticky='ns')
        self.area_texto.grid(row=0, column=1, sticky='nsew')
    
    def abrir_archivo(self):
        info = self.session.load_session()
        ruta_archivo = ""
        if info:
            last_user, last_path = list(info.items())[-1]
            ruta = last_path
            ruta_archivo = askopenfilename(initialdir=ruta, filetypes=[('Archivo de texto', ('*.txt'))])

        if not ruta_archivo:
            return
        
        self.area_texto.delete(1.0, tk.END)

        with open(ruta_archivo, 'r', encoding='utf-8') as f:
            contenido = f.read()
            self.area_texto.insert(tk.END, contenido)
        
        self.root.title(f'Editor de texto - {ruta_archivo}')

    def abrir_archivo(self, ruta):
        if not ruta:
            return

        self.area_texto.delete(1.0, tk.END)

        with open(ruta, 'r', encoding='utf-8') as f:
            contenido = f.read()
            self.area_texto.insert(tk.END, contenido)

        self.root.title(f'Editor de texto - {ruta}')

    def guardar_archivo(self):
        info = self.session.load_session()
        ruta_archivo = ""
        if info:
            last_user, last_path = list(info.items())[-1]
            ruta = last_path
            ruta_archivo = asksaveasfilename(initialdir=ruta, defaultextension='txt', filetypes=[('Archivos de texto', '*.txt')])

        if not ruta_archivo:
            return
        
        with open(ruta_archivo, 'wt', encoding='utf-8') as f:
            contenido = self.area_texto.get(1.0, tk.END)
            f.write(contenido)
        
        self.root.title(f'Editor de texto - {ruta_archivo}')

def main():
    root = tk.Tk()
    ventana = EditorTextoAplicacion(root)
    ventana.mainloop()

if __name__ == "__main__":
    main()
