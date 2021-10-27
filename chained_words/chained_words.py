words=['apple', 'eggs', 'snack', 'karat', 'tuna']
def chainedWords(words):
    i = 0
    while i <= len(words):
        if words[i][-1] == words[i+1][0] and words[-1][-1] == words[0][0]:
            print("Chained")
            return True
        else:
            print("Not chained")
            return False
        i += 1
print (chainedWords(words))
