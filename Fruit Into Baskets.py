class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        char_freq={}
        w_start=0
        max_length=0
        for w_end in range(len(fruits)):
            right_char=fruits[w_end]
            if right_char not in char_freq:
                char_freq[right_char]=0
            char_freq[right_char]+=1
            while len(char_freq)>2:
                left_char=fruits[w_start]
                char_freq[left_char]-=1
                if char_freq[left_char]==0:
                    del char_freq[left_char]
                w_start+=1
            max_length=max(max_length,w_end-w_start+1)
        return max_length