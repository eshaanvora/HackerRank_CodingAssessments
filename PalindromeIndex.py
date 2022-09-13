#Given a string of lowercase letters in the range ascii[a-z],
#determine the index of a character that can be removed to make the string a palindrome.

#The following string can become a palindrome, if we remove the char at the 0 and 3 index
s = "bcbc"


counter = 0
for i in range(len(s)):
  newString = s[:i] + s[i+1:]
  palindrome = newString[::-1]
  if palindrome == newString:
      print(counter)
  counter += 1
