class ShoesModel:
    def __init__(self):
        self.seznam_bot = []

    def pridat_boty(self, typ_bot, typ_obuvi, barva, cena, znacka, velikost):
        self.seznam_bot.append({
            'typ_bot': typ_bot,
            'typ_obuvi': typ_obuvi,
            'barva': barva,
            'cena': cena,
            'znacka': znacka,
            'velikost': velikost
        })

    def ziskat_seznam_bot(self):
        return self.seznam_bot


class ShoesController:
    def __init__(self, model):
        self.model = model

    def pridat_boty(self, typ_bot, typ_obuvi, barva, cena, znacka, velikost):
        self.model.pridat_boty(typ_bot, typ_obuvi, barva, cena, znacka, velikost)

    def ziskat_seznam_bot(self):
        return self.model.ziskat_seznam_bot()


class ShoesView:
    def zobrazit_boty(self, seznam_bot):
        for idx, boty in enumerate(seznam_bot):
            print(f"Boty {idx + 1}:")
            print(f"Typ botů: {boty['typ_bot']}")
            print(f"Typ obuvi: {boty['typ_obuvi']}")
            print(f"Barva: {boty['barva']}")
            print(f"Cena: {boty['cena']}")
            print(f"Značka: {boty['znacka']}")
            print(f"Velikost: {boty['velikost']}\n")


# Příklad použití:
model = ShoesModel()
controller = ShoesController(model)
view = ShoesView()

controller.pridat_boty("mužské", "tenisky", "černá", 50, "Nike", 42)
controller.pridat_boty("ženské", "boty", "hnědá", 80, "Timberland", 38)

seznam_bot = controller.ziskat_seznam_bot()
view.zobrazit_boty(seznam_bot)