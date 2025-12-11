class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)
        if(s == t):
            return True
        return False
    
def main():
    s = str(input("Fisrt string: ")).strip()
    t = str(input("Secon string: ")).strip()
    f = Solution()
    res = f.isAnagram(s, t)
    print(res)
    
if __name__ == "__main__":
     main()
          
