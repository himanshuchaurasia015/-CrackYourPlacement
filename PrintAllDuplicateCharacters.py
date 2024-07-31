def printDuplicates(str):
    characters = list(str)
    characters.sort()
    i = 0
    while i < len(characters):
        count = 1
        while i < len(characters)-1 and characters[i] == characters[i+1]:
            count += 1
            i += 1
        if count > 1:
            print(characters[i], ", count = ", count)
        i += 1