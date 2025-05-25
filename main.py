import winsound
import time
import json

# Frequências e tempos para som
FREQUENCIA = 750
DURACAO_PONTO = 100
DURACAO_TRACO = DURACAO_PONTO * 3
PAUSA_SINAL = 0.1
PAUSA_LETRA = 0.3
PAUSA_PALAVRA = 0.7

# Carregar dicionário do arquivo JSON
def carregar_dicionario_morse(caminho_json):
    with open(caminho_json, 'r', encoding='utf-8') as f:
        morse_dict = json.load(f)
    reverse_dict = {v: k for k, v in morse_dict.items()}
    return morse_dict, reverse_dict

# Converter texto para morse
def texto_para_morse(texto, morse_dict):
    texto = texto.lower()
    morse = []
    for char in texto:
        if char == ' ':
            morse.append('/')  # espaço vira barra
        elif char in morse_dict:
            morse.append(morse_dict[char])
        else:
            morse.append('?')  # caractere desconhecido
    return ' '.join(morse)

# Converter morse para texto
def morse_para_texto(morse, reverse_dict):
    palavras = morse.strip().split(' / ')
    texto_final = []
    for palavra in palavras:
        letras = palavra.split()
        texto = ''.join(reverse_dict.get(letra, '?') for letra in letras)
        texto_final.append(texto)
    return ' '.join(texto_final)

# Emitir som do morse
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

# Programa principal
if __name__ == "__main__":
    caminho_arquivo = 'data/json/morse-code.json'
    morse_dict, reverse_dict = carregar_dicionario_morse(caminho_arquivo)

    while True:
        try:
            texto = input("Digite uma mensagem para converter em Morse: ")
            morse = texto_para_morse(texto, morse_dict)
            print("\nTexto para Morse:\n", morse)

            print("\nTocando Morse:")
            tocar_som_morse(morse)

            print("\nConvertido de volta para texto:")
            print(morse_para_texto(morse, reverse_dict))

        except KeyboardInterrupt:
            print("\nInterrompido pelo usuário. Saindo do programa.")
            break
