from faster_whisper import WhisperModel
import os


class SrvTranslate:

    def test(self):
        print('test')




    def translateAudio(self, filePath):
        print(filePath)

        model = WhisperModel(
            "small",
            device="cpu",
            compute_type="int8"
        )

        segments = model.transcribe(
            filePath,
            beam_size=5 
        )

        for segment in segments:
            print(segment.start, segment.end, segment.text)




SrvTranslate = SrvTranslate()

