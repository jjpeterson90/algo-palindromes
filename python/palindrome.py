import re

def palindrome(word):
    word = re.sub('\W', '', str(word).lower())
    
    def test_palindrome(word):
        if len(word) < 2:
            return True
        if word[0] == word[len(word)-1]:
            reduced_word = word.replace(word[0], '')
            return test_palindrome(reduced_word)
        else:
            return False
        
    return test_palindrome(word)
    
#print(palindrome('Race car'))
#print(palindrome('12321'))