import struct
import wave


def convert_to_wav(data_set, sample_rate, file_name):
    wav = wave.open(file_name, "w")
    wav.setnchannels(1)  # --> makes it mono.
    wav.setsampwidth(2)
    wav.setframerate(sample_rate)

    for value in data_set:
        value = struct.pack("<h", int(value*8))
        wav.writeframesraw(value)

    wav.close()
