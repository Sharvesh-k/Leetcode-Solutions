class Solution(object):
    def sequentialDigits(self, low, high):
        ans = []
        s = "123456789"

        for length in range(len(str(low)), len(str(high)) + 1):
            for i in range(10 - length):
                num = int(s[i:i + length])
                if low <= num <= high:
                    ans.append(num)

        return ans