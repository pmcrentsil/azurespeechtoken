# azure_speech_service.py

# Description:
# This file demonstrates the integration of Azure Cognitive Services for real-time
# speech-to-text transcription. It allows Charter’s call center agents to transcribe calls
# in real-time, providing valuable insights and improving operational efficiency.
# The system uses Azure's Speech API for AI-powered transcription.

import azure.cognitiveservices.speech as speechsdk

class AzureSpeechService:
    def __init__(self, subscription_key, region):
        self.speech_config = speechsdk.SpeechConfig(subscription=subscription_key, region=region)
        self.speech_recognizer = speechsdk.SpeechRecognizer(speech_config=self.speech_config)

    def transcribe_audio(self, audio_file_path):
        """Transcribe audio file to text using Azure Speech API."""
        audio_config = speechsdk.audio.AudioConfig(filename=audio_file_path)
        result = self.speech_recognizer.recognize_once_from_file(audio_file_path)
        
        if result.reason == speechsdk.ResultReason.RecognizedSpeech:
            return result.text
        else:
            return "Error transcribing audio"

# Example usage:
azure_speech_service = AzureSpeechService(subscription_key="YourAzureSubscriptionKey", region="YourRegion")
transcription = azure_speech_service.transcribe_audio("path/to/audio/file.wav")
print("Transcription:", transcription)
