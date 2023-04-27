def saludo():
    print( "Hola" )

def mensajeBienvenida( nombrePersona: str, apellidoPersona: int, correosNoLeidos: int ) -> str:
    return f"Bienvenid(@) { nombrePersona } { apellidoPersona }, Tienes: { correosNoLeidos } nuevos correos sin leer!"

def suma( numeroUno = 0, numeroDos = 0 ) -> int:
    return numeroUno + numeroDos

def listarNombres( *nombres ): # Pueden venir varios nombres, los parametros se transformanen una tupla
    for nombre in nombres:
        print( nombre )

def sumarColeccionNumeros( *numeros ) -> str:
    sumatoria: int = 0
    for numero in numeros:
        sumatoria = sumatoria + int( numero )
    return f'La sumatoria de los numeros { numeros } es: { sumatoria }'

def multiplicaColeccionNumeros( *numeros ) -> str:
    multiplicacion: int = 1
    for numero in numeros:
            multiplicacion = multiplicacion * numero
    return f'La Multiplicacion de los numeros { numeros } es: { multiplicacion }'

