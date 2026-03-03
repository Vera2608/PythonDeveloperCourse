# # # def begroet():
# # #     print("Hallo daar!")
# # #
# # # begroet()
# # #
# # # def begroet(naam):
# # #     print("Hallo daar!")
# # #
# # # begroet("Vera")
# #
# # # def vierkant(n):
# # #     return n * n
# # # for i in range(1, 6):
# # #     print(f"{i}2 = {vierkant(i)}")
# #
# # # def vermedigvuldig:
# # #         return x * y
# # # lijst = [(1,2),(3,4),(5,6),(7,8)]
# # # for x, y in lijst:
# # #     pirnt(vermedigvuldig(x,y))
# #
# # # def is_even(num):
# # #     return num % 2 == 0
# # #
# # # print(is_even(2))
# # # print(is_even(-1))
# # # print(is_even(13))
# # # print(is_even(4.5))
# # # print(is_even(-6))
# #
# # def gemiddelde(getallen):
# #     return sum(getallen) / len(getallen)
# # # print(gemiddelde([1, 4, 9.6, 3]))
# #
# # def herhaal(tekst,aantal_keren):
# #     return (tekst * aantal_keren)
# # print(herhaal("hallo \n", 3))
# #
#
# cijfers = [6.5, 8.0, 7.3, 9.1]
# def gemiddelde(cijfers):
#     return sum(cijfers) / len(cijfers)
#
# if gemiddelde(cijfers) < 5.5:
#     print("onvoldoende")
# elif 5.5 < gemiddelde(cijfers) < 7.9:
#     print("voldoende")
# else:
#     print("goed")
#
#
# # via Chat GPT gegenereerd:
# # def gemiddelde(lijst):
# #     return sum(lijst) / len(lijst)
# #
# #
# # def beoordeling(gem):
# #     if gem < 5.5:
# #         print(f"Beoordeling: Onvoldoende (gemiddelde: {gem:.2f})")
# #     elif gem < 8:
# #         print(f"Beoordeling: Voldoende (gemiddelde: {gem:.2f})")
# #     else:
# #         print(f"Beoordeling: Goed (gemiddelde: {gem:.2f})")
# #
# #
# # gem = gemiddelde(cijfers)
# #
# # print(f"Cijfers: {cijfers}")
# # print(f"Gemiddelde: {gem:.2f}")
# # beoordeling(gem)
try:
    x = int(input("geef een getal: "))
    print(10/x)
# except ValueError:
#     print("Dit was geen getal")
except ZeroDivisionError:
    print("Je kan niet delen door 0")
except Exception as e:
    print(e)

print("We gaan hier verder")
