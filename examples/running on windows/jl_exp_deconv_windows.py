"""
====================================================
Python file created by .bat to run easily on Windows
====================================================

This script saves all relevant examples and lets you add your own data through a prompt.
"""
import numpy as np
from jl_exp_deconv import get_defaults
from jl_exp_deconv import IR_Results
from jl_exp_deconv.plotting_tools import set_figure_settings
from ast import literal_eval

set_figure_settings('paper')
#frequency_range = np.linspace(850,1850,num=501,endpoint=True)
frequency_range, pure_data_path, mixture_data_path_default, reaction_data_path_default = get_defaults()
pca_to_keep = 4
use_your_own = input('Do you want to use your own pure-data? Responds "yes" or "no" without quotes. \
Respond no if you want to use the default pure data to train the model.: ')
if use_your_own.lower() in ['yes', 'y']:
    pure_data_path = input('Please enter the directory to the pure-species data file: ')
    frequency_start = input('Please enter the lowest frequency to consider: ')
    frequency_end = input('Please enter the highest frequency to consider: ')
    pca_to_keep = input('Please enter the number of principal componets in the spectra to keep. \
A good starting number is the number of pure-components: ')
    frequency_range = np.linspace(float(frequency_start),float(frequency_end),num=501,endpoint=True)
mixture_data_path = input('Please enter the directory to the mixture data: ')
output_folder = input('Please enter the directory to the save the data: ')
True_or_False = input('Does the mixture data contain known concentrations? \
Enter "True" or "False" without quotes. If True,\
a parity plot is made. If False, the data is considred reaction data.: ')
if True_or_False.lower() in ['yes', 'y']:
    True_or_False = 'True'
elif True_or_False.lower() in ['no', 'n']:
    True_or_False = 'False'
contains_concentrations = literal_eval(True_or_False)
deconv = IR_Results(int(pca_to_keep), frequency_range, pure_data_path)
deconv.set_mixture_data(mixture_data_path, contains_concentrations=contains_concentrations)
if contains_concentrations == True:
    deconv.get_mixture_figures(output_folder)
    deconv.save_parity_data(output_folder)
    deconv.save_deconvoluted_spectra(output_folder)
else:
    deconv.get_reaction_figures(output_folder)
    deconv.save_reaction_data(output_folder)