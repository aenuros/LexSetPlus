import nltk
import re
# nltk.download('punkt')
# nltk.download('cmudict')

from nltk.tokenize import word_tokenize, sent_tokenize, WhitespaceTokenizer

arpabet = nltk.corpus.cmudict.dict()

text2 = '''Well, since my baby left me
Well, I found a new place to dwell
Well, it's down at the end of Lonely Street
At Heartbreak Hotel

Where I'll be, I'll be so lonely baby
Well, I'm so lonely
I'll be so lonely, I could die

Although it's always crowded
You still can find some room
For broken-hearted lovers
To cry there in their gloom

They'll be so, they'll be so lonely baby
They get so lonely
They're so lonely, they could die

Now, the bell hop's tears keep flowin'
And the desk clerk's dressed in black
Well, they've been so long on Lonely Street
They'll never, never look back

And they get so, they get so lonely baby
Well they are so lonely
They're so lonely, they could die

Well, now, if your baby leaves you
And you got a tale to tell
Well, just take a walk down Lonely Street
To Heartbreak Hotel

Where you will be, you will be so lonely baby
Well you will be lonely
You'll be so lonely, you could die

Although it's always crowded
But you still can find some room
For broken-hearted lovers to cry there in their gloom

Where they get so, they get so lonely baby
Well they're so lonely
They'll be so lonely, they could die
'''


# tokens = [word for sent in sent_tokenize(text) for word in word_tokenize(sent)]

def countLexicalSet(lexicalSet, myText, printWord):
  tk = WhitespaceTokenizer()
  phonemeCount = 0
  sentenceCount = 0
  # remove all punctuation
  cleanedText = re.sub("[,()?!]","",myText)
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






countLexicalSet('AY', text2, False)

print("------------------")

# countPhonetic('[a]', text)

print("------------------")

# print(createFullArpabetString(text2))

# TODO : convert full arpabet string back to an array?
