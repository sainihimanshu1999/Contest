class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.sums = sum(nums)

    def update(self, index: int, val: int) -> None:
        self.sums +=  val - self.nums[index]
        self.nums[index] = val
        

    def sumRange(self, left: int, right: int) -> int:
        if (left+right)<len(self.nums)//2:
            return sum(self.nums[left:right+1])

        else:
            return self.sums - sum(self.nums[:left]) - sum(self.nums[right+1:])
        
        