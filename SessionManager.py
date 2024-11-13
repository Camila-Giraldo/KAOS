class SessionManager:
    current_user = None  # Variable de clase para almacenar el usuario actual
    users_path = ""
    users_list = []

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
