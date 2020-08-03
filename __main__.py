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
