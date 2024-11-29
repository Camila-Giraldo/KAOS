import os
import subprocess
import customtkinter as ctk


class Programs:
    def __init__(self, programs_path):
        self.programs_path = programs_path
        self.processes = {}

    def _launch_program(self, program_name):
        path = os.path.join(self.programs_path, f"{program_name}.py")
        if os.path.isfile(path):
            try:
                process = subprocess.Popen(["python", path])
                self.processes[program_name] = process
            except Exception as e:
                print(f"Error al iniciar {program_name}: {e}")

    def list_active_processes(self):
        """Devuelve un diccionario de procesos activos y su estado."""
        return {
            name: "Active" if process.poll() is None else "Finished"
            for name, process in self.processes.items()
        }

    def terminate_program(self, program_name):
        process = self.processes.get(program_name)
        if process and process.poll() is None:
            process.terminate()
            return f"{program_name.capitalize()} Finished."
        else:
            return f"{program_name.capitalize()} no está activo o ya ha finalizado."

    def terminate_all(self):
        for name, process in self.processes.items():
            if process.poll() is None:
                process.terminate()

    def calculator(self):
        self._launch_program("calculator")

    def explorer(self):
        self._launch_program("explorer")

    def text_editor(self):
        self._launch_program("text_editor")

    def videogame(self):
        self._launch_program("videogame")

    def videos(self):
        self._launch_program("video")

    def gallery(self):
        self._launch_program("gallery")

    def music(self):
        self._launch_program("music")

    def chrome(self):
        self._launch_program("chrome")


class TaskManagerGUI(ctk.CTk):
    def __init__(self, programs):
        super().__init__()
        self.programs = programs
        self.title("Administrador de Tareas")
        self.geometry("400x400")

        # Crear widgets
        self.label_title = ctk.CTkLabel(
            self, text="Administrador de Tareas", font=("Arial", 16)
        )
        self.label_title.pack(pady=10)

        self.process_listbox = ctk.CTkTextbox(self, width=300, height=200)
        self.process_listbox.pack(pady=10)

        self.button_refresh = ctk.CTkButton(
            self, text="Actualizar", command=self.refresh_processes
        )
        self.button_refresh.pack(pady=5)

        self.refresh_processes()  # Inicializar la lista de procesos al iniciar la GUI

    def refresh_processes(self):
        """Actualiza la lista de procesos en el Textbox."""
        self.process_listbox.delete("1.0", "end")  # Limpiar el contenido del Textbox
        processes = (
            self.programs.list_active_processes()
        )  # Obtener los procesos activos
        for name, status in processes.items():
            self.process_listbox.insert(
                "end", f"{name.capitalize()}: {status}\n"
            )
