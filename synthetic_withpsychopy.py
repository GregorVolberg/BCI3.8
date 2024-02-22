import time

from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds

from psychopy import visual, core  # import some libraries from PsychoPy
from psychopy.hardware import keyboard


outFileName = "syntheticTest"

params = BrainFlowInputParams()
board  = BoardShim (BoardIds.SYNTHETIC_BOARD.value, params) # board id is 0
srate  = BoardShim.get_sampling_rate(BoardIds.SYNTHETIC_BOARD.value)

#tstamp = datetime.now().strftime("%Y%m%d-%H:%M:%S")
fname = "file://" + outFileName + "_" + str(srate) + "Hz.csv:w"

board.prepare_session ()
board.start_stream (450000, fname) # ring buffer size, file name

time.sleep (1)

##### presentation routine
mywin = visual.Window([800,600], monitor="testMonitor", units="deg")
#mywin.callOnFlip(board.insert_marker,1)

#create some stimuli
stim1 = visual.TextStim(win=mywin, text="Augen zu!")
stim1.draw()

for frameN in range(60*6):
    mywin.flip()   # 6 Seconds
    if frameN%25 == 0:  # Present fixation for a subset of frames
        board.insert_marker(1)

mywin.close()
#################
time.sleep (1)

board.stop_stream ()
board.release_session ()
