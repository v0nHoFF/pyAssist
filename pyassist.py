import os
import time
import playsound
import speech_recognition as sr
import platform
from gtts import gTTS

SYSTEM = platform.system()

def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)

def shutdown(sys):
	if sys == "Windows":
		os.system("shutdown -s -t 1 -f")
	elif sys == "Linux":
		os.system("poweroff")
	elif sys == "Darwin":
		os.system("sudo shutdown")

def sleep(sys):
	if sys == "Windows":
		os.system("powercfg -hibernate off")
		os.system("%windir%\System32\rundll32.exe powrprof.dll,SetSuspendState")
	elif sys == "Linux":
		os.system("systemctl suspend")
	elif sys == "Darwin":
		os.system("pmset sleepnow")

def reboot(sys):
	if sys == "Windows":
		os.system("shutdown /r")
	elif sys == "Linux":
		os.system("reboot now")
	elif sys == "Darwin":
		os.system("sudo shutdown -r now")

def get_audio():
	global SYSTEM
	r = sr.Recognizer()
	with sr.Microphone() as source:
		audio = r.listen(source)
		said = ""
		try:
			said = r.recognize_google(audio)
			action(said)
		except Exception as e:
			print("exception" + str(e))

def action(command):
	if command == "shutdown":
		speak("shutting down")
		shutdown(SYSTEM)
	elif command == "shut down":
		speak("shutting down")
		shutdown(SYSTEM)
	elif command == "sleep":
		speak("sleeping now")
		sleep(SYSTEM)
	elif command == "restart":
		speak("rebooting")
		reboot(SYSTEM)
	elif command == "reboot":
		speak("rebooting")
		reboot(SYSTEM)


def start():
	while True:
		get_audio()

if __name__ == "__main__":
    speak("hello")
    get_audio()
