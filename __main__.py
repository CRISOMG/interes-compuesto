def run():
    inversion = 1000
    tiempo = 10
    interes_compuesto = 0.1

    retorno = inversion*(1+interes_compuesto)**tiempo

    print(
        f"""
\x1b[93m Inversión inicial: ${inversion} \x1b[0m

\x1b[96m Interes compuesto: %10 \x1b[0m

\x1b[93m Tiempo Total: {tiempo} años \x1b[0m

\x1b[32m Retorno: ${round(retorno,2)} \x1b[0m
        """
    )


if __name__ == "__main__":
    run()
