from faster_whisper import WhisperModel
import os


class SrvTranslate:


    def run_translate_batch(self):
        files = self.getFiles()

        i = 0
        for audio in files:
            print(i)
            self.translateAudio(audio)
            i +=1 



    def getFiles(self):
        curDir = os.getcwd()
        fileStorage = os.path.join(curDir, 'file_storage', 'audio_in')
        files = os.listdir(fileStorage)

        arr = []
        for el in files:
            if(el == '.gitkeep') : continue
            arr.append(os.path.join(curDir, 'file_storage', 'audio_in', el))

        return arr



    def translateAudio(self, filePath):
        print(filePath)

        model = WhisperModel(
            "small",
            device="cpu",
            compute_type="int8"
        )

        segments,info = model.transcribe(
            filePath,
            beam_size=5 
        )

        for segment in segments:
            print(segment.start, segment.end, segment.text)




SrvTranslate = SrvTranslate()

