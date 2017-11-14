#!/usr/bin/env python3

import speech_recognition as sr

# get audio from the microphone
r=sr.Recognizer()
with sr.Microphone() as source:
	print("Speak:")
	audio=r.listen(source)

try:
	f=open('speech2text.txt','w')
	f.write('{ "name": "' + r.recognize_google(audio)+'" }')
	f.close()
	print('{ "name": "' + r.recognize_google(audio)+'" }')
except sr.UnknownValueError:
	print("Could not understand audio")
except sr.RequestError as e:
	print("Could not request results; {0}".format(e))


# -*- coding: utf-8 -*-

import httplib, urllib
import json

uri = 'westcentralus.api.cognitive.microsoft.com'
path = '/text/analytics/v2.0/sentiment'

def GetSentiment (documents):
    "Gets the sentiments for a set of documents and returns the information."

    headers = {'Ocp-Apim-Subscription-Key': accessKey}
    conn = httplib.HTTPSConnection (uri)
    body = json.dumps (documents)
    conn.request ("POST", path, body, headers)
    response = conn.getresponse ()
    return response.read ()

f=open("speech2text.txt","r")

documents = { 'documents': [
    { 'id': '1', 'language': 'en', 'text': f.read()}
]}

f.close()

print 'Please wait a moment for the results to appear.\n'

result = GetSentiment (documents)
print (json.dumps(json.loads(result), indent=4))




# Import the required module for text 
# to speech conversion
from gtts import gTTS
 
# This module is imported so that we can 
# play the converted audio
import os
 
# The text that you want to convert to audio
f=open("speech2text.txt","r")
mytext = 'Thank you for your response! have a nice day!!'
 
# Language in which you want to convert
language = 'en'
 
# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)
 
# Saving the converted audio in a mp3 file named
# welcome 
myobj.save("welcome.mp3")
 
# Playing the converted file
os.system("mpg321 welcome.mp3")
f.close()
