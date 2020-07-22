from greeting import see_hello


def test_greeting():
    assert see_hello() == "Hello World", 'Greeting message is wrong'


if __name__ == "__main__":
    test_greeting()
