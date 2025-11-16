"""
Programming exercise:
A word squared

Please write a function named squared, which takes a string argument and an integer argument, and prints out a square of characters as specified by the examples below.

squared("ab", 3)
print()
squared("aybabtu", 5)

Sample output

aba
bab
aba

aybab
tuayb
abtua
ybabt
uayba
"""


def squared(text: str, size: int) -> None:
    col = 0
    # A pool of characters to be used to create a new row
    pool = text

    while col < size:
        # We add to the charcter pool if the length is less that
        # the length of the text.
        while len(pool) < size:
            pool += text

        print(pool[:size])

        pool = pool[size:]
        col += 1


if __name__ == "__main__":
    squared("ab", 3)
