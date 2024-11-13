import customtkinter as ck
import os
from SessionManager import SessionManager

images_path = os.path.join(os.path.dirname(__file__), "images")

class Explorer(ck.CTk):
    def __init__(self):
        super().__init__()
        self.title("Explorer")
        self.geometry("800x600")
        self.resizable(False, False)

        self.username = SessionManager.get_user()
        self.users_path = SessionManager.get_path()

        self.user_path = os.path.join(self.users_path, f"{self.username}")

        self.folders_frame = ck.CTkFrame(self, width=200, height=400)
        self.folders_frame.pack(pady=20, padx=20, fill="both", expand=True)

        title_label = ck.CTkLabel(self.folders_frame, text="Carpetas del usuario")
        title_label.pack(pady=10)
        self.display_folders()

    def display_folders(self):
        # Limpiar el frame antes de mostrar las carpetas
        for widget in self.folders_frame.winfo_children():
            if (
                isinstance(widget, ck.CTkLabel)
                and widget.cget("text") != "Carpetas del usuario"
            ):
                widget.destroy()

        # Obtener las carpetas del usuario y mostrarlas en etiquetas
        folders = os.listdir(self.user_path)
        for folder in folders:
            folder_path = os.path.join(self.user_path, folder)
            if os.path.isdir(folder_path):  # Verifica que sea una carpeta
                folder_label = ck.CTkLabel(self.folders_frame, text=folder)
                folder_label.pack(anchor="w", padx=10, pady=5)


if __name__ == "__main__":
    app = Explorer()
    app.mainloop()
