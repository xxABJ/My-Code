nums = {
    "1":6,
    "2":1,
    "3":7,
    "4":8,
    "5":10,
    "6":10
}
print(nums)

largest = max(nums.values())
for i in nums:
    if nums[i] == largest:
        print(i)
        break