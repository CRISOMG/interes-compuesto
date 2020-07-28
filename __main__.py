def run():
    inversion = 1000
    tiempo = range(1, 121)

    crecimiento = inversion
    for mes in tiempo:
        crecimiento = crecimiento + int(crecimiento * 0.1)
        print(
            f"\x1b[33m mes {mes} \x1b[0m / \x1b[32m ganancias: ${crecimiento} \x1b[0m")

    print(
        f"""
\x1b[93m Inversión inicial: $1000 \x1b[0m

\x1b[96m Interes compuesto: %10 \x1b[0m

\x1b[93m Tiempo: {int(len(tiempo) / 12)} años \x1b[0m

\x1b[32m Retorno: ${crecimiento} \x1b[0m
        """
    )


if __name__ == "__main__":
    run()
