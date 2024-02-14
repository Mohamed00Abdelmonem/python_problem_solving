# from pytube import YouTube
# import os
# from pathlib import Path

# link = input("Enter link here: ")

# url = YouTube(link)

# print("downloading....")

# # Get the stream with resolution closest to 720p
# video = url.streams.filter(res="144p").first()

# # Specify the destination path
# download_path = r"D:\vedios youtube"

# # Download the video to the specified path
# video.download(download_path)

# print("Downloaded! :)")



# ----------------------------------------------------------



from pytube import YouTube
# from googletrans import Translator
import os
# from pathlib import Path

def download_video(link, quality='720p'):
    url = YouTube(link)

    print("downloading....")

    # Get the stream with the specified quality
    video = url.streams.filter(res=quality, progressive=True).first()

    # Specify the destination path
    download_path = r"D:\vedios youtube"

    # Download the video to the specified path
    video.download(download_path)

    print("Downloaded Done! :)")

    # # Translate video title to the specified language
    # translator = Translator()
    # translated_title = translator.translate(url.title, dest=language).text
    # print(f"Translated Title: {translated_title}")

# Example usage:
video_link = input("Enter YouTube video link: ")
download_video(video_link, quality='720p')




# ----------------------------------------------------------








# from pytube import YouTube
# from google.cloud import texttospeech
# from google.cloud import speech_v1p1beta1 as speech
# import os
# from googletrans import Translator

# def download_and_translate(link, quality="144", language="fr"):
#     try:
#         url = YouTube(link)
#         print(f"Video Title: {url.title}")

#         # Get the stream with the specified quality
#         video = url.streams.filter(res=quality, progressive=True).first()
#         if not video:
#             raise ValueError(f"No video stream found for quality {quality}.")

#         # Specify the destination path
#         download_path = r"D:\vedios youtube"

#         print("Downloading....")
#         # Download the video to the specified path
#         video.download(download_path)
#         print("Downloaded Done! :)")

#         # Transcribe the video audio using Google Cloud Speech-to-Text
#         client = speech.SpeechClient()
#         audio_path = os.path.join(download_path, f"{url.title}.wav")
#         video.audio.download(audio_path)

#         with open(audio_path, "rb") as audio_file:
#             content = audio_file.read()

#         audio = speech.RecognitionAudio(content=content)
#         config = speech.RecognitionConfig(
#             encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
#             sample_rate_hertz=44100,
#             language_code=language,
#         )

#         response = client.recognize(config=config, audio=audio)

#         # Translate and print the transcriptions
#         translator = Translator()
#         for result in response.results:
#             original_text = result.alternatives[0].transcript
#             translated_text = translator.translate(original_text, dest=language).text
#             print(f"Original: {original_text}")
#             print(f"Translated: {translated_text}")

#         # Synthesize translated text using Google Cloud Text-to-Speech
#         tts_client = texttospeech.TextToSpeechClient()
#         synthesis_input = texttospeech.SynthesisInput(text=translated_text)
#         voice = texttospeech.VoiceSelectionParams(
#             language_code=language, name=f"{language}-Wavenet-A"
#         )
#         audio_config = texttospeech.AudioConfig(
#             audio_encoding=texttospeech.AudioEncoding.LINEAR16
#         )

#         response = tts_client.synthesize_speech(
#             input=synthesis_input, voice=voice, audio_config=audio_config
#         )

#         # Save the translated and synthesized audio
#         translated_audio_path = os.path.join(download_path, f"{url.title}_{language}.wav")
#         with open(translated_audio_path, "wb") as out_audio:
#             out_audio.write(response.audio_content)

#         print("Translation and synthesis complete!")

#     except Exception as e:
#         print(f"Error: {e}")

# # Example usage:
# video_link = input("Enter YouTube video link: ")
# download_and_translate(video_link, quality="720", language="ar")
