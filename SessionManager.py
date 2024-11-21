import os
import json

session_user = os.path.join(os.path.dirname(__file__), "session_user.json")

class SessionManager:
    current_user = None  # Variable de clase para almacenar el usuario actual
    users_path = ""

    @classmethod
    def set_user(cls, username):
        """Establece el usuario actual que ha iniciado sesión."""
        cls.current_user = username

    @classmethod
    def get_user(cls):
        """Devuelve el nombre del usuario que ha iniciado sesión."""
        return cls.current_user

    @classmethod
    def set_users_path(cls, path):
        cls.users_path = path

    @classmethod
    def get_path(cls):
        return cls.users_path

    @classmethod
    def save_session(cls, session):
        """Save users to JSON file."""
        with open(session_user, "w") as f:
            json.dump(session, f, indent=4)

    @classmethod
    def load_session(cls):
        """Load users from JSON file."""
        if os.path.exists(session_user):
            with open(session_user, "r") as f:
                return json.load(f)
        return {}

    @classmethod
    def save_info(cls):
        session = {cls.get_user(): cls.get_path()}
        cls.save_session(session)

