# src: https://wiki.python.org/moin/TimeComplexity#list

def is_anagram(fst_word, snd_word):  # complex: O(n)
    fst_word = fst_word.lower()
    snd_word = snd_word.lower()

    if (fst_word == '' or snd_word == ''):  # complex: O(1)
        return False

    dupe_letter_idx = snd_word.find(fst_word[0])  # complex: O(n)
    if (dupe_letter_idx == -1):
        return False

    fst_word = fst_word[1:]  # complex: O(k) = O(1)
    snd_word = snd_word[:dupe_letter_idx] + snd_word[dupe_letter_idx + 1:]

    if (fst_word == '' and snd_word == ''):  # complex: O(1)
        return True

    return is_anagram(fst_word, snd_word)