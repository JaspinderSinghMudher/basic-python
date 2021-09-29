import re
from bs4 import BeautifulSoup
import requests
from gtts import gTTS
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
word_list = audio_text.split()
number_of_words = len(word_list)
print('Please wait while we are converting ' + str(number_of_words) +' words into Audio ..' )
#file_input_defult = f'{soup.title.text}.mp3'
file_input_defult = f'{soup.title.text}.mp3'
#print(audio_text)
audio = gTTS(text=audio_text,lang='en',slow=False)
audio.save( f"\'"+file_input_defult)
print(f'File stored in \'{file_input_defult}\'')
print('Done!! Your Audio has been created.! ')