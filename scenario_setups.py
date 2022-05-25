#using this Python file to set up different options in the lever space - used for 
# exploratory data analysis of different uncertainties (out of policy control)

#Maanav Jhatakia
#EPA1361 MBDM - Gelderland province, flood strategy 
#Last modified: May 25 2022

#import necessary packages - more or less default imports when using the workbench
import math
from ema_workbench import Scenario
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#define ethe different policy levers - RfR for each dike, raise the dike for each, early warning system
def policy_lev(d1 = 0, d2 = 0, d3 = 0, d4 = 0, d5 = 0, early_warning = 0,
    rfr0 = 0, rfr1 = 0, rfr2 = 0, rfr3 = 0, rfr4 = 0):

    #fit these to the names in dike_model_function.py to run the model using a dictionary
    policy_levers = {'A.1_DikeIncrease':d1, 'A.2_DikeIncrease':d2, 'A.3_DikeIncrease':d3,
        'A.4_DikeIncrease':d4, 'A.5_DikeIncrease': d5, 'EWS:DaysToThreat':early_warning, 
        '0_RfR':rfr0, '1_RfR':rfr1, '2_RfR':rfr2, '3_RfR':rfr3, '4_RfR':rfr4 }
    
    return policy_levers