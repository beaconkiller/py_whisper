from faster_whisper import WhisperModel
import os

from services.SrvTranslate import SrvTranslate


def getFiles():
    curDir = os.getcwd()
    fileStorage = os.path.join(curDir, 'file_storage')
    files = os.listdir(fileStorage)

    arr = []
    for el in files:
        if(el == '.gitkeep') : continue
        arr.append(os.path.join(curDir, 'file_storage',el))

    return arr




def main():
    files = getFiles()

    i = 0
    for audio in files:
        print(i)
        SrvTranslate.translateAudio(audio)
        # SrvTranslate.test()
        i +=1 

main()