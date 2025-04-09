#Using recursion write a program that removes repeated duplicate values in a string.  Example AABBCCCDEFF -> ABCDEF Aleex -> Alex Hello ->
def RemoveDuplicates (s):
 if len(s) <= 1:
    return s
 if s[0] == s[1]:
    return RemoveDuplicates(s[1:])
 else: 
    return s[0] + RemoveDuplicates(s[1:])

    ABCDEFF
print (RemoveDuplicates("AABBCCCDEFF")) 
print (RemoveDuplicates("Aleex"))    
print (RemoveDuplicates("THIIISWOOORRKSSS")) 
print (RemoveDuplicates("111111223333345555567777889")) 
