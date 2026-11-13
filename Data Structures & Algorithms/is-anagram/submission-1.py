class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        BEGIN
            IF length of s != length of t THEN
                RETURN false
            END IF

            counts = empty HashMap

            FOR i from 0 to length of s - 1 DO
                Increament counts[s[i]] by 1
                Decreament counts[t[i]] by 1
            END FOR

            FOR each value in counts DO
                IF value != 0 THEN
                    RETURN false
                END IF
            END FOR

            RETURN true
        END
        """
        if len(s) != len(t):
            return False

        counts = {}

        for i in range(len(s)):
            counts[s[i]] = counts.get(s[i], 0) + 1
            counts[t[i]] = counts.get(t[i], 0) - 1

        for val in counts.values():
            if val != 0:
                return False
        
        return True