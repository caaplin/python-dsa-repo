text = "  Python Programming  "

cleaned = text.strip()
first_word = cleaned[:6]
last_word = cleaned[7:]
reversed_text = cleaned[::-1]
uppercase_text = "".join(
    character.upper() for character in cleaned
)
vowels = "".join(
    character for character in cleaned
    if character.lower() in "aeiou"
)

print("Original:", repr(text))
print("Cleaned:", cleaned)
print("First word:", first_word)
print("Last word:", last_word)
print("Reversed:", reversed_text)
print("Uppercase:", uppercase_text)
print("Vowels:", vowels)

# Expected output:
# Original: '  Python Programming  '
# Cleaned: Python Programming
# First word: Python
# Last word: Programming
# Reversed: gnimmargorP nohtyP
# Uppercase: PYTHON PROGRAMMING
# Vowels: oooai

