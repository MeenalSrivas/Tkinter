<<<<<<< HEAD
import win32com.client as wincom

# you can  also insert gaps in the narration by adding sleep call

speak = wincom.Dispatch("SAPI.SpVoice")
while True:
    text = input("enter your text:")
    speak.Speak(text)
    if text=="busy":
        speak.Speak("bye")



=======
import win32com.client as wincom

# you can  also insert gaps in the narration by adding sleep call

speak = wincom.Dispatch("SAPI.SpVoice")
while True:
    text = input("enter your text:")
    speak.Speak(text)
    if text=="busy":
        speak.Speak("bye")



>>>>>>> c9620fbf3a4515d86fcebd2f69f58b69fe37309f
