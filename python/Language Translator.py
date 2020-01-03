# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 13:29:30 2019

@author: Ravi
"""


#Language Translator
from translate import Translator
t=Translator(from_lang='en',to_lang='hi')
translation=t.translate("I love machine learning")

print(translation,type(translation))

#gtts
from gtts import gTTS
from translate import Translator
z=Translator(from_lang='en',to_lang='hi')

mytext='Welcome to Delhi'
translation=z.translate(mytext)

language='en'
"""
danish da
french fr
german de
italian it

japan jp korean ko polish pl turkish tr
https://cloud.google.com/text-to-speech/docs/voices
"""
myobj=gTTS(text=translation,lang=language,slow=False)
myobj.save('welcome113.mp3')


from translate import Translator
from gtts import gTTS
t=Translator(from_lang='eng',to_lang='hi')
translation=t.translate("Hello to the world")
print(translation,type(translation))
language='en'
w=gTTS(text=translation,lang=language,slow=False)
w.save("welcome113.mp")



#practice

from translate import Translator
from gtts import gTTS
mytext='Welcome to Delhi'
t=Translator(from_lang='en',to_lang='hi')
translation=t.translate(mytext)

language='en'
w=gTTS(translation,lang=language,slow=False)
w.save("welcome113.mp")



#pratice

from translate import Translator
from gtts import gTTS
mytext="Welcome to India"
t=Translator(from_lang="en",to_lang="hi")
translation=t.translate (mytext)
print(translation)

language="en"

w=gTTS(translation,lang=language,slow=False)
w.save("113.mp")

























