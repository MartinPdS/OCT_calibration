
'''_____Standard imports_____'''
import os
import sys
import numpy as np
import json
import scipy.fftpack as fp
import matplotlib.pyplot as plt


'''_____Add package_____'''
p = os.path.abspath('.')
if p not in sys.path:
    sys.path.append(p)


'''_____Project imports_____'''
from src.toolbox.parsing import Bscan_parse_arguments
from src.toolbox.loadings import load_Bscan_spectra, load_calibration
from src.toolbox.plottings import Bscan_plots
import src.toolbox.directories as directories
from src.toolbox.spectra_processing import process_Bscan, denoise_Bscan



arguments = Bscan_parse_arguments()

dimension = (1,3147,1024)

Bscan_spectra = load_Bscan_spectra(arguments.input_file, dimension = dimension)


calibration = load_calibration(dir =  arguments.calibration_file)

Bscan = []

for iteration in range(dimension[0]):

    print( "########## iteration [{0}/{1}]".format( iteration, dimension[0] ) )

    tmp = process_Bscan(Bscan_spectra[iteration], calibration, shift=0, arguments=arguments)

    Bscan.append( denoise_Bscan(tmp) )

Bscan_output = np.mean(Bscan, axis=0)



Bscan_plots(Bscan_output, arguments=arguments)


#-