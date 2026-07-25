class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dict1 = {}
        i=0
        j=0
        count = 0
        mcount = 0
        while j < len(s):
            if s[j] in dict1:
                dict1[s[j]] +=1
            else:
                dict1[s[j]] = 1
            max1 = max(dict1.values())
            clen = j - i + 1

            if clen - max1 > k:
                dict1[s[i]] -=1
                i+=1
            else:
                count = j - i + 1
                if count > mcount: 
                    mcount = count
            j+=1
        return mcount
        