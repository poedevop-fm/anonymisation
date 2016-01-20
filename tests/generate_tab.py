# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 11:26:08 2016

@author: Alexis Eidelman
"""

import numpy as np
import pandas as pd

def random_table_test_anonym(size, nb_groups, nb_sensible_level):
    group = np.random.randint(nb_groups, size=size)
    sensible = np.random.randint(nb_sensible_level, size=size)
    return pd.DataFrame({
        'identifiant': group,
        'sensible': sensible
                         })
