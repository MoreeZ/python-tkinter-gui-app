import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()

apps = []

if os.path.isfile('save.txt'):
    with open("save.txt", "r") as f:
        tempApps = f.read()
        tempApps = tempApps.split(",")
        apps = tempApps
        apps = [x for x in tempApps if x.strip()]


def addApp():

    for wiget in frame.winfo_children():
        wiget.destroy()

    fileName = filedialog.askopenfilename(
        initialdir="/", title="Select File", filetypes=(("executables", "*.exe"), ("all files", "*.*")))
    apps.append(fileName)
    print(fileName)

    for app in apps:
        label = tk.Label(frame, text=app, bg="grey")
        label.pack()


def runApps():
    for app in apps:
        os.startfile(app)


canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, rely=0.1, relx=0.1)

openFile = tk.Button(root, text="Open File", padx=10,
                     pady=5, fg="white", bg="#263D42", command=addApp)

openFile.pack()

runApps = tk.Button(root, text="Run Apps", padx=10,
                    pady=5, fg="white", bg="#263D42", command=runApps)

runApps.pack()


for app in apps:
    label = tk.Label(frame, text=app, bg="grey")
    label.pack()


root.mainloop()

with open('save.txt', "w") as f:
    for app in apps:
        f.write(app + ",")
