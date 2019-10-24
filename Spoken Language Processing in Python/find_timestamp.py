import numpy as np

# Open good morning sound wave and read frames as bytes
good_morning = wave.open('good_morning.wav', 'r')
signal_gm = good_morning.readframes(-1)

# Convert good morning audio bytes to integers
soundwave_gm = np.frombuffer(signal_gm, dtype='int16')

# View the first 10 sound wave values
print(soundwave_gm[:10])

# Find the sound wave timestamps
time_gm = np.linspace(start=0,stop=len(soundwave_gm)/framerate_gm,num=len(soundwave_gm))

# Print the first 10 timestamps
print(time_gm[:10])
