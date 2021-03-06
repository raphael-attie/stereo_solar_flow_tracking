import os
import glob
from pathlib import PurePath
from . import toolbox

DATA_DIR = PurePath(os.environ['DATA'], 'STEREO/L7tum/')

# Directory hosting the prepped STEREO FITS files
PREPPED_DATA_DIR = PurePath(DATA_DIR, 'prep_fits')
# Path of the of csv file containing the coordinates and labels of the training set
TRAINING_SET_CSV = PurePath(DATA_DIR, 'training_set/targets.csv')
# Output directories for data and figures generated by mballtrack: tracked positions, overlays, etc...
OUTPUT_DIR = PurePath(os.environ['DATA'], 'STEREO/L7tum/mballtrack_output')
FIG_DIR = PurePath(OUTPUT_DIR, 'figures')

# Default input dictionnary for magnetic balltracking, fixed parameters not subject to parameter sweeps
mbt_dict = {
            "nt": 10,
            "polarity": 1,
            "track_emergence": False,
            "datafiles": sorted(glob.glob(str(PurePath(PREPPED_DATA_DIR, '*.fits')))),
            "do_plots": False,
            "astropy": True,
            "verbose": False,
            "fig_dir": FIG_DIR
            }
