def palindromes(text):
    text = text.lower()
    results = []
    for i in range(len(text)):
        for j in range(i):
            chunk = text[j:i+1]
            if chunk == chunk[::-1]:
                results.append(chunk)
    if len(sorted(results,key=len)) == 0:
        return text[0]
    else:
        return sorted(results, key=len)
mystring = raw_input("Please entere a word and I will find the longest palindrome:\n")
print palindromes(mystring)
