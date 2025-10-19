"""
CP1404 Practical
Count word occurrences in a string.
"""

def main():
    """Count and display the occurrences of each word in a string."""
    word_to_count = {}
    # text = input("Text: ")
    text = "this is a collection of words of nice words this is a fun thing it is"
    words = text.split()

    for word in words:
        # LBYL (Look Before You Leap) pattern
        word_to_count[word] = word_to_count.get(word, 0) + 1

    max_length = max(len(word) for word in words)

    for word in sorted(word_to_count):
        print(f"{word:{max_length}} : {word_to_count[word]}")


if __name__ == "__main__":
    main()
