import random
from problem import Problem
import os
#programming overseen by Jake
#data for difficulties overseen by Cheryl

#class for handling word module, will include difficultly, problems, etc.

class Word(Problem):
  
  def __init__(self):
    super().__init__()
    self._words_by_difficulty = dict()
    self._word = ""
    self._words_in_level = []
    self.word_list = []
    self.create_list()


  def create_list(self):
    here = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(here, "word_list.txt")
    self.words = open(filename, 'r')
    for word in self.words.readlines():
      self.word_list.append(word[0:len(word) - 1])

     
  def setup_sentence(self):
    self._setup_dictionary()
    self._setup_difficulty()
    self._select_word()
    self._create_problem()

  def _select_word(self):
    """randomly selects word"""
    self._word = random.choice(self._words_in_level)

  def _create_problem(self):
    """sets the value for problem"""
    self.problem = self._word
    self._solution = self.problem
  
  def _setup_dictionary(self):
    """splits word list into a dictionary based on word length"""
  
    for word in self._words:
      length = len(word)
      temp_array = []
      if length in self._words_by_difficulty:
        temp_array = self._words_by_difficulty[length]
        temp_array.append(word)
        self._words_by_difficulty[length] = temp_array
      
      else:
        temp_array.append(word)
        self._words_by_difficulty[length] = temp_array
      
  
  def _setup_difficulty(self):
    """sets up the difficulty by finding how many total words there 
    are, and dividing them up roughly by how many letters they 
    contain"""

    # determine size of word array
    length = len(self._words)
    lengths_of_words =[]
    for key in self._words_by_difficulty:
      lengths_of_words.append(key)
    lengths_of_words.sort()

  # determine the number of words per level
    if length < 100:
      words_per_level = length // 5
    
    else:
      words_per_level = 10
    
    self._words_in_level = self._words_by_difficulty[lengths_of_words[self._difficulty]].copy()

    if len(self._words_in_level) < words_per_level:
      if self._difficulty < len(lengths_of_words) - 1:
        self._words_in_level += self._words_by_difficulty[lengths_of_words[self._difficulty + 1]]

      else:
        self._words_in_level += self._words_by_difficulty[lengths_of_words[self._difficulty - 1]]
      


  def get_word(self, difficulty):
      """Gets a random word from the list and returns it to director."""
      word = random.choice(self.word_list)
      if difficulty == "easy":
        while len(word) > 4:
          word = random.choice(self.word_list)
      if difficulty == "medium":
        while len(word) <= 3 and len(word) >= 7:
          word = random.choice(self.word_list)
      if difficulty == "hard":
        while len(word) < 4:
          word = random.choice(self.word_list)
      
      return word.lower()
    
list_words = [ "about", "above", "add", "after", "again", "against",
 "air", "all", "almost", "also", "always", "am", "America", "an", 
 "and", "animal", "another", "answer", "any", "are", "around", "as",
  "ask", "at", "away", "back", "be", "because", "become", "been", 
  "before", "began", "begin", "being", "below", "between", "big", 
  "book", "both", "boy", "but", "by", "call", "came", "can", "can", 
  "car", "carry", "change", "child", "children", "city", "close", 
  "come", "come", "consider", "could", "could", "country", "course", 
  "cut", "day", "develop", "did", "different", "do", "does", "down", 
  "during", "each", "early", "earth", "eat", "end", "enough", "even", 
  "every", "example", "eye", "face", "fact", "family", "far", "farm", 
  "father", "feel", "feet", "few", "find", "first", "follow", "food", 
  "for", "form", "found", "four", "from", "general", "get", "girl", 
  "give", "go", "good", "got", "govern", "great", "group", "grow", 
  "had", "hand", "hard", "has", "have", "he", "head", "hear", "help", 
  "her", "here", "high", "him", "his", "hold", "home", "house", 
  "how", "however", "idea", "if", "important", "in", "increase", 
  "interest", "into", "is", "it", "just", "keep", "kind", "know", 
  "know", "land", "large", "last", "late", "later", "lead", "learn", 
  "leave", "left", "let", "letter", "life", "light", "like", "line", 
  "list", "little", "live", "long", "look", "made", "make", "man", 
  "many", "may", "me", "mean", "men", "might", "mile", "miss", 
  "more", "most", "mother", "mountain", "move", "much", "must", "my", 
  "name", "nation", "near", "need", "never", "new", "next", "night", 
  "no", "not", "now", "number", "of", "off", "often", "old", "on", 
  "once", "one", "only", "open", "or", "order", "other", "our", 
  "out", "over", "own", "page", "paper", "part", "people", "person", 
  "picture", "place", "plan", "play", "point", "possible", "present", 
  "problem", "program", "public", "put", "read", "real", "really", 
  "right", "river", "run", "said", "same", "saw", "say", "school", 
  "sea", "second", "see", "seem", "seem", "sentence", "set", "she", 
  "should", "show", "side", "since", "small", "so", "some", 
  "something", "sometimes", "song", "soon", "sound", "spell", 
  "stand", "start", "state", "still", "stop", "story", "study", 
  "such", "system", "take", "talk", "tell", "than", "that", "the", 
  "their", "them", "then", "there", "these", "they", "thing", 
  "think", "this", "those", "thought", "three", "through", "time", 
  "time", "to", "together", "too", "took", "tree", "try", "turn", 
  "two", "under", "up", "us", "use", "very", "walk", "want", "was", 
  "watch", "water", "way", "we", "well", "went", "were", "what", 
  "when", "where", "which", "while", "white", "who", "why", "will", 
  "with", "without", "word", "work", "world", "would", "write", 
  "year", "you", "young", "your"]

  

''' 
while(True):      
  nouns = ["boy", "girl", "dog", "apple", "horse"]
  verbs = ["ran", "fought", "jumped"]
  prepositions = ["about", "above", "across", "after", "along",
          "around", "at", "before", "behind", "below",
          "beyond", "by", "despite", "except", "for",
          "from", "in", "into", "near", "of",
          "off", "on", "onto", "out", "over",
          "past", "to", "under", "with", "without"]

  articles = ["a", "the"]

  word = Word(nouns, verbs, prepositions, articles)

  word.setup_sentence()
  print(word.problem)
  solution = input("> ")
  print(word.check_solution(solution))
  '''
