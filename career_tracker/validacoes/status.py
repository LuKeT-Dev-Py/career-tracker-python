def validar_status(status):
    permitidos = ('enviada', 'entrevista', 'recusada')
    if status in permitidos:
        return True
    else:
        return False
