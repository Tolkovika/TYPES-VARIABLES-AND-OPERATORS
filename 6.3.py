###
# A program that prints a university abbreviation
#   
university = "Krakow University of Economics"
words = university.split()
skip_words = {"of"}
abbreviation = ''.join([word[0].upper() for word in words if word.lower() not in skip_words])
print(abbreviation)