class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        BEGIN
            groups = empty HastMap(Dict)

            FOR each word IN strs DO
                count = empty array of 26

                FOR char IN word DO
                    index = ASCII(char) - ASCII(a)
                    Increament count[index] by 1
                END FOR

                key = count

                IF key does not exists IN groups THEN
                    groups[key] = empty list

                Append word to group[key]
            END FOR

            RETURN list of all values in groups
        END
        """
        groups = {}

        for word in strs:
            count = [0] * 26
            
            for char in word:
                index = ord(char) - ord('a')
                count[index] += 1

            key = tuple(count)

            if key not in groups:
                groups[key] = []

            groups[key].append(word)
            
        return list(groups.values())