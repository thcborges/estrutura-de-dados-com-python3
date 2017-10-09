from tkinter import *


def click_button():
    print(entry_text.get())


# cria uma nova janela
window = Tk()

# seta o título da janela
window.title('Meu programa')

entry_text = Entry(window, width=30)
entry_text.pack()
entry_text.focus_set()

btn = Button(window, text='Clique aqui', width=20, command=click_button)
btn.pack()

window.geometry('300x150')

window.mainloop()
