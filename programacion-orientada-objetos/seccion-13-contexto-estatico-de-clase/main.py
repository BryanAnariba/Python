from classes.MiClase import MyClase

def main():
    print( f' Variable de la clase MyClase sin Instanciar: { MyClase.variableClase }' )
    clase = MyClase( 'Hola' )
    clase.metodoClase()
    clase.metodoInstanciasMetodoNormalDeClase()

    
main()