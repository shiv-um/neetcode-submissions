class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        BEGIN
            history = empty HashMap

            FOR i from 0 to length of nums -1 DO
                current_num = nums[i]
                complement = target - current_num

                IF complement exits in history THEN
                    RETURN [history[complement], i]
                END IF

                history[complement] = i
            END FOR
        END
        """
        
        history = {}

        for i in range(len(nums)):
            curr_num = nums[i]
            complement = target - curr_num

            if complement in history:
                return [history[complement], i]
            
            history[curr_num] = i
        
