import nltk
import re
# nltk.download('punkt')
# nltk.download('cmudict')

from nltk.tokenize import word_tokenize, sent_tokenize, WhitespaceTokenizer

arpabet = nltk.corpus.cmudict.dict()

text2 = '''Hey!  Life, look at me, I can see the reality,
'Cause when you shook me, took me outta my world, I woke up.
Suddenly I just woke up to The Happening.
When you find that you left the future behind.
'Cause when you got a tender love you don't take care of, 
then you better beware of,
 
The Happening.
One day you're up, when you turn around,
You find your world is tumbling down.
It happened to me and it can happen to you.
 
I was sure, I felt secure until love took a detour.
Yeah!  Riding high on top of the world, it happened.
Suddenly it just happened, 
I saw my dreams torn apart 
when love walked away from my heart.
And when you lose a precious love you need to guide you 
something happens inside you,
 
The Happening.
Now I see life for what it is.
It's not of dreams, it's not of bliss.
It happened to me and it can happen to you
And then it happened.
Oo, and then it happened.
Oo, and then it happened.
 
Is it real?  Is it fake?
Is this game of life a mistake?
'Cause when I lost the love I thought was mine for certain,
Suddenly it starts hurting.
I saw the light too late when that fickle finger of fate.
Yeah!  It came and broke my pretty balloon,
I woke up, suddenly I just woke up, so sure,
I felt secure until love took a detour.
'Cause when you got a tender love you don't take care of,
then you better beware of,
The Happening.
The Happening.
'''


# tokens = [word for sent in sent_tokenize(text) for word in word_tokenize(sent)]

def countLexicalSet(lexicalSet, myText, printWord):
  tk = WhitespaceTokenizer()
  phonemeCount = 0
  sentenceCount = 0
  # remove all punctuation
  cleanedText = re.sub("[,()?!]","", myText)
  for sentence in cleanedText.splitlines():
    sentenceCount += 1
    wordCount = 0
    # words = word_tokenize(sentence)
    words = tk.tokenize(sentence)
    for word in words:
      wordCount += 1
      try:
        arpWord = ' '.join(arpabet[word.lower()][0])
        if lexicalSet in arpWord:
          phonemeCount += 1
          if printWord:
            print("line number: ", sentenceCount, "word num: ", wordCount, word, arpWord)
      except Exception as e:
        print ("^^^", e)
  print("Total ''" + lexicalSet + "'' count: ", phonemeCount)

def countPhonetic(phoneticString, myText):
  phoneticCount = 0
  lineCounter = 0
  for sentence in myText.splitlines():
    wordCounter = 0
    lineCounter += 1
    words = sentence.split()
    for word in words:
      wordCounter += 1
      if phoneticString in word:
        phoneticCount += 1
        print("line number: ", lineCounter, "word num: ", wordCounter, word)
  print("Total count of ", phoneticString, ": ", phoneticCount)
      

def convertToArpabetArray(myText):
  sentenceList = []
  tk = WhitespaceTokenizer()
  # remove all punctuation
  cleanedText = re.sub("[,()?!]","",myText)
  for sentence in cleanedText.splitlines():
    wordList = []
    words = tk.tokenize(sentence)
    for word in words:
      try:
        arpWord = '_'.join(arpabet[word.lower()][0])
        wordList.append(arpWord)
      except Exception as e:
        errorWord = "*" + word
        wordList.append(errorWord)
    sentenceList.append(wordList)
  return sentenceList

def createFullArpabetString(myText):
  sentList = convertToArpabetArray(myText)
  newSentenceList = []
  for sentence in sentList:
    wordList = []
    for word in sentence:
      wordList.append(word)
    newSentence = " ".join(wordList)
    newSentenceList.append(newSentence)
  fullArpabetText = "\n".join(newSentenceList)
  return fullArpabetText


# countLexicalSet('AY', text2, True)

print("------------------")

# countPhonetic('[a]', text)

print("------------------")

# print(createFullArpabetString(text2))

# TODO : convert full arpabet string back to an array?

def addBrackets(lexicalSet, myText):
  tk = WhitespaceTokenizer()
  newSentenceList = []
  # remove all punctuation
  cleanedText = re.sub("[.,()?!\"]","", myText)
  for sentence in cleanedText.splitlines():
    wordCount = 0
    # words = word_tokenize(sentence)
    words = tk.tokenize(sentence)
    wordList = []
    for word in words:
      wordToAppend = word
      try:
        arpWord = ' '.join(arpabet[word.lower()][0])
        for lex in lexicalSet:
          if lex in arpWord:
            wordToAppend = "[" + word + "]"
      except Exception as e:
        print("^^^", e)
      wordList.append(wordToAppend)
    newSentence = " ".join(wordList)
    newSentenceList.append(newSentence)
  fullBracketText = "\n".join(newSentenceList)
  return fullBracketText

print(addBrackets(['AY','IY0'], text2))
