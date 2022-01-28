import random


def primary():
    f = open("quotes.txt")
    quotes = f.readlines()
    f.close()

    last = len(quotes) - 1

    for i in range(2):
        print(f"Quote #{i+1}: {quotes[random.randint(0, last)]}")


if __name__ == "__main__":
    primary()
