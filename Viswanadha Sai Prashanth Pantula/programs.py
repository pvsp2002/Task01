def is_palindrome(text):
    clean_text = ''.join(char.lower() for char in text if char.isalnum())
    return clean_text == clean_text[::-1]

def is_anagram(str1, str2):
    clean_str1 = sorted(str1.replace(' ', '').lower())
    clean_str2 = sorted(str2.replace(' ', '').lower())
    return clean_str1 == clean_str2

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(is_palindrome("madam"))
print(is_anagram("listen","silent"))
print(is_prime(37))