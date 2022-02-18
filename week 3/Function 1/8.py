def spy_game(nums):
    s=""
    for i in range(len(nums)):
        if nums[i]==0 or nums[i]==7:
            s+=str(nums[i])
    if "007" in s:
        return True
    return False

s=list(map(int, input().split()))

print(spy_game(s))