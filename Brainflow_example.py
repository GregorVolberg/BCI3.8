# simple Brainflow read
# from https://brainflow-openbci.readthedocs.io/en/latest/Examples.html
# and https://brainflow.readthedocs.io/en/stable/SupportedBoards.html#cyton
import numpy as np
import pandas as pd
import time
import brainflow
from brainflow.board_shim import BoardShim, BrainFlowInputParams, LogLevels, BoardIds
from datetime import datetime
#from brainflow.data_filter import DataFilter, FilterTypes, AggOperations

outFileName = "testData"

#BoardShim.enable_dev_board_logger ()
params = BrainFlowInputParams ()
params.serial_port = 'COM3'

board = BoardShim (BoardIds.CYTON_BOARD.value, params) # board id is 0
srate = BoardShim.get_sampling_rate(BoardIds.CYTON_BOARD.value)

tstamp = datetime.now().strftime("%Y%m%d-%H:%M:%S")
fname = "file://" + outFileName + "_" + str(srate) + "Hz.csv:w"
board.prepare_session ()

#BoardShim.log_message (LogLevels.LEVEL_INFO.value, 'start streaming ...')
#board.start_stream ()
board.start_stream (450000, fname) # ring buffer size, file name

#BoardShim.log_message (LogLevels.LEVEL_INFO.value, 'start sleeping in the main thread')
for j in range(4):
    time.sleep (1)
    board.insert_marker(j+1)

data = board.get_current_board_data (20) # get 20 latest data points dont remove them from internal buffer
# dataf = board.get_board_data() # Get all board data and remove them from ringbuffer
board.stop_stream ()
board.release_session ()

eeg_channels = BoardShim.get_eeg_channels (BoardIds.CYTON_BOARD.value)
df = pd.DataFrame (np.transpose (data))
print ('Data From the Board')
print (df.head (10))

# demo for data serialization using brainflow API, we recommend to use it instead pandas.to_csv()
DataFilter.write_file (data, 'test.csv', 'w') # use 'a' for append mode
restored_data = DataFilter.read_file ('test.csv')
restored_df = pd.DataFrame (np.transpose (restored_data))
print ('Data From the File')
print (restored_df.head (10))


