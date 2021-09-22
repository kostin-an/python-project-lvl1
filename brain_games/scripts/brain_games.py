#!/usr/bin/env python3

from brain_games.cli import welcome_user
from brain_games.scripts.brain_even import even_check


def greething():
    print('Welcome to the Brain Games!')


def main():
    greething()
    name = welcome_user()
    even_check(name)


if __name__ == '__main__':
    main()
