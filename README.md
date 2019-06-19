# pywire-processing
Simple Python3 wire stream, using numpy array for processing

This is a Python3 "wire" script: it takes default input, convert it into a Numpy Array and process it.

There are 4 examples of processing:
- no processing: just wire the input to the output (just for having a very-basic in-out connector)
- raise/lower signal: multiply the data for a static index to modify output volume
- tremolo: cycle volume to have a tremolo effect
- roboto: mix the signal with a sine wave to have a robotic-like effect

Functions are commented. Comments are welcomed ;-)
