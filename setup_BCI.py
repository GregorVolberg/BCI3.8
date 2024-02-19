# test for shimming etc
# https://brainflow-openbci.readthedocs.io/en/latest/Examples.html

import numpy as np

import brainflow
from brainflow.board_shim import BoardShim, BrainFlowInputParams
from brainflow.data_filter import DataFilter, FilterTypes, AggOperations

from psychopy import visual, core  # import some libraries from PsychoPy
from psychopy.hardware import keyboard
import psychtoolbox as ptb
from psychopy import sound

#BoardShim()


#create a window
mywin = visual.Window([800,600], monitor="testMonitor", units="deg")

#create some stimuli
stim1 = visual.TextStim(win=mywin, text="Augen zu!")
#grating = visual.GratingStim(win=mywin, mask="circle", size=3, pos=[-4,0], sf=3)
#fixation = visual.GratingStim(win=mywin, size=0.5, pos=[0,0], sf=0, rgb=-1)

#create a keyboard component
kb = keyboard.Keyboard()

#draw the stimuli and update the window
stim1.draw()
#fixation.draw()
mywin.flip()

#pause, so you get a chance to see it!
core.wait(1.0)

#sound
mySound = sound.Sound('A')
#now = ptb.GetSecs()
#mySound.play(when=now+0.5) 
nextFlip = mywin.getFutureFlipTime(clock='ptb')

mySound.play(when=nextFlip)
mywin.flip() 
core.wait(nextFlip+1.0)
mywin.close()
