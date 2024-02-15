def is_anagram(word1, word2):
 return sorted(word1) == sorted(word2)

word1=input()
word2=input()

if is_anagram(word1,word2):
 print("YES")
else:
 print("NO")