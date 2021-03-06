# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
from matplotlib import rcParams
from matplotlib import rcParamsDefault
import numpy as np

def set_figure_settings(Figure_Type,**kwargs):
    rcParams.update(rcParamsDefault)
    params = {}
    if Figure_Type == 'paper':
        params = {'lines.linewidth': 2,
            'lines.markersize': 5,
            'legend.fontsize': 8,
            'legend.borderpad': 0.2,
            'legend.labelspacing': 0.2,
            'legend.handletextpad' : 0.2,
            'legend.borderaxespad' : 0.2,
            'legend.scatterpoints' :1,
            'xtick.labelsize' : 8,
            'ytick.labelsize' : 8,
            'axes.titlesize' : 8,
            'axes.labelsize' : 8,
            'figure.autolayout': True,
            'font.family': 'Calibri',
            'font.size': 8}
    elif Figure_Type == 'presentation':
        params = {'lines.linewidth'   : 3,
          'legend.handlelength'  : 1.0,
          'legend.handleheight'  : 1.0,
          'legend.fontsize': 16,
          'legend.borderpad': 0.2,
          'legend.labelspacing': 0.2,
          'legend.handletextpad' : 0.2,
          'legend.borderaxespad' : 0.2,
          'legend.scatterpoints' :1,
          'xtick.labelsize' : 16,
          'ytick.labelsize' : 16,
          'axes.titlesize' : 24,
          'axes.labelsize' : 20,
          'figure.autolayout': True,
          'font.size': 16.0}
    rcParams.update(params)
    rcParams.update(kwargs)