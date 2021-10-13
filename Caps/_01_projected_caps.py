def ranks_function():
    import pandas as pd
    from _000_caps_calculator import determine_caps, determine_plus_minus
    matriz_jugadores = pd.read_csv("01_rankdata.csv", encoding="UTF-8")
    del (matriz_jugadores["id"], matriz_jugadores["NK Level"], matriz_jugadores["Donated"], matriz_jugadores["Role"],
         matriz_jugadores["Join Date"], matriz_jugadores["Collection"])

    total_jugadores = len(matriz_jugadores.index)

    lista_caps = []
    posibles_mas = []
    posibles_menos = []

    for jugador in range(0, total_jugadores - 1):
        lista_caps.append(determine_caps(matriz_jugadores.loc[jugador, "MMR"]))

    ## SE AÑADE 0 A LAS CAPS DE LA CUENTA PARA EL BOT ###
    lista_caps.append(0)

    margin = 100
    for jugador in range(0, total_jugadores - 1):
        posibles_mas.append(determine_plus_minus(matriz_jugadores.loc[jugador, "MMR"], margin)[0])
        posibles_menos.append(determine_plus_minus(matriz_jugadores.loc[jugador, "MMR"], margin)[1])

    ## SE AÑADEN 0 A LA CUENTA PARA EL BOT ##
    posibles_mas.append(0)
    posibles_menos.append(0)

    matriz_jugadores["Caps"] = lista_caps
    matriz_jugadores["+"] = posibles_mas
    matriz_jugadores["-"] = posibles_menos

    # Suma las columnas para obtener los totales

    total_caps = matriz_jugadores["Caps"].sum()
    total_mas = matriz_jugadores["+"].sum()
    total_menos = matriz_jugadores["-"].sum()

    # Crea las nuevas filas como listas y luego se añaden a los indices que corresponden
    totales_por_dia = ["Total per day", "-", str(total_caps), "+" + str(total_mas), str(total_menos)]
    totales = ["Total projected", "-", str(total_caps * 3), "+" + str(total_mas * 3), str(total_menos * 3)]
    matriz_jugadores.loc[total_jugadores] = totales_por_dia
    matriz_jugadores.loc[total_jugadores + 1] = totales

    nombre2 = []
    mmr2 = []

    # Arregla formato de columnas nombre y MMR
    for nombre in range(0, total_jugadores + 2):
        nombre2.append(matriz_jugadores.loc[nombre, "Name"].ljust(24, " "))
        mmr2.append(str(matriz_jugadores.loc[nombre, "MMR"]).center(12, " "))

    # Borra y reemplaza las columnas antiguas por las nuevas
    del (matriz_jugadores["Name"], matriz_jugadores["MMR"])
    matriz_jugadores.insert(0, "Name", nombre2)
    matriz_jugadores.insert(1, "MMR", mmr2)

    projected_caps = open("report_projected_caps.txt", "w", encoding="UTF-8")
    encabezados = matriz_jugadores.head(len(matriz_jugadores))
    projected_caps.write(
        encabezados.to_string(index=False, justify="center"))
    projected_caps.close()

    return matriz_jugadores


