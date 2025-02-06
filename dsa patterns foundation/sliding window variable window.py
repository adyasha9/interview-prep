# 💡 Tip: Use Variable Sliding Window when subarray/substring size is dynamic.

def min_window_substring(s, t):
    """
    Given a string s and a pattern t, find the smallest substring in s that contains all characters of t.
    """
    from collections import Counter

    t_count = Counter(t)  # Frequency of chars in 't'
    window_count = {}
    left, min_len = 0, float('inf')
    required_chars = len(t_count)
    formed_chars = 0
    ans = ""

    for right in range(len(s)):
        char = s[right]
        window_count[char] = window_count.get(char, 0) + 1
        
        if char in t_count and window_count[char] == t_count[char]:
            formed_chars += 1  # One required char completely matched

        while formed_chars == required_chars:  # Try shrinking
            if right - left + 1 < min_len:
                min_len = right - left + 1
                ans = s[left:right + 1]
            
            # Remove leftmost char from window
            window_count[s[left]] -= 1
            if s[left] in t_count and window_count[s[left]] < t_count[s[left]]:
                formed_chars -= 1
            left += 1  # Move left pointer

    return ans

# Test
print(min_window_substring("ADOBECODEBANC", "ABC"))  # Output: "BANC"
