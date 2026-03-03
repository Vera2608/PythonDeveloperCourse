def inloggen (password):
    geheim = "python"
    pogingen = 3

    while password != geheim and pogingen > 0:
        pogingen -= 1
        if pogingen == 0:
            return ("account geblokkeerd")
        return ("Incorrect. Je hebt nog", pogingen, "pogingen")
        # password = input("voer je wachtwoord in: ")

    if password == geheim:
        return ("Welkom, je bent ingelogd")

if __name__ == "__main__":
    password = input("Voer je wachtwoord in: ")
    print(inloggen(password))