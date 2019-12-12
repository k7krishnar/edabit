def count_vowels(txt):
    vowels=['a','e','i','o','u']
    count=0
    for i in txt:
        if i in vowels:
            count+=1
    print(count)

count_vowels('Celebration')

# other solution1
def count_vowels(txt):
  return sum([1 for x in txt.lower() if x in 'aeiou'])

# other solution2
import re

def countVowels(str):
	return len(re.findall(r'[aeiou]', str))

