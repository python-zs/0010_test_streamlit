""" Audio to text converter """
import streamlit as st
from pydub import AudioSegment, silence
import speech_recognition as sr

st.title("Audio to text converter")

# upload audio file
audio_file = st.file_uploader("Upload Audio", type=["wav", "mp3"])

# check if audio file is uploaded
if audio_file is not None:

    # show audio file for user to check if correct file is uploaded
    st.audio(audio_file, format='audio/wav')

    # split audio file into chunks
    audio_segment = AudioSegment.from_file(audio_file, format="wav")
    audio_chunks = silence.split_on_silence(
        audio_segment,
        min_silence_len=500,
        silence_thresh=audio_segment.dBFS-30
    )
    # export audio chunks as wav files
    for i, chunk in enumerate(audio_chunks):
        out_file = f"chunk{i}.wav"
        print("exporting", out_file)
        chunk.export(out_file, format="wav")

    # convert audio to text
    r = sr.Recognizer()
    TEXT = ""
    for i, chunk in enumerate(audio_chunks):
        with sr.AudioFile(f"chunk{i}.wav") as source:
            audio_listened = r.record(source)
            try:
                rec = r.recognize_google(audio_listened)
                TEXT += " " + rec
                st.write(rec)
            except sr.UnknownValueError as e:
                print("Error:", str(e))

    # if you don't want to split audio file into chunks.
    # make sure delete AudioSegment.from_file line, otherwise we opened audio file twice.
    # with sr.AudioFile(audio_file) as source:
    #     audio_listened = r.record(source)
    #     try:
    #         rec = r.recognize_google(audio_listened)
    #         st.write(rec)
    #     except sr.UnknownValueError as e:
    #         print("Error:", str(e))

    # download audio to text
    st.download_button("Download", TEXT)
