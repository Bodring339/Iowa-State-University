# Muhammad Muhamedjonov
# LAB 11 (K), 11-10-2025
# Four approaches of sum of two

def twoSumLoops(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None

def twoSumDict(nums, target):
    mp = {}
    for i, a in enumerate(nums):
        b = target - a
        if b in mp:
            return [mp[b], i]
        mp[a] = i
    return None

def twoSumLoopsAll(nums, target):
    res = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                res.append((i, j))
    return res

def twoSumDictAll(nums, target):
    res = []
    mp = {}
    for i, a in enumerate(nums):
        b = target - a
        if b in mp:
            for j in mp[b]:
                res.append((j, i))
        if a not in mp:
            mp[a] = []
        mp[a].append(i)
    return res
 

def main():
    nums = [2, 11, 7, 15, 2, 7]
    target = 9

    print(f"twoSumLoops (one pair): {twoSumLoops(nums, target)}")
    print(f"twoSumDict (one pair): {twoSumDict(nums, target)}")
    print(f"twoSumLoopsAll (all pairs): {twoSumLoopsAll(nums, target)}")
    print(f"twoSumDictAll (all pairs): {twoSumDictAll(nums, target)}")


if __name__ == "__main__":
    main()