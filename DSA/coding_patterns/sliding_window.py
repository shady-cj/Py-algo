"""
: Fixed size 

Find the max sum subarray of a fixed size K


Example input:
[4, 2, 1, 7, 8, 1, 2, 8, 1, 0]
"""


def max_subarray(array, k):
    if len(array) < k or k <= 0:
        return None
    current_running_sum = sum(array[:k])
    max_sum = current_running_sum
    subarray = array[:k]
    for i in range(k, len(array)):
        current_running_sum -= array[i - k]
        current_running_sum += array[i]
        if current_running_sum > max_sum:
            max_sum = current_running_sum
            subarray = array[(i - k + 1) : (i + 1)]

    return subarray


# print(max_subarray([4, 2, 1, 7, 8, 1, 2, 8, 1, 9], 3))

# print(
#     max_subarray(
#         [-1, -2, 3, 4],
#         3,
#     )
# )


# Let imagine python doesn't have sum(arr[:k])
def max_subarray2(array, k):
    if k > len(array) or k <= 0:
        return None

    max_sum = None
    current_running_sum = 0

    for i in range(len(array)):
        current_running_sum += array[i]
        if i >= k - 1:
            if max_sum is None:
                max_sum = current_running_sum
            else:
                max_sum = max(current_running_sum, max_sum)
            current_running_sum -= array[i - k + 1]
    return max_sum


# print(max_subarray2([4, 2, 1, 7, 8, 1, 2, 8, 1, 9], 2))


# Solving leetcode problem https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/


# Using set and dictionary
# def max_sum_of_distinct_subarrays(nums, k):
#     if k > len(nums) or k <= 0:
#         return 0
#     current_running_sum = 0
#     max_sum = current_running_sum
#     distinct_subarray = set([])
#     array_map = {}
#     for i in range(len(nums)):
#         array_map[nums[i]] = array_map.get(nums[i], 0) + 1
#         if nums[i] not in distinct_subarray:
#             current_running_sum += nums[i]
#             distinct_subarray.add(nums[i])

#         if len(distinct_subarray) == k:
#             max_sum = (
#                 current_running_sum
#                 if max_sum is None
#                 else max(current_running_sum, max_sum)
#             )

#         if i >= k - 1:
#             array_map[nums[i - k + 1]] -= 1
#             if not array_map[nums[i - k + 1]]:
#                 current_running_sum -= nums[i - k + 1]
#                 distinct_subarray.remove(nums[i - k + 1])

#     return max_sum


# using only dictionary(hashmap) since some languages don't have set() feature built in


def max_sum_of_distinct_subarrays(nums, k):
    if k > len(nums) or k <= 0:
        return 0
    current_running_sum = 0
    max_sum = current_running_sum
    array_map = {}
    for i in range(len(nums)):
        array_map[nums[i]] = array_map.get(nums[i], 0) + 1
        current_running_sum += nums[i]
        if len(array_map) == k:
            max_sum = (
                current_running_sum
                if max_sum is None
                else max(current_running_sum, max_sum)
            )
        if i >= k - 1:
            array_map[nums[i - k + 1]] -= 1
            current_running_sum -= nums[i - k + 1]
            if not array_map[nums[i - k + 1]]:
                del array_map[nums[i - k + 1]]

    return max_sum


# print(max_sum_of_distinct_subarrays([1, 5, 4, 2, 9, 9, 9], 3))
# print(max_sum_of_distinct_subarrays([4, 4, 4], 3))
# print(max_sum_of_distinct_subarrays([3, 2, 3, 1], 3))
# print(max_sum_of_distinct_subarrays([1, 1, 1, 7, 8, 9], 3))


# Dynamic Sliding Window
# Leetcode problem https://leetcode.com/problems/minimum-size-subarray-sum/


def minimum_size_subarray_sum(target, nums):
    min_size = 0
    window_start = 0
    current_window_sum = 0

    for window_end in range(len(nums)):
        current_window_sum += nums[window_end]
        while current_window_sum >= target:
            current_size = (
                window_end - window_start + 1
            )  # e.g start = 0 end = 2 => array of length 3
            min_size = current_size if min_size == 0 else min(min_size, current_size)
            if min_size == 1:
                return min_size
            current_window_sum -= nums[window_start]
            window_start += 1

    return min_size


# Try with divide and conquer
# print(minimum_size_subarray_sum(7, [2, 3, 1, 2, 4, 3]))


# Longest Substring without repeating characters
# Leetcode Problem https://leetcode.com/problems/longest-substring-without-repeating-characters/

# The function returns the length


