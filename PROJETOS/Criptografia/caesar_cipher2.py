#Caesar Cipher
#https://nostarch.com/crackingcodes/

import pyperclip

#A mensagem a ser criptografada:
message = 'Esta é minha mensagem secreta'

#A chave de encriptação/decriptação:
key = 13

#Modo a selecionar:
mode = 'encrypt' #OPÇÕES: 'encrypt' ou 'decrypt'.

#Todos os possíveis símbolos que podem ser encriptados:
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvxwyz1234567890 !?@#/Ç.,;'

#Guarda a forma encriptada/decriptada da mensagem:
translated = ''

for symbol in message:
    #NOTA: Apenas símbolos na variável SYMBOLS são afetadas.
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)

        #Encripta / decripta:
        if mode == 'encrypt':
            translatedIndex = symbolIndex + key
        elif mode == 'decrypt':
            translatedIndex = symbolIndex - key
        #Lida com wraparound, se necessário:
        if translatedIndex >= len(SYMBOLS):
            translatedIndex = translatedIndex - len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(SYMBOLS)

        translated = translated + SYMBOLS[translatedIndex]
    else:
        #Acrescenta o símbolo sem encriptar/decriptar:
        translated = translated + symbol

#Output da string traduzida:
print(translated)
pyperclip.copy(translated)
