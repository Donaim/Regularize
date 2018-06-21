import subprocess
import os
import tempfile
import time
import threading


def create_temp() -> str:
    fname = tempfile.mktemp()
    fname += '.py'
    f = open(fname, 'w+') # just create it
    f.close()
    return fname
def open_file(editor: str, fname: str):
    return subprocess.Popen([editor, fname])

def listen_file(filename: str, check, callback):
    def st(): listen_file_sync(filename, check, callback)
    threading.Thread(target=st).start()

def listen_file_sync(filename: str, check, callback):
    update_time = os.path.getmtime(filename)

    while check():
        time.sleep(0.01)

        new_uptime = os.path.getmtime(filename)
        if new_uptime > update_time:
            update_time = new_uptime
            callback()

