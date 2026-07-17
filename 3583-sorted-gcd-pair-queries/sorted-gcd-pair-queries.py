import bisect

class Solution:
    def gcdValues(self, nums, queries):
        max_num = max(nums)
        
        freq = [0] * (max_num + 1)
        for x in nums:
            freq[x] += 1
            
        count_divisor = [0] * (max_num + 1)
        for f in range(1, max_num + 1):
            for multiple in range(f, max_num + 1, f):
                count_divisor[f] += freq[multiple]
                
        count_gcd_pair = [0] * (max_num + 1)
        for gcd in range(max_num, 0, -1):
            c = count_divisor[gcd]
            total_pairs_with_div = (c * (c - 1)) // 2
            
            for larger_gcd in range(2 * gcd, max_num + 1, gcd):
                total_pairs_with_div -= count_gcd_pair[larger_gcd]
                
            count_gcd_pair[gcd] = total_pairs_with_div
        prefix_sums = [0] * (max_num + 1)
        for g in range(1, max_num + 1):
            prefix_sums[g] = prefix_sums[g - 1] + count_gcd_pair[g]
            
        ans = []
        for q in queries:
            idx = bisect.bisect_right(prefix_sums, q)
            ans.append(idx)
            
        return ans