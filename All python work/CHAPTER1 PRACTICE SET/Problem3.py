import pyttsx3
# Initialize the TTS engine
engine = pyttsx3.init()
# Convert text to speech
engine.say("Ap kesay ho")
# Wait for the speech to finish
engine.runAndWait()