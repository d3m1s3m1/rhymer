vowel_map = dict()
vowels = "iyɨʉɯuɪʏʊeøɘɵɤoe̞ø̞əɤ̞o̞ɛœɜɞʌɔæɐaɶäɑɒɝŋ"

def vowelize(word):
    ret = []
    vowelized = ""
    for c in word:
        if c in vowels:
            vowelized += c
        else:
            if vowelized != "": 
                ret.append(vowelized)
            vowelized = ""
    return ret

def find_vowels(search_vowels):
    ret = []
    for word, vowels in vowel_map.items():
        if vowels == search_vowels:
            ret.append(word)
    return ret

with open("data/en_Us.csv", encoding="utf-8") as f:
    data = f.read().splitlines()
    
    for i in data:
        d = i.split(",")
        word = d[0]
        ipa = d[1]
        
        vowel_map[word] = vowelize(ipa)


def d(word):
    ret = []
    vowelized = ""
    for c in word:
        if c in vowels:
            vowelized += c
        else:
            if vowelized != "": 
                ret.append(vowelized)
            vowelized = ""
    return ret

class Path:
    remaining = []
    traversed = []

    def __init__(self, remaining=[], traversed=[]):
        self.remaining = remaining
        self.traversed = traversed


def search(vowels):
    queue = []
    queue.append(Path(vowels))
    while len(queue) != 0:
        v = queue.pop(0)
        if len(v.remaining) == 0:
            print(" ".join(v.traversed))
        # find all edges
        edges = []
        for word, search_vowels in vowel_map.items():
            if len(search_vowels) > len(v.remaining):
                continue
            works = True
            for i, k in enumerate(search_vowels):
                if k != v.remaining[i]:
                    works = False
                    break
            if works:
                t = v.traversed.copy()
                t.append(word)
                edges.append(Path(v.remaining[len(search_vowels):], t))
        for e in edges:
            # print(e.traversed, e.remaining)
            queue.append(e)

query = input()
query_list = []

for word in query.split(" "):
    query_list.extend(vowel_map[word])

print("Searching Vowels: ", query_list)
search(query_list)
