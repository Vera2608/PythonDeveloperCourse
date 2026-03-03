with open("test.txt") as f:
    inhoud = f.readlines()

for regel in inhoud:
    print(regel, end= '')
    # je kan de tekst printen, maar ook in een variabele zetten, zodat je er later nog iets mee kan doen.