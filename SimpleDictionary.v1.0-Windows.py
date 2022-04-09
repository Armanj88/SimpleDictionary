'''
test link is: https://api.dictionaryapi.dev/api/v2/entries/en/hello

the main api link is: https://api.dictionaryapi.dev/api/v2/entries/en/<word>

author: Arman Jamshidi
'''

import requests as rs
import os
os.system("cls")

while 1:
    user_url = input('Type the word: ')
    if user_url == "exit()":
        exit()
    url = 'https://api.dictionaryapi.dev/api/v2/entries/en/{}'.format(user_url)
    os.system("cls")
    response = rs.get(url)
    audio_phonetics = None
    
    try:
      word = user_url
    except:
      word = response.json()[0]['word']
    if word == user_url:
      try:
        audio_phonetics = response.json()[0]['phonetics'][0]['audio']
      except:
        type(audio_phonetics) == type(None)
      # pronunciation = response.json()[0]['phonetics'][1]['text']
      # print("word:" , word)
      # print("audio of phonetics:", audio_phonetics)
      # input("")
      print("Word:", word)
      print("Audio phonetics:", audio_phonetics)
      try:
        print("Meanings:")
        for i in response.json()[0]['meanings']:
          partOfSpeech = i['partOfSpeech']
          definition = i['definitions'][0]['definition']
          # example = i['definitions'][0]['example']
          # print(f"\tPart Of Speech: {partOfSpeech}\n\tDefinition: {definition}\n\tExample: {example}")
          print(
              f"\tPart Of Speech: {partOfSpeech}\n\tDefinition: {definition}")
          print('')
      except:
        pass
      
      print("json link:", url)
    input("- ")
    os.system("cls")

'''
example clean json:


[
    {
      "word": "hello",
      "phonetic": "həˈləʊ",
      "phonetics": [
        {
          "text": "həˈləʊ",
          "audio": "//ssl.gstatic.com/dictionary/static/sounds/20200429/hello--_gb_1.mp3"
        },
        {
          "text": "hɛˈləʊ"
        }
      ],
      "origin": "early 19th century: variant of earlier hollo ; related to holla.",
      "meanings": [
        {
          "partOfSpeech": "exclamation",
          "definitions": [
            {
              "definition": "used as a greeting or to begin a phone conversation.",
              "example": "hello there, Katie!",
              "synonyms": [],
              "antonyms": []
            }
          ]
        },
        {
          "partOfSpeech": "noun",
          "definitions": [
            {
              "definition": "an utterance of ‘hello’; a greeting.",
              "example": "she was getting polite nods and hellos from people",
              "synonyms": [],
              "antonyms": []
            }
          ]
        },
        {
          "partOfSpeech": "verb",
          "definitions": [
            {
              "definition": "say or shout ‘hello’.",
              "example": "I pressed the phone button and helloed",
              "synonyms": [],
              "antonyms": []
            }
          ]
        }
      ]
    }
]
'''
