from typing import List

def group_anagrams(strs: List[str]) -> List[List[str]]:
    if len(strs) == 1:
        return [strs]

    answer = list()
    anagrams = set()

    for str in strs:
        anagrams.add(''.join(sorted(str)))

    d = dict()

    for anagram in list(anagrams):
        d[anagram] = list()

    for k, v in d.items():
        for i in strs:
            if ''.join(sorted(i)) == k:
                d[k].append(i)
            
    for value in d.values():
        answer.append(value)
    
    return answer

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))

# Input: strs = [""]
# Output: [[""]]
print(group_anagrams([""]))