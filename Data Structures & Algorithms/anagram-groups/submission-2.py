class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # defaultdict(list) prevents a KeyError crash by automatically creating an empty list [] the very first time you access a key that doesn't exist yet.
        groups = defaultdict(list)

        for word in strs:
            count = [0] * 26
            
            for char in word:
                index = ord(char) - ord('a')
                count[index] += 1

            key = tuple(count)

            # This if block not required then.
            # if key not in groups:
            #     groups[key] = []

            groups[key].append(word)
            
        return list(groups.values())