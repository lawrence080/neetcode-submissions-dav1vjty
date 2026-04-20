class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for i in s.lower():
            if ord(i) >=97 and ord(i)<=122 or ord(i)>=48 and ord(i)<=57:
                string+=i
        string = string.lower()
        tail = len(string)-1
        for i in range(len(string)):
            if string[i] != string[tail-i]:
                print(string[i]+" "+string[tail-i])
                return False
        return True