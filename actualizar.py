import shlex, subprocess
subprocess.call(['rm -rf Tool_Kit'],shell=True)
subprocess.call(['git clone https://github.com/jm-12345/Tool_Kit.git'],shell=True)
subprocess.call(['rm actualizar.py'],shell=True)
