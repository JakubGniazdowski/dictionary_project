import difflib
import json
data = json.load(open('data.json'))

def translation(word):
    word=word.lower()
    if word in data:
        return data[word]
    elif word.title() in data: 
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(difflib.get_close_matches(word ,data.keys()))>0:
        yn=input("did you mean %s instead. Enter Y if yes N if no: " % difflib.get_close_matches(word ,data.keys())[0])
        if yn=="Y":
            return data[difflib.get_close_matches(word ,data.keys())[0]]
        if yn=="N":
            return "there is no word like this in our dictionary, sorry"
        else:
            return "we didnt understand your entry"
    else:
        return "there is no word like this in our dictionary, sorry"
        

word=input("put here word that you search for: ")
output=translation(word)
if type(output)== list:
    for item in output:
        print(item)
else:
    print(output)