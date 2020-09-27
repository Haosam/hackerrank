import re

vowel = 'aeiou'
consonant = "qwrtypsdfghjklzxcvbnm"

match = re.findall(r'(?<=['+consonant+'])(['+vowel+']{2,})(?=['+consonant+'])',input(),flags = re.I)

print('\n'.join(match or['-1']))
