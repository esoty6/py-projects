from collections import Counter


def palindrome_permutation(s: str) -> bool:
    char_counts = Counter(c.lower() for c in s if c != ' ')
    return sum(count % 2 for count in char_counts.values()) <= 1
    
    
print(palindrome_permutation('tact coa'))
print(palindrome_permutation('abba'))
print(palindrome_permutation('tact coazc'))
    