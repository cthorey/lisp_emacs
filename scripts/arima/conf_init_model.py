import os
import sys
import json
import sys
sys.path.append('../../')
from multiprocessing import cpu_count
from utils.initialization import *
from utils.data_utils import load_raw_data
from utils.helper import myDict
from utils import pipe_def

fognet = os.path.join('~', 'Documents', 'project', 'competition', 'fognet')
conf = {}


####################################
# Version code
conf['nb_cpus'] = 2

####################################
# Model definition
conf['overwrite'] = True
conf['continue_training'] = False

# pipeline
# Faire bien attention __ et pas _ pour les parametres
conf['pipe'] = getattr(pipe_def, 'pipe0')

# Architecture
conf['type_model'] = 'arima'
conf['which_architecture'] = 'SARIMAX'

# Hyperparameters
conf['AR'] = 0
conf['MA'] = 1
conf['D'] = 1
conf['Season_AR'] = 0
conf['Season_MA'] = 0
conf['Season_D'] = 0
conf['Season_Period'] = 0

conf['verbose'] = 2
# Initialization
conf['platform'], conf[
    'access_token_oscar'] = get_platform_and_create_folder(fognet)
initialize_work_tree(fognet, conf)