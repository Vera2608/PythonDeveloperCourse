#DRY principe = don't repeat yourself

# for i in range(5):
#     print("iteratie:", 1)
#
# print ("de tafel van 7: ")
# for i in range(1,11):
#     # print(i, "x 10 =", i*10)
#     print(f"{i} x 7 = { i*7}")
# de i is een variabele die wordt gedefiniëerd door de range, de range bepaalt wat de i inhoud.

#
# x = 0
#
# while x <= 20:
#     # print("x is", x)
#     print(x, end=",") #door de end kan je het einde van een print aanpassen, dus ipv enter wordt het hier met een , gescheiden.
#     x += 4 #dit geeft aan dat x telkens 4 hoger moet worden

password = input("Voer je wachtwoord in: ")
geheim = "python"
pogingen = 3

while password != geheim and pogingen > 0:
    pogingen -= 1
    if pogingen == 0:
        print("account geblokkeerd")
        break
    print("Incorrect. Je hebt nog", pogingen, "pogingen")
    password = input("voer je wachtwoord in: ")

if password == geheim:
    print("Welkom, je bent ingelogd")
