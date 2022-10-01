from gtts import gTTS
import os
file = open(&quot;abc.txt&quot;, &quot;r&quot;).read()
speech = gTTS(text=file, lang=&#39;en&#39;, slow=False)
speech.save(&quot;voice.mp3&quot;)
os.system(&quot;voice.mp3&quot;)
print(file)