import customtkinter as ck
import os
from PIL import Image, ImageTk
import tkinter as tk
from SessionManager import SessionManager
from text_editor import EditorTextoAplicacion

images_path = os.path.join(os.path.dirname(__file__), "images")

class Explorer(ck.CTk):
    def __init__(self):
        super().__init__()
        self.title("Explorer")
        self.geometry("800x600")
        self.resizable(False, False)

        self.session = SessionManager()

        self.folders_frame = ck.CTkFrame(self, width=200, height=400)
        self.folders_frame.pack(pady=20, padx=20, fill="both", expand=True)

        title_label = ck.CTkLabel(self.folders_frame, text="Carpetas del usuario")
        title_label.pack(pady=10)
        self.display_folders()

    def display_folders(self, path=None):
        # Limpiar el frame antes de mostrar las carpetas
        for widget in self.folders_frame.winfo_children():
            if (
                isinstance(widget, ck.CTkLabel)
                and widget.cget("text") != "Carpetas del usuario"
            ):
                widget.destroy()

        if path is None:
            _, path = self.validate_session()

        folders = os.listdir(path)
        for folder in folders:
            folder_path = os.path.join(path, folder)
            if os.path.isdir(folder_path):  # Verifica que sea una carpeta
                # Cargar la imagen del icono de carpeta
                try:
                    icon_image = Image.open("images\\explorer.png")
                    icon_image = icon_image.resize((20, 20))  # Ajustar tamaño del icono
                    icon_image = ImageTk.PhotoImage(icon_image)
                except Exception as e:
                    print(f"Error al cargar la imagen del icono: {e}")
                    icon_image = None

                # Crear el Label con imagen y texto

                folder_label = ck.CTkButton(
                    self.folders_frame,
                    text=folder,
                    image=icon_image,
                    command=lambda p=folder_path: self.open_folder(p),
                    text_color="black",
                    fg_color = "transparent",
                    hover = False,
                )
                folder_label.image = icon_image  # Prevenir que se elimine la referencia
                folder_label.pack(anchor="w", padx=10, pady=5)
            elif os.path.isfile(folder_path):
                try:
                    icon_image = Image.open("images\\file.png")
                    icon_image = icon_image.resize((20, 20))  # Ajustar tamaño del icono
                    icon_image = ImageTk.PhotoImage(icon_image)
                except Exception as e:
                    print(f"Error al cargar la imagen del icono: {e}")
                    icon_image = None

                # Crear el Label con imagen y texto
                folder_label = ck.CTkButton(
                    self.folders_frame,
                    text=folder,
                    image=icon_image,
                    command=lambda p=folder_path: self.open_file(p),
                    text_color="black",
                    fg_color="transparent",
                    hover=False,
                )
                folder_label.image = icon_image
                folder_label.pack(anchor="w", padx=10, pady=10)

    def open_folder(self, path):
        if os.path.isdir(path):  # Verificar que sea un directorio
            self.display_folders(path)
        else:
            print("No se puede abrir, no es una carpeta.")

    def open_file(self, path):
        root = tk.Tk()
        root.title('Editor de texto')
        root.geometry('480x400')
        text_editor = EditorTextoAplicacion(root)
        text_editor.abrir_archivo(path)

    def validate_session(self):
        info = self.session.load_session()
        if isinstance(info, dict) and info:
            last_user, last_path = list(info.items())[-1]
            return last_user, last_path
        return "", ""

if __name__ == "__main__":
    app = Explorer()
    app.mainloop()
