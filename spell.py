import re
from collections import Counter


def get_words(text_file):
    return re.findall(r'\w+', text_file.lower())


WORDS = Counter(get_words(open('content.txt').read()))


def get_prob(word, total_words=sum(WORDS.values())):
    return WORDS[word] / total_words


def get_correct_word(word):
    return max(candidates(word), key=get_prob)


def candidates(word):
    return Find([word]) or Find(edits1(word)) or Find(edits2(word)) or [word]


def Find(words):
    return set(w for w in words if w in WORDS)


def edits1(word):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    splits = [(word[:i], word[i:]) for i in range(0, len(word) + 1)]

    deletes = [L + R[1:] for (L, R) in splits if len(R) > 0]
    transposes = [L + R[1] + R[0] + R[2:] for (L, R) in splits if len(R) > 1]
    replaces = [L + c + R[1:] for (L, R) in splits if len(R) > 0 for c in letters]
    inserts = [L + c + R for (L, R) in splits for c in letters]

    return set(deletes + transposes + replaces + inserts)


def edits2(word):
    return set(w2 for w1 in edits1(word) for w2 in edits1(w1))


if __name__ == "__main__":
    print("Enter the words and see the correct spellings\n")
    while 1:
        word = raw_input()
        print("Predicted spelling of {0} is : {1}\n".format(word, get_correct_word(word)))


