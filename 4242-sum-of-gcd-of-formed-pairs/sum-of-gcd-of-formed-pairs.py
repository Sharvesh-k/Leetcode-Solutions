class Solution:
    
    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
    def gcdSum(self, nums):
        n = len(nums)
        prefixMax = float('-inf')
        prefixGcd = [0] * n
        
        for i in range(n):
            prefixMax = max(prefixMax, nums[i])
            prefixGcd[i] = self.gcd(prefixMax, nums[i])
        
        prefixGcd.sort()
        
        s = 0
        for i in range(n // 2):
            s += self.gcd(prefixGcd[i], prefixGcd[n - i - 1])
        
        return s 