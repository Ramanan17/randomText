import random

# Createe a function that will take no arguments. The purpose of the function is to generate a random word from a list of five words that you make up.   Return the random word to the caller.
def getRandomWord():
  # return random word from list of five words
 return random.choice(["sentence","the","which","put","no"])

# Createe a second function which will take one string argument.  The purpose of the function is to search the text file created in step one, and determine how many occurrences of the argument passed into the function occur in the file. Return the number of occurrences to the caller along with the word "high", "medium" , "low" or "none" based upon the number of hits received-  0 = none, 1-5 low, 6-10 medium, 11+ high
def getnumOccurences(string):
  # Open the file
  with open("words.txt") as f:
    # get the list of wors
    words = list(map(lambda x:x.replace("\n",""),f.readlines()))
    # Get the number of occurences
    numOccurences = len(list(filter(lambda word:word==string,words)))
    # return result with appropriate message
    if numOccurences==0:
      return (numOccurences,"none")
    elif 1<=numOccurences<=5:
      return (numOccurences,"low")
    elif 6<=numOccurences<=10:
      return (numOccurences,"medium")
    elif numOccurences>11:
      return (numOccurences,"high")

# 4            Writee a script which will call the appropriate methods to find how many occurrences of a random word occurs in the text file. Print out the number of occurrences and keyword (with an appropriate message) along with the length of time it took to complete the search - with an appropriate message.

if __name__=="__main__":
  # get random word
  random_word = getRandomWord()
  # measure time
  import time
  start = time.time()
  # get occurence and msg
  numOccurences,msg = getnumOccurences(random_word)
  end = time.time()-start
  # print the result
  print(f"Number of Occurences of random word '{random_word}': {numOccurences}-{msg}")
  print(f"Time taken to complete the search {end:.6f}s")
  
  
    
  