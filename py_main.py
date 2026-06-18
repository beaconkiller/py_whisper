from faster_whisper import WhisperModel
import os
import asyncio
from services.SrvRecord import SrvRecord
from services.SrvTranslate import SrvTranslate



def main():
    # SrvTranslate.run_translate_batch()
    # SrvRecord.record()
    asyncio.run(SrvRecord.record_continuously())


main()