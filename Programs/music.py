import os
import random
import tkinter
import pygame
from PIL import Image, ImageTk
from tkinter import Tk, Button, Label, filedialog, PhotoImage, Frame, Image
from tkinter import ttk
from SessionManager import SessionManager
from config import IMAGES_PATH

images_path = IMAGES_PATH

class MusicPlayer(tkinter.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.root.title('Reproductor de Música')
        self.root.config(bg='black')
        self.root.geometry("430x400")
        self.root.resizable(False, False)

        self.session = SessionManager()

        # Inicializar pygame mixer
        pygame.mixer.init(frequency=44100)

        # Variables principales
        self.direction = []
        self.pos = 0
        self.update = None

        # Configurar styles
        self.configure_styles()

        # Crear interfaz
        self.create_interface()

    def configure_styles(self):
        style = ttk.Style()
        style.theme_use('clam')
        style.configure(
            "Vertical.TProgressbar",
            foreground='#1F509A', background='#1F509A', troughcolor='black',
            bordercolor='black', lightcolor='#1F509A', darkcolor='#1F509A'
        )
        style.configure(
            "Horizontal.TProgressbar",
            bordercolor='#D0E8C5', lightcolor='#D0E8C5', darkcolor='black'
        )

    def create_interface(self):
        # Frames
        self.frame_sticks = Frame(self.root, bg='black', width=600, height=350)
        self.frame_sticks.grid(column=0, row=0, sticky='nsew')
        self.frame_controls = Frame(self.root, bg='black', width=600, height=50)
        self.frame_controls.grid(column=0, row=1, sticky='nsew')

        # sticks de progreso
        self.sticks = [
            ttk.Progressbar(self.frame_sticks, orient='vertical', length=300, maximum=300,
                            style="Vertical.TProgressbar")
            for _ in range(20)
        ]
        for idx, stick in enumerate(self.sticks):
            stick.grid(column=idx, row=0, padx=1)

        # Controles y etiquetas
        self.quantity = Label(self.frame_controls, bg='black', fg='green2')
        self.quantity.grid(column=8, row=0)

        # Botones
        self.create_buttons()

        # Barra de time
        self.time = ttk.Progressbar(self.frame_controls, orient='horizontal', length=390,
                                      style="Horizontal.TProgressbar")
        self.time.grid(row=1, columnspan=8, padx=5)

    def create_buttons(self):
        buttons = [
            ("File", self.open_file),
            ("Play", self.start),
            ("Stop", self.stop),
            ("Prev", self.prev),
            ("Next", self.next),
        ]

        for idx, (name, command) in enumerate(buttons):
            button = Button(
                self.frame_controls,
                text=name,
                command=command)
            button.grid(column=idx, row=2, pady=10)

    def open_file(self):
        data = self.session.load_session()
        if data:
            last_user, last_path = list(data.items())[-1]
            self.direction = filedialog.askopenfilenames(
                initialdir=last_path, title='Escoger la canción(es)',
                filetypes=(('mp3 files', '*.mp3*'), ('All files', '*.*'))
            )
        self.pos = 0
        if self.direction:
            print(self.direction)
            self.update_song()

    def open_file_exp(self, path):
        if not path:
            return

        self.direction = (path,)
        self.pos = 0
        if self.direction:
            self.update_song()

    def start(self):
        if not self.direction:
            return
        pygame.mixer.music.load(self.direction[self.pos])
        pygame.mixer.music.play()
        self.reproduction_update()

    def update_song(self):
        self.quantity.config(text=f"{self.pos + 1}/{len(self.direction)}")

    def reproduction_update(self):
        # update sticks
        for stick in self.sticks:
            stick['value'] = random.randint(50, 300)

        # update time
        actual_time = pygame.mixer.music.get_pos() // 1000
        self.time['value'] = actual_time

        if actual_time >= self.time['maximum']:
            self.next()

        self.update = self.root.after(400, self.reproduction_update)

    def stop(self):
        pygame.mixer.music.stop()
        if self.update:
            self.root.after_cancel(self.update)

    def prev(self):
        if self.pos > 0:
            self.pos -= 1
            self.start()

    def next(self):
        if self.pos < len(self.direction) - 1:
            self.pos += 1
            self.start()

if __name__ == "__main__":
    root = Tk()
    player = MusicPlayer(root)
    root.mainloop()

