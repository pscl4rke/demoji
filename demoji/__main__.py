

import sys

import emoji


def main():
    original = sys.stdin.read()
    cleaned = emoji.demojize(original)
    print(cleaned)


if __name__ == '__main__':
    main()
