class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """"
        BEGIN
            seen = empty HastSet

            FOR each num in nums DO
                IF num in seen THEN
                    RETURN true
                END IF

                add num to seen
            END FOR

            RETURN false
        END
        """
        seen = set()

        for num in nums:
            if num in seen:
                return True
            
            seen.add(num)
        
        return False
        

