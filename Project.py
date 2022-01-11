import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def qry(wrd):
    wrd = wrd.lower()
    if wrd in data:
        return data[wrd]
    elif len(get_close_matches(wrd, data.keys())) > 0:
        g = get_close_matches(wrd, data.keys())[0]
        aw = input("Did you mean %s instead, Enter Y for \"yes\" and N for \"no\"?" % g)
        aw = aw.capitalize()
        if aw == "Y":
            return data[g]
        elif aw == "N":
            return "Word not found."
        else:
            return "Wrong Choice."
    else:
        return "Word not found."

word = input("Insert Word: ")
ans = qry(word)

if type(ans) == list:
    for item in ans:
        print(item)
else:
    print(ans)
