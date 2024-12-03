import customtkinter as ck
import os
from PIL import Image, ImageTk
import tkinter as tk
from SessionManager import SessionManager
from text_editor import EditorTextoAplicacion
from music import MusicPlayer


def open_file(path):
    if os.path.splitext(path)[1] == '.txt':
        root = tk.Tk()
        text_editor = EditorTextoAplicacion(root)
        text_editor.abrir_archivo(path)
    elif os.path.splitext(path)[1] == '.mp3':
        root = tk.Tk()
        music_player = MusicPlayer(root)
        music_player.open_file_exp(path)
    else:
        print("Archivo no reconocido")


class Explorer(ck.CTk):
    def __init__(self):
        super().__init__()
        self.title("Explorer")
        self.geometry("800x600")
        self.resizable(False, False)

        self.session = SessionManager()

        title_label = ck.CTkLabel(self, text=f"Carpetas del Usuario", font=("Roboto", 20))
        title_label.pack(pady=10)

        home_image = ck.CTkImage(
            light_image=Image.open("images\\home.png"),
            dark_image=Image.open("images\\home.png"),
            size=(40, 40)
        )
        home_button = ck.CTkButton(
                    self,
                    text="",
                    image=home_image,
                    command=self.principal_route,
                    fg_color = "transparent",
                    hover = False,
        )
        home_button.pack(anchor="n", pady=10, padx=10)

        self.folders_frame = ck.CTkFrame(self, width=200, height=400, fg_color="transparent")
        self.folders_frame.pack(pady=20, padx=20, fill="both", expand=True)

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
            if os.path.isdir(folder_path):
                try:
                    icon_image = Image.open("images\\explorer.png")
                    icon_image = icon_image.resize((20, 20))
                    icon_image = ImageTk.PhotoImage(icon_image)
                except Exception as e:
                    print(f"Error al cargar la imagen del icono: {e}")
                    icon_image = None

                folder_label = ck.CTkButton(
                    self.folders_frame,
                    text=folder,
                    image=icon_image,
                    command=lambda p=folder_path: self.open_folder(p),
                    text_color="black",
                    fg_color = "transparent",
                    hover = False,
                )
                folder_label.image = icon_image
                folder_label.pack(anchor="w", padx=10, pady=5)
            elif os.path.isfile(folder_path):
                if os.path.splitext(folder_path)[1] == ".txt":
                    try:
                        icon_image = Image.open("images\\file.png")
                        icon_image = icon_image.resize((20, 20))
                        icon_image = ImageTk.PhotoImage(icon_image)
                    except Exception as e:
                        print(f"Error al cargar la imagen del icono: {e}")
                        icon_image = None
                    self.create_button(folder, icon_image, folder_path)
                elif os.path.splitext(folder_path)[1] == ".mp3":
                    try:
                        icon_image = Image.open("images\\music.png")
                        icon_image = icon_image.resize((20, 20))
                        icon_image = ImageTk.PhotoImage(icon_image)
                    except Exception as e:
                        print(f"Error al cargar la imagen del icono: {e}")
                        icon_image = None
                    self.create_button(folder, icon_image, folder_path)
                elif os.path.splitext(folder_path)[1] == ".png" or os.path.splitext(folder_path)[1] == ".jpg":
                    try:
                        icon_image = Image.open("images\\gallery.png")
                        icon_image = icon_image.resize((20, 20))
                        icon_image = ImageTk.PhotoImage(icon_image)
                    except Exception as e:
                        print(f"Error al cargar la imagen del icono: {e}")
                        icon_image = None
                    self.create_button(folder, icon_image, folder_path)
                elif os.path.splitext(folder_path)[1] == ".mp4":
                    try:
                        icon_image = Image.open("images\\video.png")
                        icon_image = icon_image.resize((20, 20))
                        icon_image = ImageTk.PhotoImage(icon_image)
                    except Exception as e:
                        print(f"Error al cargar la imagen del icono: {e}")
                        icon_image = None
                    self.create_button(folder, icon_image, folder_path)
                else:
                    ck.CTkLabel(self.folders_frame, compound="center", text="Archivo no reconocido").pack()
            else:
                ck.CTkLabel(self.folders_frame, compound="center", text="No hay archivos o carpetas en esta ruta").pack()

    def create_button(self, folder, img, path):
        folder_label = ck.CTkButton(
            self.folders_frame,
            text=folder,
            image=img,
            command=lambda p=path: open_file(p),
            text_color="black",
            fg_color="transparent",
            hover=False,
        )
        folder_label.image = img
        folder_label.pack(anchor="w", padx=10, pady=10)

    def open_folder(self, path):
        for widget in self.folders_frame.winfo_children():
            widget.destroy()
        if os.path.isdir(path):
            self.display_folders(path)
        else:
            print("No se puede abrir, no es una carpeta.")

    def validate_session(self):
        info = self.session.load_session()
        if isinstance(info, dict) and info:
            last_user, last_path = list(info.items())[-1]
            return last_user, last_path
        return "", ""

    def principal_route(self):
        _, route = self.validate_session()
        if route:
            for widget in self.folders_frame.winfo_children():
                widget.destroy()
            self.open_folder(route)

if __name__ == "__main__":
    app = Explorer()
    app.mainloop()
