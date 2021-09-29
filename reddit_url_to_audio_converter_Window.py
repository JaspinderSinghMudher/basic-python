import re
from bs4 import BeautifulSoup
import requests
import gtts
#pip install gtts-token
try:
    global uin
    uin = input('Enter Reddit url :- ')
    if 'https://www.reddit.com' in uin:
        pass
    else:
        print('Please Use proper Reddit url (eg:- https://www.reddit.com )')
        exit()
except KeyboardInterrupt:
    pass
response = requests.get(uin, headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 Chrome/83.0.4103.97 Safari/537.36"})
soup = BeautifulSoup(str(response.text),'html.parser')
divs = soup.find_all('div')
audio_text = ''
for div in divs:
    try:
        if str(div.attrs['class'][1]) == str('RichTextJSON-root') and str(div.attrs['style']) == str('color:#1A1A1B'):
            try:
                for p in div.find_all('p'):
                    try:
                        story = p.text
                        for string in story:
                            audio_text = audio_text + string    
                    except KeyboardInterrupt:
                        pass
            except KeyboardInterrupt:
                pass
            break
    except KeyError:
        pass 
    except IndexError:
        pass
audio_text = audio_text + f'\nThanks for Listening this story is available in Reddit as {soup.title.text}'
print(f'CREATING AUDIO OF \"{soup.title.text}\"')
file_name = re.findall('(.*):', str(soup.title.text))
#print(file_name)
word_list = audio_text.split()
number_of_words = len(word_list)
print("Please wait While we convert",number_of_words,"into audio.....")
tts = gtts.gTTS(audio_text)
tts.save(file_name[0]+".wav")
#playsound("hello.mp3")
