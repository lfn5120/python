# ANAGRAM FINDER
# This application has the objective of identifying if the two strings whom of which the 
# user prompts is or not an anagram (this exercise was specifically asked only for lowercase single words)

def anagram(str1, str2) -> bool:
    frequency1 = {}
    frequency2 = {}
    for char in str1:
        frequency1[char] = frequency1.get(char, 0) + 1
    for char in str2:
        frequency2[char] = frequency2.get(char, 0) + 1
    for key in frequency1:
        if key not in frequency2:
            return False
        if frequency1[key] != frequency2[key]:
            return False
    return True

print(anagram(*input(""""Welcome to ANAGRAM FINDER. Please write two words in lowercase and separate them by a space "
""").split()))
