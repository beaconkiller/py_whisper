import sounddevice as sd
from scipy.io.wavfile import write


class SrvRecord:


    def record(self):
        sample_rate = 44100                     # frequency
        duration = 5                            # in seconds
        filename = "my_voice_recording.wav"


        # Record microphone input into a NumPy array
        audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=2, dtype='int16')
        sd.wait()  # Block the script until the recording finishes


        # Save the captured data as a WAV file
        write(filename, sample_rate, audio_data)
