class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words_array = []
        word = ""
        for char in s:
            if char != " ":
                word += char
            elif word:
                words_array.append(word)
                word = ""
        # After the loop, if there's still a word left add it to the array 
        if word:
            words_array.append(word)
        if words_array:
            return len(words_array[-1])
        else:
            return 0

s = "Hello World "
solution = Solution()
print(solution.lengthOfLastWord(s))  