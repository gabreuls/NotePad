import tkinter as tk
import keyboard

def apenas_alfabeto(event):
    teclas_permitidas = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ012346789 \n\r"

    if event.char in teclas_permitidas or event.keysym == 'BackSpace':
        return
    else:
        return "break"

def criar_bloco_notas():
    root = tk.Tk()
    root.title("Gigi e Cardihno")

    texto = tk.Text(root, wrap="word", font = ("Arial", 30))
    texto.pack(expand = True, fill = "both")

    texto.bind("<KeyPress>", apenas_alfabeto)

    root.mainloop()

if __name__ == "__main__":
    criar_bloco_notas()

