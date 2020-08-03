print("""
Bienvenid@ a nuestra calculadora de Interes Compuesto.

 Este codigo te permite calcular el interes compuesto producido por una capital inicial en un periodo de tiempo especifico;
este puede bien ser meses, dias o inclusive años.

 Recuerda que el interes compuesto hace que el valor que se paga por concepto de intereses se incremente mes a mes,
puesto que la base para el cálculo del interés se incrementa cada vez que se liquidan los respectivos intereses. 
 
 
 """)


def calc(inversion, interes, tiempo):
    # Formula para calcular interes compuesto
    # M = C * (1 + i)**​n

    # M es la suma de capital más intereses al final del período.
    # C es el capital inicial.
    # i es la tasa de interés compuesto.
    # n es el número de períodos durante los cuales se capitaliza el interés compuesto.

    C = inversion
    I = interes
    N = tiempo

    M = C * (1+I)**N

    return int(M)


def run():
    inversion = int(input("Capital inicial: $"))
    interes = float("0." + input("Porcentaje de interes: 0."))
    tiempo = int(input("Numero de Periodos: "))

    retorno = calc(inversion, interes, tiempo)
    print(f"\x1b[32m retorno: ${retorno} \x1b[0m")


if __name__ == "__main__":
    run()
