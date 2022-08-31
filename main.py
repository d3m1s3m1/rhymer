

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


class Tree:
    def __init__(self, branches={}, words=[]):
        self.branches = branches
        self.words = words

    def find(self, vowelized):
        if len(vowelized) == 0:
            return self.words
        else:
            if vowelized[0] in self.branches:
                return self.branches[vowelized[0]].find(vowelized[1:])
            else:
                return []

    def insert(self, word, vowelized):
        if len(vowelized) == 0:
            self.words.append(word)
        else:
            if vowelized[0] in self.branches:
                self.branches[vowelized[0]].insert(word, vowelized[1:])
                return
            node = Tree({}, [])
            node.insert(word, vowelized[1:])
            self.branches[vowelized[0]] = node


vowel_tree = Tree()

with open("data/en_Us.csv", encoding="utf-8") as f:
    data = f.read().splitlines()

    for i in data:
        d = i.split(",")
        word = d[0]
        ipa = d[1]

        vowel_map[word] = vowelize(ipa)
        vowel_tree.insert(word, vowelize(ipa))


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
        s = v.remaining.copy()
        while len(s) != 0:
            to_add = vowel_tree.find(s)
            for i in to_add:
                trav = v.traversed.copy()
                trav.append(i)
                edges.append(Path(v.remaining[len(s):], trav))
            s.pop()
        for e in edges:
            # print(e.remaining, e.traversed)
            queue.append(e)


def find_vowels(search_vowels):
    ret = []
    for word, vowels in vowel_map.items():
        if vowels == search_vowels:
            ret.append(word)
    return ret


query = input()
query_list = []

for word in query.split(" "):
    query_list.extend(vowel_map[word])

print("Searching Vowels: ", query_list)
search(query_list)
