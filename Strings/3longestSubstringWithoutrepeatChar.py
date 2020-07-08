"""
LeetCode question 3. Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.

Solution walk through:
We can utilise the sliding window technique:

1. We'll have two pointers, start and end to represent the start and the end of our window respectively. We'll also have
    a current_window_len which shall denote the len of current window
2. We'll also have a dict data stracture, cache, which shall hold the characters we've seen and the number of times
    we've seen it

3. As we are moving pointer end, when we get to a char that we've already encountered, we get the difference between start and end
    The difference represents the number of characters in our window(The window contains non-repeating chars)
    We then find the max of the new diff/len of window and the previous diff/len of window.
    We'll then contract our window

Example

"a b c a b c b b"   "dvdf" "dacabcd" "babbcfg" "abddddaobbqwert"
 0 1 2 3 4 5 6 7

 step 1. both end and start pointers are pointing at char in index 0
    Add char a to cache {a:1}
    Increament end pointer end +=1   end=1
    increament current_window_len += 1  current_window_len=1

2. end now points at char b at index 1
    Check if the char is in cache. if not Add b to cache {a:1, b:1}
    Icreament end += 1 end 2
    increament current_window_len += 1 current_window_len=2

3. check if char c at index 2 is in cache
    Add in cache {a:1, b:1, c:1}
    Icreament end += 1 end 3
    increament current_window_len += 1 current_window_len=3

4. Check if char a at index 3 in cache
    if present: Find diff/ len of current window  end-start = 3-0 = 3
    find max(previous_len, current_len)
    Then contract window start += 1 start=1

"""
class Solution:
    def lengthOfLongestSubstring(self, s):

        # base case 
        if not s:
            return 0

        cache = {} # shall hold the char we've seen
        start = 0 # start of window
        end = 0 # end of window
        window_len = 0 # len of window/ number of characters in window
        max_window_len = 0 # len of the largest window that we've created

        while end < len(s): # this shall be our terminating condition
            # check if char at current end index is in cache and it's previous index is within our window
            if s[end] in cache and cache[s[end]] >= start:
                #1. find the number of char in current window: current window is denoted by where the indexe duplicate
                # cache[s[end]] will return the index of the previous encounter of the char currently at index end
                window_len  = end-cache[s[end]]
                start = cache[s[end]] + 1 # the start of the new window will be one step infront of the index of the previous encounter of the character
                # we have to update where we've encountered this current repeating char
                cache[s[end]] = end

        
            else:
                # if not add it to the cache
                cache[s[end]] = end # the value is the index where it was found
                #increament the current window len since this is a new character we've encountered
                window_len += 1
                # get max
                max_window_len = max(window_len, max_window_len) # the max between the current window and previously considered max windows

            # expand window
            end += 1 

        return max_window_len
                