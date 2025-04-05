import requests
from collections import defaultdict

from line_profiler import profile


@profile
def get_text(url):
    response = requests.get(url)
    return response.text


@profile
def count_word_frequencies(text, words_to_count):
    word_count = defaultdict(int)
    words = text.split()

    for word in words:
        if word in words_to_count:
            word_count[word] += 1

    return word_count


@profile
def main():
    words_file = "words.txt"
    url = "https://eng.mipt.ru/why-mipt/"

    with open(words_file, "r") as file:
        words_to_count = {line.strip() for line in file if line.strip()}

    text = get_text(url)

    frequencies = count_word_frequencies(text, words_to_count)
    print(frequencies)


if __name__ == "__main__":
    main()
