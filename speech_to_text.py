import speech_recognition as sr
import matplotlib.pyplot as plt
import numpy as np
import wave
import sys

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Anything :")
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("You said : {}".format(text))

        # write audio to a WAV file
        with open("microphone-results.wav", "wb") as f:
            f.write(audio.get_wav_data())

        spf = wave.open('microphone-results.wav','r')

        #Extract Raw Audio from Wav File
        signal = spf.readframes(-1)
        signal = np.fromstring(signal, 'Int16')


        #If Stereo
        if spf.getnchannels() == 2:
            print ('Just mono files')
            sys.exit(0)

        plt.figure(1)
        plt.title('Signal Wave...')
        plt.plot(signal)
        plt.show()

    except:
        print("Sorry could not recognize what you said")
