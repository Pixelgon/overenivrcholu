# Jedeme do kopce
# Matej Matejka

vrcholy = open("vrcholy.txt", "r")

t = int(vrcholy.readline())

# Pro kazdy seznam vrcholu
for x in range(0, t):
    pocet_cisel = int(vrcholy.readline())
    nadmorske_vysky_in = vrcholy.readline().strip()
    nadmorske_vysky = nadmorske_vysky_in.split(" ")
    nadmorske_vysky = list(map(int, nadmorske_vysky))
    lze = True

    # Udelej pro cisla v seznamu od 0. do předposledního
    for i in range(0, pocet_cisel - 1):
        if nadmorske_vysky[i + 1] - nadmorske_vysky[i] > 3:
            lze = False
            break

    if lze is True:
        print("ANO")
    else:
        print("NE")
exit()
