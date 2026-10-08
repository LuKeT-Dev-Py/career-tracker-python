def validar_status(status):
    permitidos = ('enviada', 'entrevista', 'recusada') 
    if status in permitidos:
        return True
    else:
        try:
            return False
        except ValueError:
            return print('Digite um valor inteiro valido.')
    
def normalizar_status(texto):
    return texto.strip().lower()