# #DRY principe = don't repeat yourself
#
# # for i in range(5):
# #     print("iteratie:", 1)
# #
# # print ("de tafel van 7: ")
# # for i in range(1,11):
# #     # print(i, "x 10 =", i*10)
# #     print(f"{i} x 7 = { i*7}")
# # de i is een variabele die wordt gedefiniëerd door de range, de range bepaalt wat de i inhoud.
#
# #
# # x = 0
# #
# # while x <= 20:
# #     # print("x is", x)
# #     print(x, end=",") #door de end kan je het einde van een print aanpassen, dus ipv enter wordt het hier met een , gescheiden.
# #     x += 4 #dit geeft aan dat x telkens 4 hoger moet worden
#
# password = input("Voer je wachtwoord in: ")
# geheim = "python"
# pogingen = 3
#
# while password != geheim and pogingen > 0:
#     pogingen -= 1
#     if pogingen == 0:
#         print("account geblokkeerd")
#         break
#     print("Incorrect. Je hebt nog", pogingen, "pogingen")
#     password = input("voer je wachtwoord in: ")
#
# if password == geheim:
# #     print("Welkom, je bent ingelogd")
#
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]
#
# print(matrix [1][2]) #begin met tellen bij 0, dus dit geeft de 2e rij het 3e getal = 6

getallen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for getal in getallen:
    if getal % 2 == 0:
        print(getal, end = " ")

print()

steden = ("Breda", "Utrecht", "Amsterdam")
for stad in steden:
    print(stad)
#hoe krijg ik ze onder elkaar -> gebruik een for-loop


cijfersA = {1, 4, 6, 9}
cijfersB = {2, 4, 6, 7}
print (cijfersA & cijfersB)

# naam = ["Vera", "Kevin", "Eva"]
# leeftijd = [28, 24, 30]
# studentA = {"naam": "Vera", "leeftijd": 28}
# studentB = {"naam": "Kevin", "leeftijd": 24}
# studentC = {"naam": "Eva", "leeftijd": 30}
# gemiddelde = (studentA["leeftijd"] + studentB["leeftijd"] + studentC["leeftijd"])/3
# print(gemiddelde)
#
# print(studentA.keys())
# print(studentA.values())

# Je kan een dictionary nesten:

klas = {
    "studenten": [
        {"naam": "Vera", "leeftijd": 28},
        {"naam": "Kevin", "leeftijd": 24},
        {"naam": "Eva", "leeftijd": 30}
    ]
}
leeftijden = [student["leeftijd"] for student in klas["studenten"]]
gemiddelde = sum(leeftijden)/len(leeftijden)
print(f"Gemiddelde leeftijd = {gemiddelde:.2f}")

