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
            name: "Activo" if process.poll() is None else "Finalizado"
            for name, process in self.processes.items()
        }

    def terminate_program(self, program_name):
        process = self.processes.get(program_name)
        if process and process.poll() is None:
            process.terminate()
            return f"{program_name.capitalize()} terminado."
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

        self.button_terminate_selected = ctk.CTkButton(
            self, text="Terminar Seleccionado", command=self.terminate_selected_process
        )
        self.button_terminate_selected.pack(pady=5)

        self.button_terminate_all = ctk.CTkButton(
            self, text="Terminar Todos", command=self.terminate_all_processes
        )
        self.button_terminate_all.pack(pady=5)

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
            )  # Insertar el estado en el Textbox

    def terminate_selected_process(self):
        """Termina el proceso seleccionado en el Textbox."""
        try:
            selected_text = (
                self.process_listbox.get("sel.first", "sel.last")
                .strip()
                .split(":")[0]
                .lower()
            )  # Obtener el nombre del proceso seleccionado
            message = self.programs.terminate_program(
                selected_text
            )  # Terminar el proceso
            ctk.CTkMessagebox.showinfo("Info", message)  # Mostrar mensaje
            self.refresh_processes()  # Refrescar la lista de procesos
        except (
            ctk.CTkTextbox.SelectionError
        ):  # Manejo de excepción si no hay texto seleccionado
            ctk.CTkMessagebox.showwarning(
                "Advertencia", "Selecciona un proceso para terminar."
            )

    def terminate_all_processes(self):
        """Termina todos los procesos activos."""
        message = self.programs.terminate_all()
        ctk.CTkMessagebox.showinfo("Info", message)  # Mostrar mensaje
        self.refresh_processes()  # Refrescar la lista de procesos
