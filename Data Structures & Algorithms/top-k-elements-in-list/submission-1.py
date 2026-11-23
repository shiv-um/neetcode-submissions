class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
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
                

