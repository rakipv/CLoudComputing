import os
import io
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] ="C:/Python310/qwiklabs-gcp-00-63c4ce86d292-202362401176.json"
from google.cloud import translate_v2 as translate
translate_client=translate.Client()

Lang_list=translate_client.get_languages()
for language in Lang_list:
    print(u"{name} {{languages}}".format(**language))


text=" hi hello how are you "
target='ml'
model='base'
ouput=translate_client.translate( text ,target_language=target ,model=model)
print(u" text: {} ".format( ouput["input"]))
print(u"translation {}".format(ouput["translatedText"]))
    
    
