# Jedeme do kopce
# Matej Matejka

input = open("vrcholy.txt", "r")

t = int(input.readline())

for x in range(0, t - 1):
    pocet_cisel = int(input.readline())
    nadmorske_vysky_in = input.readline().strip()
    nadmorske_vysky = nadmorske_vysky_in.split(" ")
    nadmorske_vysky = list(map(int, nadmorske_vysky))
    lze = True
    for i in range(0, pocet_cisel - 1):
        if nadmorske_vysky[i + 1] - nadmorske_vysky[i] > 3:
            lze = False
            break
    if lze == True:
        print("ANO")
    else:
        print("NE")







