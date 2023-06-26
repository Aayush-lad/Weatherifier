import azure.cognitiveservices.speech as speechsdk
from azure.cognitiveservices.speech.audio import AudioOutputConfig
from config import get_value_from_api

def text_to_speech(text: str, output_file: str, voice: str = 'en-US-Guy24kRUS') -> None:
    subscription_key = get_value_from_api('subscription_key')
    endpoint = 'https://centralindia.api.cognitive.microsoft.com/sts/v1.0/issuetoken'
    speech_config = speechsdk.SpeechConfig(subscription=subscription_key, region='centralindia')
    audio_config = AudioOutputConfig(use_default_speaker=True)
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    synthesizer.speak_text(text)
