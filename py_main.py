from faster_whisper import WhisperModel
import os

from services.SrvTranslate import SrvTranslate



def main():
    SrvTranslate.run_translate_batch()

main()