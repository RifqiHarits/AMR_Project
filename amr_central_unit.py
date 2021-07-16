import requests
import amr_elements
import time
from bs4 import BeautifulSoup
from tkinter import Label
from tkinter import Listbox
from tkinter import Tk
from tkinter import Button
from tkinter import END
from tkinter import font
import json
import threading
from multiprocessing import Process
from http.server import HTTPServer, BaseHTTPRequestHandler

# amr = amr_elements.AMRServerElement()

data = None
automate = False


def task_send(task_no):
    if task_no == 1:
        data = {
            "task_definition_id": 22,
            "goals": [{
                "index": 0,
                "waypoint_id": 43,
                "pickup": [],
                "delivery": []
            }],
            "priority": 100
        }
    elif task_no == 2:
        data = {
            "task_definition_id": 22,
            "goals": [{
                "index": 0,
                "waypoint_id": 43,
                "pickup": [],
                "delivery": []
            }],
            "priority": 100
        }
    elif task_no == 3:
        data = {
            "task_definition_id": 22,
            "goals": [{
                "index": 0,
                "waypoint_id": 43,
                "pickup": [],
                "delivery": []
            }],
            "priority": 100
        }
    elif task_no == 4:
        data = {
            "task_definition_id": 22,
            "goals": [{
                "index": 0,
                "waypoint_id": 43,
                "pickup": [],
                "delivery": []
            }],
            "priority": 100
        }
    elif task_no == 5:
        data = {
            "task_definition_id": 22,
            "goals": [{
                "index": 0,
                "waypoint_id": 43,
                "pickup": [],
                "delivery": []
            }],
            "priority": 100
        }
    if data is not None:
        print(task_no)
        print(data)
        # amr.create_task(data)


def do_task():
    if listbox.curselection() == ():
        return
    task = listbox.get(listbox.curselection())
    print(task + " sent")
    listbox.delete(listbox.curselection())
    task_no = ''.join(filter(str.isdigit, task))
    task_no = int(task_no)
    task_send(task_no)


def automate_task():
    global automate
    global listbox
    automate = not automate
    if automate:
        auto_button.config(bg="red")
    else:
        auto_button.config(bg="white")

    for i, items in enumerate(listbox.get(0, END)):
        task_no = ''.join(filter(str.isdigit, items))
        task_no = int(task_no)
        task_send(task_no)
        listbox.delete(0)


master = Tk()
master.title("AMR Central Unit")
master.iconbitmap("icon.ico")
master.geometry("300x400")
master.resizable(width=False, height=False)
master.config(bg="white")

list_font = font.Font(family="Tahoma", size=20)
button_font = font.Font(family="Tahoma", size=15)
listbox = Listbox(master, font=list_font)
listbox.pack(fill="both", expand=True)

# listbox.insert(END, "Task 1")
# listbox.insert(END, "Task 4")

button = Button(master, text="Send Task", command=do_task, font=button_font)
auto_button = Button(master, text="Automate", command=automate_task, font=button_font)
button.pack(side="left")
auto_button.pack(side="right")


# gui_thread = threading.Thread(target=master.mainloop)
# gui_thread.start()


# master.after(1000, get_task)


class echoHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()

        output = "<html><body>Testing</body></html>"
        self.wfile.write(output.encode())

    def do_POST(self):
        if self.path.endswith('/task'):
            data_string = self.rfile.read(int(self.headers['Content-Length']))
            task_no = json.loads(data_string)["task"]
            if task_no <= 5:
                if not automate:
                    listbox.insert(END, "Task " + str(task_no))
                else:
                    task_send(task_no)

        if task_no <= 5:
            self.send_response(201)
            self.send_header('content-type', 'text/html')
            self.end_headers()
        else:
            self.send_response(418)
            self.send_header('content-type', 'text/html')
            self.end_headers()


PORT = 9000
server_address = ('localhost', PORT)
server = HTTPServer(server_address, echoHandler)
print('Server running on port %s' % PORT)

close_app = False


def the_server():
    print("ok")
    server.serve_forever()
    print("ok")


server_thread = threading.Thread(target=the_server)
server_thread.daemon = True
server_thread.start()

server_process = Process(target=the_server)
server_process.daemon = True


def app_close():
    master.destroy()


master.protocol("WM_DELETE_WINDOW", app_close)
master.mainloop()
