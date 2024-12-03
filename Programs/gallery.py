import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from SessionManager import SessionManager

class ImageViewerApp(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.root.title("Visor de Imágenes")
        self.root.geometry("800x600")
        self.root.resizable(False, False)

        self.session = SessionManager()

        # Botón para cargar imagen
        self.load_button = tk.Button(root, text="Cargar Imagen", command=self.load_image)
        self.load_button.pack(pady=10)

        # Etiqueta para mostrar la imagen
        self.image_label = tk.Label(root)
        self.image_label.pack(pady=20)

    def load_image(self):
        data = self.session.load_session()
        file_path = ""
        if data:
            last_user, last_path = list(data.items())[-1]
            file_path = filedialog.askopenfilename(
                initialdir=last_path,
                title="Seleccionar una imagen",
                filetypes=[("Imagenes", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")]
            )

        if file_path:
            # Cargar la imagen usando Pillow
            image = Image.open(file_path)

            # Redimensionar la imagen si es muy grande
            image = image.resize((700, 500), Image.Resampling.LANCZOS)

            # Convertir la imagen para mostrarla en el label
            self.photo = ImageTk.PhotoImage(image)

            # Mostrar la imagen en el label
            self.image_label.config(image=self.photo)
            self.image_label.image = self.photo  # Mantener la referencia para evitar que se elimine

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageViewerApp(root)
    root.mainloop()