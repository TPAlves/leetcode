from ast import List
input = [1, 2, 3, 1]
result = False
# for i in range(len(input)):
#     for j in range(i + 1, len(input)):
#         if input[i] == input[j]:
#             result = True
#             break

# print(result)  


for n, i in enumerate(input):
    if i in input[n + 1:]:
        result = True
        break
    
print(result)
nums = [1, 2, 3, 1]

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool: 
        hash = set()
        for n in nums:
            if n in hash:
                return True
            hash.add(n)
        return False

    