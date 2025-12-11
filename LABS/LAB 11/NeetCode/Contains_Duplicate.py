from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                    return True
        return False
    
def main():
    n = int(input("Size of array:" ))
    a = [0] * n
    print("Enter n integers: ")
    for i in range(n):
        a[i] = int(input())
    s = Solution()
    res = s.hasDuplicate(a)
    print(res)
    
if __name__ == "__main__":
     main()
          
