import http.server
import socketserver

import keyboard

import threading

def http_server():
    PORT = 80

    handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print("Server started at localhost:" + str(PORT))
        httpd.serve_forever()

def keyboard_handler():
    try: # Set counter to 0 if there is no file
            f = open("web/counter.txt", "r")
    except Exception:
        f = open("web/counter.txt", "w+")
        f.write("0")
    f.close()

    while True:
        keyboard.wait("p")

        try:
            f = open("web/counter.txt", "r")
        except Exception:
            f = open("web/counter.txt", "w+")

        data = f.read()

        try:
            x = int(data)
        except Exception:
            x = 0

        y = x + 1

        f.close()

        f = open("web/counter.txt", "w")
        f.write(str(y))
        f.close()

        print("+1")


http_server_thread = threading.Thread(target=http_server)
http_server_thread.start()

keyboard_handler_thread = threading.Thread(target=keyboard_handler)
keyboard_handler_thread.start()