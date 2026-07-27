class Solution:
    def isValid(self, s: str) -> bool:
        stack1 = []
        for i in range (0,len(s)):
            if s[i] in "{[(":
                stack1.append(s[i])
                print(stack1)
            elif s[i] in "}])":
                if len(stack1) == 0:
                    return False
                top = stack1.pop()
                
                if s[i] == ")" and top !="(":
                    return False
                elif s[i] == "]" and top !="[":
                    return False
                elif s[i] == "}" and top !="{":
                    return False
        if len(stack1) == 0:
            return True
        else:
            return False
        