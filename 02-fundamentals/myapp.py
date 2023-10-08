import physics

print("Pomer vahy na Mesici a na Zemi je 1:{}".format(round(physics.EARTH_GRAVITY/physics.MOON_GRAVITY)))
vaha= input("Zadejte svoji hmotnost v kg")
print("Na Zemi jste pritahovani silou {} N ".format(physics.calculate_weight(int(vaha))[0]))

print("Na Mesici budete pritahovani silou {} N ".format(physics.calculate_weight(int(vaha))[1]))

cas=input("Zadejte časový rozdíl blesku a hromu v sekundách")
print("Blesk uderil {} m daleko".format(physics.calculate_lightning_distance(int(cas))))
