import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os
from translate import Translator
import requests

crypto_api = "https://api.coindesk.com/v1/bpi/currentprice.json"


def translator(text):
    translator= Translator(to_lang="German")
    alina_talk_de(translator.translate(text))

def bitcoin():
   
    # URL to fetch the Bitcoin price
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"

    # Fetch data from the URL
    response = requests.get(url)
    data = response.json()

    # Extract the Bitcoin price in USD
    btc_price_usd = data['bpi']['USD']['rate']

    return btc_price_usd 
        
def alina_listen():
    
    rec = sr.Recognizer()

    with sr.Microphone() as source:
        audio = rec.listen(source)
        text = ''
        # text = rec.recognize_google(audio)
        # text = text.lower()
        # print(f" you said {text}")

    try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_alina_talk_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
        text = rec.recognize_google(audio)
    except sr.UnknownValueError:
        print("Google alina_talk Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google alina_talk Recognition service; {0}".format(e))
    
    text = text.lower()
    return text


def alina_talk(text):
    #create audio file
    file_name = "audio_data.mp3"
    #convert test to alina_talk
    tts= gTTS(text=text, lang='en', slow=False)
    #save file
    tts.save(file_name)
    #play file
    playsound(file_name)
    #remove file
    os.remove(file_name)

def alina_talk_de(text):
    #create audio file
    file_name = "audio_data.mp3"
    #convert test to alina_talk
    tts= gTTS(text=text, lang='de')
    #save file
    tts.save(file_name)
    #play file
    playsound(file_name)
    #remove file
    os.remove(file_name)
    
def alina_reply(text):
    if 'what' in text and 'name' in text:
        alina_talk("My name is Alina and I am your personal assistant")
    elif "why" in text and 'exist' in text:
        alina_talk("I was created to work for you")

    elif "translate" in text:
        alina_talk('Sure, what do you need me to translte?')
        while True:
            text_to_translate= alina_listen()
            if text_to_translate != 'turn off translator':
                translator(text_to_translate)
            else:
                alina_talk('the translator will be turned off .. What else I can do for you?')
    elif "bitcoin" in text:
        price =bitcoin()
        alina_talk("the current price for a Bitcoin is" + price +"US Dollars")
    elif 'stop' in text:
        alina_talk('I was a pleasure to help you, I wish you a wonderful day')
    else:
        alina_talk('Excuse me, I did not get that, Can you please repeat it?')

        
def execute_assistant():
    alina_talk('Hi, I am here to support you. Can you please tell me your name')
    listen_name = alina_listen()
    alina_talk("Hi" + listen_name + 'what can I do for you?')


    while True:
        listen_alina = alina_listen()
        print(listen_alina)
        alina_reply(listen_alina)

        if 'stop' in listen_alina:
            break

execute_assistant()
