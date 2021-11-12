def CountWordsFromFile():
    filePath = input("Enter the file path")
    fileName = open(filePath, 'r')
    numberOfWords = 0
    for lines in fileName:
        words = lines.split()
        numberOfWords = numberOfWords+ len(words)
    print(numberOfWords)
    
CountWordsFromFile()     