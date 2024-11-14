import customtkinter as ck
from PIL import Image
import os
import json
from hashlib import sha256
from SessionManager import SessionManager


images_path = os.path.join(os.path.dirname(__file__), "images")
users_file = os.path.join(os.path.dirname(__file__), "users.json")
users_path = os.path.join(os.path.dirname(__file__), "Users")
session = SessionManager()

class LoginFrame(ck.CTkFrame):
    def __init__(self, master, switch_frame_callback):
        super().__init__(master)
        self.switch_frame_callback = switch_frame_callback
        self.pack(fill="both", expand=True)

        # Logo and user image
        logo = ck.CTkImage(
            light_image=Image.open(os.path.join(images_path, "Kaos.png")),
            dark_image=Image.open(os.path.join(images_path, "Kaos.png")),
            size=(420, 280),
        )
        img_user = ck.CTkImage(
            light_image=Image.open(os.path.join(images_path, "user.png")),
            dark_image=Image.open(os.path.join(images_path, "user.png")),
            size=(180, 180),
        )
        ck.CTkLabel(self, image=logo, text="").pack()
        ck.CTkLabel(self, image=img_user, text="").pack()

        # Login part
        ck.CTkLabel(self, text="User").pack()
        self.user_entry = self.create_entry("Username")
        self.user_entry.pack()

        ck.CTkLabel(self, text="Password").pack()
        self.password_entry = self.create_entry("*******", is_password=True)
        self.password_entry.pack()

        # Buttons
        ck.CTkButton(self, text="Sign in", command=self.validate_login).pack(pady=10)
        ck.CTkButton(self, text="Register", command=self.register_user).pack(pady=5)

        ck.CTkButton(
            self,
            image=ck.CTkImage(
                Image.open(os.path.join(images_path, "power-button.png")), size=(30, 30)
            ),
            text="",
            fg_color="transparent",
            hover=False,
            command=master.quit,
        ).pack(side="right")

    def create_entry(self, placeholder, is_password=False):
        entry = ck.CTkEntry(self, show="*" if is_password else "")
        entry.insert(0, placeholder)
        entry.bind(
            "<FocusIn>",
            lambda e: entry.delete(0, "end") if entry.get() == placeholder else None,
        )
        entry.bind(
            "<FocusOut>",
            lambda e: entry.insert(0, placeholder) if not entry.get() else None,
        )
        return entry

    def hash_password(self, password):
        """Hash the password for secure storage."""
        return sha256(password.encode()).hexdigest()

    def load_users(self):
        """Load users from JSON file."""
        if os.path.exists(users_file):
            with open(users_file, "r") as f:
                return json.load(f)
        return {}

    def save_users(self, users):
        """Save users to JSON file."""
        with open(users_file, "w") as f:
            json.dump(users, f, indent=4)

    def validate_login(self):
        """Validate user credentials for login."""
        username = self.user_entry.get()
        password = self.hash_password(self.password_entry.get())
        users = self.load_users()

        if username in users and users[username] == password:
            session.set_user(username)
            path = os.path.join(users_path, username)
            session.set_users_path(path)
            session.save_info()
            ck.CTkLabel(self, text="Login successful", text_color="green").pack()
            self.switch_frame_callback("desktop")
        else:
            ck.CTkLabel(
                self, text="User or password incorrect", text_color="red"
            ).pack()

    def register_user(self):
        """Register a new user and save it to JSON file."""
        username = self.user_entry.get()
        password = self.hash_password(self.password_entry.get())
        users = self.load_users()

        if username in users:
            ck.CTkLabel(self, text="User already exists", text_color="orange").pack()
        else:
            users[username] = password
            self.save_users(users)
            path = os.path.join(users_path, username)
            os.makedirs(path, exist_ok=True)
            self.create_principal_folders(path)
            ck.CTkLabel(
                self, text="User registered successfully", text_color="green"
            ).pack()

    def create_principal_folders(self, path):
        base_folders = [
            "Descargas",
            "Documentos",
            "Música",
            "Imágenes",
            "Escritorio",
            "Videos",
        ]

        for folder in base_folders:
            route = os.path.join(path, folder)
            os.makedirs(route, exist_ok=True)