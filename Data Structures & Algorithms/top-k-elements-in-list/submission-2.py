class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        BEGIN
            counts = empty HashMap(dict)

            FOR num in nums DO
                Increament counts[num] by 1
            END FOR

            bucket = array of len(nums)+1 emtpy lists

            FOR num, freq in counts.items() DO
                append num to bucket[freq]
            END FOR

            result = empty list

            FOR freq from len(counts) to 1 DO
                FOR each num in bucket[freq] DO
                    append num to result

                    IF len(result) == k THEN
                        RETURN result
                    END IF
                END FOR
            END FOR
        END
        """
        #Sttep 1: Build frequency counter
        counts = {}

        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        #Step 2: Create N+1 emtpy buckets
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in counts.items():
            buckets[freq].append(num)

        #Step 3: Walk backwards
        result = []

        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                result.append(num)

                if len(result) == k:
                    return result
                

