import speech_recognition
import asyncio

# function for submitting help request
def process_text(text, audio):
    print("DECODED TEXT: " + text)

    # Look for keyword
    if text.find("help") != -1:
        print("HELP REQUEST HAS BEEN SENT")
        # Connect to firebase

# Crate listen function
async def listen():
    # Set up recognizer
    recognizer = speech_recognition.Recognizer()

    while True:
        try:
            with speech_recognition.Microphone() as mic:

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic, phrase_time_limit = 5)

                text = recognizer.recognize_google(audio)
                text = text.lower()

            # Process input text (MIGHT NEED TO RM FOR ASYNC)
            process_text(text, audio)

        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()

# Create event loop
print("Starting event loop...")
loop = asyncio.get_event_loop()

try:
    asyncio.ensure_future(listen())
    loop.run_forever()

except KeyboardInterrupt:
    pass

finally:
    print("Closing loop")
    loop.close()
