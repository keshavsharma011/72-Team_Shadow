import subprocess
import re

def open_applications_from_paragraph(paragraph):
    def extract_applications(paragraph):
        app_name_pattern = re.compile(r'\b(?:notepad|chrome|firefox|calculator|code|whatsapp|word|excel|vlc|photos|linkedin|explorer|edge|power point|outlook)\b', re.IGNORECASE)
        return re.findall(app_name_pattern, paragraph)

    def open_application(app_name):
        try:
            subprocess.run(["start", app_name], shell=True)
            print(f"Opened {app_name} successfully.")
        except FileNotFoundError:
            print(f"{app_name} not found. Make sure the application is installed.")
        except Exception as e:
            print(f"An error occurred while opening {app_name}: {e}")

    extracted_applications = extract_applications(paragraph)

    for app_name in extracted_applications:
        open_application(app_name)


