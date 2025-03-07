# So far these are only needed to test standalone
import sys
import numpy as np

# Different path because not running in fenics yet
#sys.path.append("home/fenics/shared/source_code/dependencies/cell_ion_module")
import recode_dictionary

## Class for cell ion models
#
#calculate calcium concentration (and other concentrations depending on the model) and ion voltage
class cell_ion_module():

    def __init__(self,params):

        # Specify model to be ran
        temp = params["model"][0]

        base_dir = "cell_ion_module."
        model_name = base_dir + temp

        # Import the model
        self.model = __import__(model_name)
        #help(self.model)
