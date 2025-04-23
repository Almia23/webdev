class PairFinder:
    def find(self, nums, target):
        m = {}
        for i, n in enumerate(nums):
            if target-n in m: return [m[target-n], i]
            m[n] = i

print(PairFinder().find([2, 7, 11, 15], 9))