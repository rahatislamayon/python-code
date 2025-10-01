def get_cents():
    while True:
        try:
            cents = int(input("No of cents: "))
            if cents >= 0:
                return cents
        except ValueError:
            pass  # ignore invalid input


def calculate_quarters(cents):
    return cents // 25


def calculate_dimes(cents):
    return cents // 10


def calculate_nickels(cents):
    return cents // 5


def calculate_pennies(cents):
    return cents


def main():
    cents = get_cents()

    quarters = calculate_quarters(cents)
    cents -= quarters * 25

    dimes = calculate_dimes(cents)
    cents -= dimes * 10

    nickels = calculate_nickels(cents)
    cents -= nickels * 5

    pennies = calculate_pennies(cents)
    cents -= pennies * 1

    coins = quarters + dimes + nickels + pennies
    print(coins)


if __name__ == "__main__":
    main()
