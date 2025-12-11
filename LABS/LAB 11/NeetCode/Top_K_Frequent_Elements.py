from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        cnt = 0
        a = []
        for i in range(len(nums)):
            cnt += 1
            if(i == len(nums) - 1 or nums[i] != nums[i + 1]):
                a.append((-cnt, nums[i]))
                cnt = 0

        a.sort()
        res = []
        for i in range(k):
            res.append(a[i][1])
        return res

def main():
    n = int(input("Size of array:" ))
    k = int(input("Enter k: "))
    a = [0] * n
    print("Enter n integers: ")
    for i in range(n):
        a[i] = int(input())
    s = Solution()
    res = s.topKFrequent(a, k)
    print(res)
    
if __name__ == "__main__":
     main()
          
