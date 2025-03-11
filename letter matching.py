def matchWords(words):
    counter = 0
    lst = []
    
    for word in words:
        
        if len(word) > 1 and word[0] == word[-1]:
            
            counter = counter + 1
            lst.append(word)
            
    print(f"List of words with first and last character same \n{lst}\n\n")
    
    return counter
list1 = ["abc", "cfc", "xyz", "aba", "1221", "saifan", "nahian", "indradipi", "noorian"]
count = matchWords(list1)

print(f"Number of words having first and last character same : {count}")