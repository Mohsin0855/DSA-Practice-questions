from collections import Counter
def is_Anagram(s1,s2):
    clean_s1 = s1.replace(' ','').lower()
    clean_s2 = s2.replace(' ','').lower()
    return Counter(clean_s1) == Counter(clean_s2)

print(is_Anagram("silent", "listen"))

# other method

def anagram(s1,s2):
    clean_s1 = s1.replace(' ','').lower()
    clean_s2 = s2.replace(' ','').lower()
    return sorted(clean_s1) == sorted(clean_s2)


print(anagram("hello", "olleh"))