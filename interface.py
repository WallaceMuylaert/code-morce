import tkinter as tk
from tkinter import messagebox, scrolledtext, ttk
import winsound
import json
import os
import time

CAMINHO_JSON = 'data/json/morse-code.json'

FREQUENCIA = 750
DURACAO_PONTO = 100
DURACAO_TRACO = DURACAO_PONTO * 3
PAUSA_SINAL = 0.1
PAUSA_LETRA = 0.3
PAUSA_PALAVRA = 0.7

if os.path.exists(CAMINHO_JSON):
    with open(CAMINHO_JSON, 'r', encoding='utf-8') as f:
        morse_dict = json.load(f)
else:
    messagebox.showerror("Erro", f"Arquivo não encontrado: {CAMINHO_JSON}")
    exit()

reverse_dict = {v: k for k, v in morse_dict.items()}

def texto_para_morse(texto):
    texto = texto.lower()
    morse = []
    for char in texto:
        if char == ' ':
            morse.append('/')
        elif char in morse_dict:
            morse.append(morse_dict[char])
        else:
            morse.append('?')
    return ' '.join(morse)

def morse_para_texto(morse):
    palavras = morse.strip().split(' / ')
    texto_final = []
    for palavra in palavras:
        letras = palavra.split()
        texto = ''.join(reverse_dict.get(letra, '?') for letra in letras)
        texto_final.append(texto)
    return ' '.join(texto_final)

def tocar_som_morse(morse):
    for simbolo in morse:
        if simbolo == '.':
            winsound.Beep(FREQUENCIA, DURACAO_PONTO)
            time.sleep(PAUSA_SINAL)
        elif simbolo == '-':
            winsound.Beep(FREQUENCIA, DURACAO_TRACO)
            time.sleep(PAUSA_SINAL)
        elif simbolo == ' ':
            time.sleep(PAUSA_LETRA)
        elif simbolo == '/':
            time.sleep(PAUSA_PALAVRA)

def converter_para_morse():
    texto = entrada_texto.get("1.0", tk.END).strip()
    morse = texto_para_morse(texto)
    entrada_morse.delete("1.0", tk.END)
    entrada_morse.insert(tk.END, morse)

def converter_para_texto():
    morse = entrada_morse.get("1.0", tk.END).strip()
    texto = morse_para_texto(morse)
    entrada_texto.delete("1.0", tk.END)
    entrada_texto.insert(tk.END, texto)

def tocar_morse():
    morse = entrada_morse.get("1.0", tk.END).strip()
    tocar_som_morse(morse)

def limpar():
    entrada_texto.delete("1.0", tk.END)
    entrada_morse.delete("1.0", tk.END)

# Criação da Janela
janela = tk.Tk()
janela.title("Conversor de Código Morse")
janela.geometry("700x520")
janela.configure(bg="#eaeaea")  # Fundo mais suave

fonte_titulo = ("Segoe UI", 18, "bold")
fonte_label = ("Segoe UI", 12)
fonte_botao = ("Segoe UI", 11)

# Título
titulo = tk.Label(janela, text="🔤 Conversor de Texto ↔ Código Morse", font=fonte_titulo, bg="#eaeaea", fg="#222")
titulo.pack(pady=(15, 10))

# Entrada de texto
frame_texto = tk.Frame(janela, bg="#eaeaea")
frame_texto.pack(fill="x", padx=20, pady=5)

label_texto = tk.Label(frame_texto, text="Digite o texto:", font=fonte_label, bg="#eaeaea")
label_texto.pack(anchor="w")
entrada_texto = scrolledtext.ScrolledText(frame_texto, height=5, font=("Consolas", 12), wrap="word", relief="solid", bd=1)
entrada_texto.pack(fill="x")

# Entrada de código Morse
frame_morse = tk.Frame(janela, bg="#eaeaea")
frame_morse.pack(fill="x", padx=20, pady=5)

label_morse = tk.Label(frame_morse, text="Código Morse:", font=fonte_label, bg="#eaeaea")
label_morse.pack(anchor="w")
entrada_morse = scrolledtext.ScrolledText(frame_morse, height=5, font=("Consolas", 12), wrap="word", relief="solid", bd=1)
entrada_morse.pack(fill="x")

# Botões
frame_botoes = tk.Frame(janela, bg="#eaeaea")
frame_botoes.pack(pady=20)

estilo = ttk.Style()
estilo.theme_use("clam")  # Tema moderno
estilo.configure("TButton", font=fonte_botao, padding=6)
estilo.map("TButton", background=[("active", "#ddd")])

botoes = [
    ("Texto → Morse", converter_para_morse, "#4caf50"),
    ("Morse → Texto", converter_para_texto, "#2196f3"),
    ("Tocar Morse", tocar_morse, "#ff9800"),
    ("Limpar", limpar, "#757575")
]

for texto, comando, cor in botoes:
    btn = tk.Button(frame_botoes, text=texto, command=comando, font=fonte_botao,
                    bg=cor, fg="white", activebackground="#333", width=15)
    btn.pack(side="left", padx=8)

# Rodapé
rodape = tk.Label(janela, text="Wallace Barbosa • Código Morse em Python", font=("Segoe UI", 9), bg="#eaeaea", fg="#555")
rodape.pack(side="bottom", pady=10)

janela.mainloop()
