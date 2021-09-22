from brain_games.cli import welcome_user
from brain_games.even import even_check


def main():
    name = welcome_user()
    even_check(name)


if __name__ == '__main__':
    main()
