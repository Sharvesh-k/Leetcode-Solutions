class Solution(object):
    def gcdOfOddEvenSums(self, n):
        evenSum=0
        oddSum=0
        for i in range(1,2*n+1):
            if i%2==0:
                evenSum+=i
            else:
                oddSum+=i
        while evenSum:
            oddSum,evenSum=evenSum,oddSum%evenSum
        return abs(oddSum)