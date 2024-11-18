import re
import unicodedata

def remover_acentos(texto):
    # Normaliza o texto para decompor caracteres acentuados
    nfkd = unicodedata.normalize('NFKD', texto)
    return nfkd

# Lê o arquivo e remove caracteres indesejados, letras maiúsculas e acentos
with open('legenda.txt', 'r', encoding='utf-8') as arquivo:
    linhas = arquivo.readlines()
    linhas_modificadas = [
        remover_acentos(re.sub(r"[\n,\'\"]", '', linha.strip()).lower()) for linha in linhas
    ]

# Reescreve o arquivo com as linhas modificadas
with open('legenda.txt', 'w', encoding='utf-8') as arquivo:
    for linha in linhas_modificadas:
        arquivo.write(linha+" ")

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

