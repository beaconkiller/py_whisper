import os
import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write

from services.SrvDir import SrvDir
from services.SrvHelper import SrvHelper

class SrvRecord:

    gain = 6.0      # Use this to increase gain in Db
    duration = 5    # In seconds

    def record(self):

        print(SrvHelper.getDateString())

        sample_rate = 44100                     # frequency
        duration = 5                            # in seconds
        filename = f"record_{SrvHelper.getDateString()}.wav"

        audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='float32')
        audio_data = self.multiply_gain(audio_data)
        audio_data = np.clip(audio_data, -1.0, 1.0)

        sd.wait()  

        save_target = os.path.join(SrvDir.dir_recording_out, filename)

        write(save_target, sample_rate, audio_data)


    def multiply_gain(self, data):
        multipler = 10 ** (self.gain / 20)
        return data * multipler
        

SrvRecord = SrvRecord()