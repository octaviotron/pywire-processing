#!/usr/bin/env python3

import pyaudio
import numpy as np

# open a new instance of PyAudio
p = pyaudio.PyAudio()

# callback function. Here signal is modified
def callback(in_data, frame_count, time_info, status):
	# all input data is converted into numpy array
	audio_data = np.frombuffer(in_data, dtype=np.int16)
	# by default do nothig but redirect (wire) the input to the output
	audio_out = audio_data

	# uncommnet next line to modify volume (1.0 max, 0.01 min)
	#audio_out = (audio_data * 0.1).astype(np.int16)

	# uncomment next line to add a vibrato efect
	#audio_out = (audio_data * vibrato_fx()).astype(np.int16)

	# uncomment next line to add a robotic effect
	#audio_out = (audio_data * sine).astype(np.int16)

	return (audio_out, pyaudio.paContinue)

# VIBRATO fx
# iterate between 0.1 and 0.9 to make volume variation
vibr = 0.0
vibr_ = -1
def vibrato_fx():
	global vibr,vibr_
	vibr = vibr + (0.2 * vibr_)
	vibr = round(vibr,1)
	if vibr >= 0.80:
		vibr_ = -1
	if vibr <= 0.10:
		vibr_ = 1
	return vibr

# ROBOTO fx
# adds a sine wave to input signal
frequency = 40
sampling_rate = 44100.0
num_samples = 2048
sine_wave = [np.sin( np.pi * frequency * x/sampling_rate ) for x in range(num_samples)]
sine = np.array(sine_wave)

# stream definition
stream = p.open(format=p.get_format_from_width(2),
	# stereo
	channels=2,
	# at 44100 hz
	rate=44100,
	input=True,
	output=True,
	frames_per_buffer=1024,
	stream_callback=callback)

# do all infinite loop and close stream stuff
stream.start_stream()
while stream.is_active():
	pass
stream.stop_stream()
stream.close()
p.terminate()
