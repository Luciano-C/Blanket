#Definición de clase Card, basada en el codigo _02_required_caps.py
class Card:
    def __init__(self,name,rarity,level):
        self.name = name
        self.level = level
        self.rarity = rarity
    def caps_required(self):
        if self.rarity == "leg":
            if self.level == 1:
                self.caps = 0
            elif self.level == 2:
                self.caps = 200
            elif self.level == 3:
                self.caps = 475
            elif self.level == 4:
                self.caps = 875
            elif self.level == 5:
                self.caps = 1375
            elif self.level == 6:
                self.caps = 1950
            elif self.level == 7:
                self.caps = 2575
        elif self.rarity == "epi":
            if self.level == 1:
                self.caps = 0
            elif self.level == 2:
                self.caps = 0
            elif self.level == 3:
                self.caps = 175
            elif self.level == 4:
                self.caps = 425
            elif self.level == 5:
                self.caps = 800
            elif self.level == 6:
                self.caps = 1275
            elif self.level == 7:
                self.caps = 1825
        elif self.rarity == "rar":
            if self.level == 1:
                self.caps = 0
            elif self.level == 2:
                self.caps = 0
            elif self.level == 3:
                self.caps = 0
            elif self.level == 4:
                self.caps = 125
            elif self.level == 5:
                self.caps = 325
            elif self.level == 6:
                self.caps = 650
            elif self.level == 7:
                self.caps = 1075
        elif self.rarity == "com":
            if self.level == 1:
                self.caps = 0
            elif self.level == 2:
                self.caps = 0
            elif self.level == 3:
                self.caps = 0
            elif self.level == 4:
                self.caps = 0
            elif self.level == 5:
                self.caps = 100
            elif self.level == 6:
                self.caps = 275
            elif self.level == 7:
                self.caps = 575
        return self.caps

# Función para buscar rareza de cartas basada en el codigo _02_required_caps.py
def get_rarities(df_cartas,df_niveles_evaluar):
    cards_rarities = []
    for iteracion_tvt in range(0, len(df_niveles_evaluar)):
        for iteracion in range(0, len(df_cartas)):
            if df_niveles_evaluar.loc[iteracion_tvt, "Name"] in df_cartas.values:
                if df_niveles_evaluar.loc[iteracion_tvt, "Name"] == df_cartas.loc[iteracion, "Name"]:
                    cards_rarities.append(df_cartas.loc[iteracion, "Rarity"])
            else:
                print(f"No se encuentra {niveles_tvt.loc[iteracion_tvt, 'Name']}")
                input()
                quit()
    return cards_rarities

