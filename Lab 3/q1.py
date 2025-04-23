def stats(nums):
    m = sum(nums)/len(nums)
    var = sum((x-m)**2 for x in nums)/len(nums)
    print(f"Mean: {m}, Variance: {var}, Std Dev: {var**0.5}")

nums = list(map(int, input("Enter numbers: ").split()))
stats(nums)