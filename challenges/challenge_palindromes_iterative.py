def is_palindrome_iterative(word):  # O(n/2)
    checkpoint = round(len(word)/2)

    for index in range(checkpoint):
        testing_index = -1

        if (word[index] == '' or
                word[testing_index] == '' or
                word[index] != word[testing_index]):
            return False

        testing_index -= 1
        
    return True
