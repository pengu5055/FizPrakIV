"""
  Run
    python3 read_dmm.py <logfile> <start freq> <freq step>
"""
import sys
import time
import serial
import string as str

def read_from_dmm():
  # ~ ser.write(b':ABORt?\r\n')
  # ~ ser.write(b'INITiate\r\n')
  ser.write(b':DATA:FRESH?\r\n')
  #ser.write(b':FETCh?\r\n')
  ser.flush()

  out = bytes()

  time.sleep(0.1)           # wait for 100ms for measurements
  while ser.inWaiting() > 0:
    out += ser.read(1)
    if out != '':
        out=out.rstrip()

  print(len(out))

  return out.decode("utf-8")


# configure the serial connections
ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=19200
)

if ser.isOpen() == False:
  ser.open()
else:
  ser.close()
  ser.open()

ser.reset_output_buffer()
ser.reset_input_buffer()

ser.flushInput()
ser.flushOutput()

#ser.open()
#ser.isOpen()

#C0s =[150, 330, 560, 820, 1150] # coupling, pF

logfile= sys.argv[1];
freq_start = int(sys.argv[2])   # start frequency , Hz
freq_end = int(sys.argv[3])     # end frequency, Hz
df = int(sys.argv[4])           # frequency step, Hz


with open(logfile,'a') as f:
  f.write("#" + "-"*80 + "\n")

  freq = freq_start

  while freq <= freq_end:

    print("-"*80, "\nfreq=", freq, " .. press ENTER", flush=True)

    input()

    val = read_from_dmm()        # in [mVAC]

    print("value=", val, flush=True)

    f.write("%d %s\n" % (freq, val))
    f.flush()

    freq = freq + df


#
# testing
#
# ~ while True:
  # ~ print("-"*80, "\nTo read press ENTER", flush=True)

  # ~ input()

  # ~ val = read_from_dmm()        # in [mVAC]

  # ~ print("value=", val, flush=True)
