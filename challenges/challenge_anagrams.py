# src: https://wiki.python.org/moin/TimeComplexity#list

def is_anagram(first_word, second_word):  # complex: O(n)
    first_word = first_word.lower()
    second_word = second_word.lower()

    if (first_word == '' or second_word == ''):  # complex: O(1)
        return False

    dupe_letter_index = second_word.find(first_word[0])  # complex: O(n)
    if (dupe_letter_index == -1):
        return False

    first_word = first_word[1:]  # complex: O(n)
    second_word = second_word[:dupe_letter_index] + second_word[dupe_letter_index + 1:]  # complex: O(n)

    if (first_word == '' and second_word == ''):  # complex: O(1)
        return True

    return is_anagram(first_word, second_word)