def longest_sub_without_repeating_characters(s):
    if len(s) < 1:
        return 0

    windowStart = 0
    current_substring_length = 0
    longest_substring = current_substring_length
    string_map = {}

    for windowEnd in range(len(s)):
        string_map[s[windowEnd]] = string_map.get(s[windowEnd], 0) + 1
        current_substring_length += 1
        # print(string_map)
        while string_map[s[windowEnd]] > 1:
            string_map[s[windowStart]] -= 1
            windowStart += 1
            current_substring_length -= 1
        # print(current_substring_length, longest_substring)
        if current_substring_length > longest_substring:
            longest_substring = current_substring_length

    return longest_substring


# print(longest_sub_without_repeating_characters("abcabcbb"))
# print(longest_sub_without_repeating_characters("bbbbb"))
# print(longest_sub_without_repeating_characters("pwwkew"))

# Leetcode Problem https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/


def longest_substr_with_k_characters(s, k):
    if k > len(s) or k <= 0:
        return 0

    hashmap = {}

    for c in s:
        hashmap[c] = hashmap.get(c, 0) + 1

    l = 0

    while l < len(s) and hashmap[s[l]] >= k:
        l += 1

    if l == len(s):
        return l

    s1 = longest_substr_with_k_characters(s[:l], k)

    while l < len(s) and hashmap[s[l]] < k:
        l += 1

    s2 = longest_substr_with_k_characters(s[l:], k)

    return max(s2, s1)


# print(longest_substr_with_k_characters("aca", 2))
# print(longest_substr_with_k_characters("ababbc", 1))


# Longest substring with at most k distinct characters
# Leetcode problem https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
# https://www.codingninjas.com/studio/problems/longest-substring-with-at-most-k-distinct-characters_2221410
def longest_substring_with_at_most_k_distinct_characters(k, str):
    if len(str) < 1 or k > len(str):
        return 0

    windowStart = 0
    char_map = {}
    current_substring_length = 0
    longest_substring = current_substring_length

    for windowEnd in range(len(str)):
        char_map[str[windowEnd]] = char_map.get(str[windowEnd], 0) + 1
        current_substring_length += 1
        while len(char_map) > k:
            char_map[str[windowStart]] -= 1
            if not char_map[str[windowStart]]:
                del char_map[str[windowStart]]
            windowStart += 1
            current_substring_length -= 1
        if current_substring_length > longest_substring:
            longest_substring = current_substring_length
    return longest_substring


# print(longest_substring_with_at_most_k_distinct_characters(3, "aabbbbbbccc"))


# Find all anagrams of a string
# Leetcode problem https://leetcode.com/problems/find-all-anagrams-in-a-string/


def find_anagrams(s, p):
    if len(p) > len(s):
        return []
    anagram_indexes = []
    char_map = {}
    p_map = {}
    windowStart = 0
    for char in p:
        p_map[char] = p_map.get(char, 0) + 1
    for windowIndex in range(len(s)):
        char_map[s[windowIndex]] = char_map.get(s[windowIndex], 0) + 1
        if windowIndex >= len(p) - 1:
            not_found = False
            for c in p_map:
                if c not in char_map or p_map[c] != char_map[c]:
                    not_found = True
            if not not_found:
                anagram_indexes.append(windowStart)
            char_map[s[windowStart]] -= 1
            if not char_map[s[windowStart]]:
                del char_map[s[windowStart]]
            windowStart += 1

    return anagram_indexes


# print(find_anagrams("abab", "ab"))
# print(find_anagrams("cbaebabacd", "abc"))
# print(find_anagrams("baa", "aa"))


# Leetcode Problem https://leetcode.com/problems/sliding-window-maximum/

# Fixed size window problem


# Using monotonic decreasing queue (deque)
# The idea is enqueue only if the element is less than the element at the front of the queue


# Explanation: https://www.youtube.com/watch?v=DfljaUwZsOk
def sliding_window_maximum(nums, k):
    if k > len(nums) or k <= 0:
        return []

    max_sliding_window_outputs = []
    deque = []
    deque_max_value_index = None

    for windowEnd in range(len(nums)):
        if deque_max_value_index is None:
            deque.append(nums[windowEnd])
            deque_max_value_index = 0
        else:
            while len(deque) > deque_max_value_index and deque[-1] < nums[windowEnd]:
                deque.pop()
            else:
                deque.append(nums[windowEnd])
        if windowEnd >= k - 1:
            max_sliding_window_outputs.append(deque[deque_max_value_index])
            index = windowEnd - k + 1  # index to be removed from the window
            if deque[deque_max_value_index] == nums[index]:
                deque_max_value_index += 1

    return max_sliding_window_outputs


print(sliding_window_maximum([1, 3, -1, -3, 2, 3, 6, 7], 3))
print(sliding_window_maximum([1], 1))


# brute force approach


def sliding_window_maximum_brute(nums, k):
    if k > len(nums) or k <= 0:
        return []

    max_sliding_window = []
    current_window = []
    startIndex = 0

    for i in range(len(nums)):
        current_window.append(nums[i])
        if i >= k - 1:
            max_sliding_window.append(max(current_window[startIndex:]))
            startIndex += 1

    return max_sliding_window
