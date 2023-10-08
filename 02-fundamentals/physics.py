'''
Konstanty v Pythonu

Konstanta je vlastně speciální typ proměnné, jejíž hodnota nemůže být změněna.
V Pythonu jsou konstanty obvykle deklarovány a přiřazovány v modulu, který bývá importován do souboru aplikace.
Konstanty jsou pojmenovány velkými písmeny a jednotlivá slova jsou oddělována podtržítky.
'''

EARTH_GRAVITY = 9.81  # normální pozemské tíhové zrychlení v m/s^2
MOON_GRAVITY = 1.62  # měsíční gravitace v m/s^2
SPEED_OF_LIGHT = 299792458  # rychlost světla ve vakuu v m/s
SPEED_OF_SOUND = 343  # rychlost zvuku při teplotě 20 °C v suchém vzduchu v m/s

def calculate_weight(mass):
    """
    Vypočítá váhu objektu na Zemi a Měsíci na základě jeho hmotnosti.
    """
    weight_earth = mass * EARTH_GRAVITY  # Váha na Zemi
    weight_moon = mass * MOON_GRAVITY  # Váha na Měsíci
    return (weight_earth, weight_moon)

def calculate_lightning_distance(time_interval):
    """
    Vypočítá vzdálenost, na kterou udeřil blesk, na základě časového intervalu mezi bleskem a hromem.
    """
    # Vzdálenost = časový interval × rychlost zvuku ve vzduchu
    return time_interval * SPEED_OF_SOUND

lightning_distance = calculate_lightning_distance(5)
weight_earth, weight_moon = calculate_weight(60)

''' 
Úkol:
1. Doplňte správně hodnoty uvedených konstant.
2. Doplňte physics.py o několik výpočtových funkcí (opatřené docstrings), v nichž využijete minimálně všechny výše uvedené konstanty.
Samozřejmě můžete své řešení rozšířit i o jiné fyzikální konstanty.
3. Vytvořte z tohoto souboru samostatný modul v Pythonu podle návodu, který si sami najdete na internetu.      
4. Vytvořte vlastní aplikaci myapp.py, do níž tento modul importujte. Demonstrujte v ní na jednoduchých příkladech využití vámi
připravených funkcí.  
'''