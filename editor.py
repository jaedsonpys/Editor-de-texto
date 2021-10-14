from tkinter import *
from tkinter import filedialog

import keyboard

file_local = False

def openfile():
    global file_local

    file_name = filedialog.askopenfilename()

    with open(file_name, 'r') as file:
        text.delete(1.0, END)
        text.insert(END, file.read())

    file_local = file_name


def savefile():
    if file_local is False:
        savefilewith()

    with open(file_local, 'w') as file_name:
        file_name.write(text.get(1.0, END))


def savefilewith():
    global file_local

    file_name = filedialog.asksaveasfile()

    if file_name is not None:
        file_name.write(text.get(1.0, END))

        file_local = file_name.name
        file_name.close()

# def message(msg):
#     top = Toplevel(root)

#     top.title('Mensagem')
#     top.geometry('200x200')
#     top.resizable(False, False)

#     Label(top, text=msg).pack(pady=20, padx=20,)

root = Tk()

menu_bar = Menu(root)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='Abrir arquivo', command=openfile)
file_menu.add_command(label='Salvar arquivo', command=savefile)
file_menu.add_command(label='Salvar como...', command=savefilewith)

menu_bar.add_cascade(label='Arquivo', menu=file_menu)

root.config(menu=menu_bar)

text_frame = LabelFrame(root)
text_frame.pack(fill=BOTH, expand=True, pady=10, padx=10)

text = Text(text_frame, tabs='4')
text.pack(expand=True, fill=BOTH)

keyboard.add_hotkey('ctrl+s', savefile)

root.title('Editor de Texto')
root.geometry('600x600')
root.mainloop()
