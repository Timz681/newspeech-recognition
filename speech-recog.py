import streamlit as st
import speech_recognition as sr

# Set page title and configure layout
st.set_page_config(page_title="Speech Recognition App", layout="wide")

# Set page header with speech recognition title
st.markdown("<h1 style='text-align: center;'>Speech Recognition App</h1>", unsafe_allow_html=True)

def transcribe_speech(recognizer, audio):
    try:
        text = recognizer.recognize_google(audio, show_all=False)  # Change the speech recognition API here
        return text
    except sr.UnknownValueError:
        return "Speech Recognition could not understand audio"
    except sr.RequestError as e:
        return f"Error: Could not connect to the speech recognition service. {e}"

def save_transcribed_text(text):
    # Add your code here to save the transcribed text to a file
    pass

# Set up the speech recognizer
r = sr.Recognizer()

# Add an option for users to select the speech recognition API
speech_recognition_api = st.selectbox("Select Speech Recognition API", ["Google Speech Recognition", "Other APIs"])

# Configure the speech recognition API based on the selected option
if speech_recognition_api == "Google Speech Recognition":
    recognizer = sr.Recognizer()
else:
    # Add your code here to configure other speech recognition APIs
    recognizer = None  # Replace None with the appropriate speech recognition API

# Add an option for users to select the language they are speaking in
language = st.selectbox("Select Language", ["English", "Spanish", "French"])

# Set the language for the speech recognition API
if language == "English":
    recognizer.energy_threshold = 4000
elif language == "Spanish":
    recognizer.energy_threshold = 5000
elif language == "French":
    recognizer.energy_threshold = 6000

# Add a button to start and stop the speech recognition process
if st.button("Start Speech Recognition"):
    with sr.Microphone(device_index=0) as source:

        st.markdown("<h3 style='text-align: center;'>Listening...</h3>", unsafe_allow_html=True)

        # Use a loop to continuously listen for speech and transcribe it
        while True:
            audio = r.listen(source)

            # Add a feature to allow the user to pause and resume the speech recognition process
            if st.button("Pause"):
                st.markdown("<h3 style='text-align: center;'>Speech Recognition Paused</h3>", unsafe_allow_html=True)
                break

            text = transcribe_speech(recognizer, audio)
            st.write("Transcribed Text:", text)

            # Add a feature to allow the user to save the transcribed text to a file
            if st.button("Save"):
                save_transcribed_text(text)
                st.markdown("<h3 style='text-align: center;'>Transcribed Text Saved</h3>", unsafe_allow_html=True)

            # Break the loop if the speech recognition is complete
            if text:
                break
