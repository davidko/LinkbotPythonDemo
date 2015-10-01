import string
import tempfile
import subprocess
import threading
import os

def run_template_file(template_filename, mapping, callback=None):
    with open(template_filename, 'r') as f:
        s = string.Template(f.read())
        exec_data = s.subsitute(mapping)
    with tempfile.NamedTemporaryFile(delete=False) as f:
        f.write(exec_data)
        filename = f.name
    subprocess.run(['python3', filename])
    if callback:
        callback()
    
def run_template_file_async(template_filename, mapping, callback):
    t = threading.Thread(target=run_template_file, 
                         args=(template_filename, mapping, callback) )
    t.start()

def run_string(python_string, callback=None):
    with tempfile.NamedTemporaryFile(delete=False) as f:
        f.write(python_string)
        tempfilename = f.name
    subprocess.call(['python3', tempfilename])
    os.remove(tempfilename)
    if callback:
        callback()

def run_string_async(*args, **kwargs):
    t = threading.Thread(target=run_string, args=args, kwargs=kwargs)
    t.start()

def translate_file(filename, mapping):
    # Translate a template file and return the string
    with open(filename, 'r') as f:
        s = string.Template(f.read())
        translated = s.substitute(mapping)
        return translated
