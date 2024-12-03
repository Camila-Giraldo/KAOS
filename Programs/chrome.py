import webbrowser
import os


def find_file_from_root(file_name, start_path=None):
    start_path = start_path or os.path.abspath(os.sep)

    for root, dirs, files in os.walk(start_path):
        if file_name in files:
            return os.path.join(root, file_name)
    return None

chrome_file = "chrome.exe"

chrome_path = find_file_from_root(chrome_file, start_path="C:\\")
if chrome_path:
    webbrowser.get(f'"{chrome_path}" %s').open("https://www.google.com")
else:
    print("No se encontró Google Chrome.")
