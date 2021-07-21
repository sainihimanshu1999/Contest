'''In this question we have to shuffle array, we can use random inbuilt class for python and there are two methods
1. random.shuffle(arr) it mutates the original array 2. random.sample(arr,len(arr)) you can save it's result in new array'''


import random

class Soution:

    def  __init__(self,nums):
        self.nums = nums

    def reset(self):
        return self.nums

    def shuffle(self):
        x = random.sample(self.nums,len(self.nums))
        return x


    