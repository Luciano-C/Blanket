def caps_function():
    import pandas as pd
    from _00_cards import Card, get_rarities

    cartas = pd.read_csv("02_cartas_sppd.csv", encoding="UTF-8")
    niveles_tvt = pd.read_csv("02_levels_tvt.txt", encoding="UTF-8")

    cartas_tvt = []
    caps_needed = []

    tvt_rarities = get_rarities(cartas, niveles_tvt)

    # Crea una lista de cartas utilizando la clase "Card", con esto se determinan las caps requeridas
    for iteracion in range(0, 12):
        carta_tvt = Card(niveles_tvt.loc[iteracion, "Name"], tvt_rarities[iteracion],
                         niveles_tvt.loc[iteracion, "Level"])
        cartas_tvt.append(carta_tvt)
        caps_needed.append(cartas_tvt[iteracion].caps_required())

    # Añade columna "Caps" al data frame y la fila de totales
    niveles_tvt["Caps"] = caps_needed
    total_caps_needed = sum(caps_needed)
    Totales = ["TOTAL", "-", total_caps_needed]

    niveles_tvt.loc[len(niveles_tvt)] = Totales

    nombre2 = []
    mmr2 = []

    # Arregla formato de columnas nombre y MMR
    for nombre in range(0, len(niveles_tvt)):
        nombre2.append(niveles_tvt.loc[nombre, "Name"].ljust(24, " "))

    # Borra y reemplaza las columnas antiguas por las nuevas
    del (niveles_tvt["Name"])
    niveles_tvt.insert(0, "Name", nombre2)


    # Genera reporte
    report = open("report_required_caps.txt", "w", encoding="UTF-8")
    encabezados = niveles_tvt.head(len(niveles_tvt))  # Asigna el encabezado y los N primeros valores
    report.write(
        encabezados.to_string(index=False, justify="center"))  # index = False imprime la matriz sin los índices
    report.write("\n" + "\n")
    report.write(f"Caps needed: {total_caps_needed}" + "\n")


    return total_caps_needed


