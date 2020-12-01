# is anagram
# anagrams contain the same letter but in diffent orders
# Listen = Silent
# use dict to check values


s1 = "Listen"
s2 = "Silent"
def anagram(s1, s2):
    s1 = s1.lower()
    s1 = s1.replace(" ", "")
    s2 = s2.lower()
    s2 = s2.replace(" ", "")
    d1 = {}
    d2 = {}

    if len(s1) != len(s2):
        return False

    for i in s1:
        d1[i] = 1
    
    for i in s2:
        d2[i] = 1
        
    if d1 == d2:
        return True
    else:
        return False

print(anagram(s1, s2))