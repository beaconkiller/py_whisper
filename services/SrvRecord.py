import os
import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import asyncio
from services.SrvDir import SrvDir
from services.SrvHelper import SrvHelper

class SrvRecord:

    duration = 5                # In seconds
    obj_record_config = {
        'sample_rate' : 44100,  # frequency
        'duration' : 5,         # in seconds
        'gain' : 6.0,           # Use this to increase gain in Db
    }

    is_recording = False

    def record(self):

        print(SrvHelper.getDateString())

        sample_rate = self.obj_record_config['sample_rate']     # frequency
        duration = self.obj_record_config['duration']           # in seconds
        filename = f"record_{SrvHelper.getDateString()}.wav"

        audio_data = sd.rec(
            int(duration * sample_rate), 
            samplerate=sample_rate, 
            channels=1, 
            dtype='float32'
        )

        audio_data = self.multiply_gain(audio_data)
        audio_data = np.clip(audio_data, -1.0, 1.0)

        sd.wait()  

        save_target = os.path.join(SrvDir.dir_recording_out, filename)

        write(save_target, sample_rate, audio_data)



    async def record_continuously(self):

        self.is_recording = True

        stream = sd.InputStream(
            samplerate=self.obj_record_config['sample_rate'],
            dtype='float32',
            channels=1,
            blocksize=1024
        )


        i = 0
        with stream:
            while self.is_recording:
                data, overflowed = stream.read(stream.blocksize)
                data = data * 3

                actual_volume = np.mean(np.abs(data.astype(np.float64)))


                # print("\033[H\033[2J", end="")
                # print( data.shape, overflowed, np.mean(data.astype(np.float64)), i)
                # print( data.shape, overflowed, np.mean(np.abs(data.astype(np.float64))), i)
                self.draw_data(actual_volume * 1000)
                # print(f"Shape: {data.shape} | Overflow: {overflowed} | Vol: {actual_volume:.6f} | Iteration: {i}")
                await SrvHelper.delay(0.001)
                i+=1


        # i = 0
        # while i < 4 :
        #     print(i)
        #     await SrvHelper.delay(2)
        #     i+=1 



    def test(self, data):
        print(data)



    def draw_data(self, data):
        str_data = ''
        # data = str(data)[0]
        # if (data == '-') : 
        #     data = 1    
        for i in range(int(data)):
            str_data = str_data + '|'
        print(str_data)



    def multiply_gain(self, data):
        multipler = 10 ** (self.gain / 20)
        return data * multipler
        

SrvRecord = SrvRecord()