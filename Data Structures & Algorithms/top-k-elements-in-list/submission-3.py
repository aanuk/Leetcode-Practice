class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for i in nums:
            if i in counter:
                counter[i] += 1
            else:
                counter[i] = 1
        # counter = {1: 3, 2: 1, 5: 3}, k = 2

        only_count = []
        for keys, values in counter.items():
            only_count.append(values)
        only_count.sort()
        # [1, 3, 3]

        final = []
        for i in range(k):
            maxi = only_count.pop()  
            for key, value in counter.items():
                if value == maxi:
                    final.append(key)
                    del counter[key]  
                    break

        return final




            
 
             