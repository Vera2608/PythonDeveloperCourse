from wachtwoord import inloggen

def test_inloggen():
    assert inloggen("python") == "Welkom, je bent ingelogd"
    # assert inloggen('python123') == "account geblokkeerd"
    assert inloggen("python123")[0].startswith("Incorrect. Je hebt nog")
