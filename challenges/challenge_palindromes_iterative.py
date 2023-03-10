def is_palindrome_iterative(word):  # O(n/2)
    if (word == ''):
        return False

    checkpoint = round(len(word)/2)
    testing_index = -1

    for index in range(checkpoint):
        if (word[index] == '' or
                word[testing_index] == '' or
                word[index] != word[testing_index]):
            return False

        testing_index -= 1

    return True
