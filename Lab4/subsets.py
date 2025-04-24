class Subsets:
    def get(self, nums):
        res = [[]]
        for n in nums:
            res += [r+[n] for r in res]
        return res

print(Subsets().get([1,2,3]))