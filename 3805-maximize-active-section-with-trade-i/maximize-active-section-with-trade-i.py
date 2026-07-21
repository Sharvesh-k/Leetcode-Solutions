class Solution(object):
    def maxActiveSectionsAfterTrade(self, s):
        # Number of active sections we already have
        ones = s.count('1')

        # Augment the string as required
        t = '1' + s + '1'

        best = 0
        prev = 0
        i = 0

        while i < len(t):
            if t[i] == '1':
                i += 1
            else:
                # Count the current block of consecutive zeros
                j = i
                while j < len(t) and t[j] == '0':
                    j += 1

                curr = j - i

                # Gain from the zero blocks on both sides
                if prev:
                    best = max(best, prev + curr)

                prev = curr
                i = j

        return ones + best