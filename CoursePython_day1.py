# naam = input('Wat is je naam?')
# print('Hallo ' + naam)
#
# getal_I = int(input('Geef een getal:'))
# getal_II = int(input('Geef een ander getal:'))
#
# som = sum((getal_I, getal_II))
# print(som)
#
# temperatuur = input('Hoeveel graden celcius is het?')
# temperatuur = float(temperatuur)
# fahrenheit = temperatuur * 9 / 5 + 32
# print(fahrenheit)
#
# stad = input('In welke stad woon je? ')
# land = input('In welk land ligt dat? ')
# print(f'Ik kom uit {land} en woon in {stad}. Het is hier {temperatuur} graden celcius.')
#
# leeftijd = int(input('Wat is jouw leeftijd? '))
# if leeftijd >= 18:
#         print('Jij mag stemmen.')
# elif 12 < leeftijd < 18:
#         print('Jij mag een jeugdstem uitbrengen.')
# else:
#     print('Jij mag niet stemmen.')

# getal = input('Geef mij een getal. ')
# getal = int(getal)
# if getal == 0:
#     print('dit is 0.')
# elif getal >0:
#     print('dit is een positief getal.')
# else:
#     print('dit is een negatief getal.')
#
# wachtwoord = input('Wat is jouw wachtwoord? ')
# if wachtwoord == 'python':
#     print('dit is het correcte wachtwoord')
# else:
#     print('dit wachtwoord is incorrect')
#
# leeftijd = int(input('Hoe oud ben je? '))
# if leeftijd >=18:
#     print('Jij bent een volwassene.')
# elif 14 < leeftijd < 18:
#     print('Jij bent een tiener.')
# else:
#     print('Jij bent een kind')

invoer = input('Enter invoer: ')
if invoer.isdigit():
    print(f"Jouw getal is {invoer}")
elif invoer.isalpha():
    print(f'Jouw tekst is {invoer}')
else:
    print("alphanumeriek")
