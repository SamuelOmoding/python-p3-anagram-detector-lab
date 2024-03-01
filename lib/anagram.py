# your code goes here!
class Anagram:
    def __init__(self, word):
        # Initialize the Anagram object with a word and store its sorted version
        self.word = word
        self.sorted_word = sorted(word)
        
    def match(self, possible_anagrams):
        # Initialize a list to store matching anagrams
        matches = []
        for possible_anagram in possible_anagrams:
           # Check if the current possible anagram is an anagram of the word
            if self.is_anagram(possible_anagram):
                # If it is, add it to the matches list
                matches.append(possible_anagram)
        return(matches)
        
    def is_anagram(self, possible_anagram):
         # Check if the sorted characters of the possible anagram match the sorted word
        return sorted(possible_anagram) == self.sorted_word
    
# Create an instance of Anagram with the word "listen"
listen = Anagram("listen")
# Define a list of possible anagrams
possible_anagrams = ['enlists', 'google', 'inlets', 'banana']
# Find matches for the word "listen" among the possible anagrams
matches = listen.match(possible_anagrams)    
#Print the number of matches and the matches themselves
print(f"Found {len(matches)} match(es) for '{listen.word}': {matches}")    