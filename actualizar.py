import subprocess
subprocess.call(['clear'],shell=True)
subprocess.call(['rm -rf Tool_Kit && git clone https://github.com/jm-12345/Tool_Kit.git'],shell=True)
subprocess.call(['rm actualizar.py'],shell=True)
print("""
  
Actualizado con exito""")
time.sleep(2)
subprocess.call(['cd Tool_Kit && python Tool_Kit.py'],shell=True)
