import numpy as np
import pandas as pd
import seaborn as sns

import matplotlib
matplotlib.use('TkAgg') #Had issues with the weyland backend for matplotlib
import matplotlib.pyplot as plt

from scipy.stats import ttest_ind
from scipy.stats import t

data = pd.read_csv('A_B_Test_Data.csv')

#print(data.head)

def hypothesis_test_from_scratch():

    # 1. Calculate the means of the two samples

    mean_eng_new = data.groupby("Design").agg({"mean"}).iloc[0,1]
    mean_eng_old = data.groupby("Design").agg({"mean"}).iloc[1,1]

    # 2. Calculate the standard deviations of the two samples

    std_eng_new = data.groupby("Design").agg({"std"}).iloc[0,1]
    std_eng_old = data.groupby("Design").agg({"std"}).iloc[1,1]

    # 3. Calculate the standard errors of the two samples
    
    n_st_error = std_eng_new/np.sqrt(data.drop("User_ID",axis=1).groupby("Design").count())
    o_st_error = std_eng_old/np.sqrt(data.drop("User_ID",axis=1).groupby("Design").count())

    # 4. Calculate the t-statistic = (mean1 - mean2) / sqrt(se1^2 + se2^2)

    t_stat = (mean_eng_new - mean_eng_old) / np.sqrt(std_eng_new**2/len(data[data['Design'] == 'New']['Engagement']) + std_eng_old**2/len(data[data['Design'] == 'Old']['Engagement']))

    print(f"t stat: {t_stat}")

    # 5. Calculate the degrees of freedom = n1 + n2 - 2

    n1 = len(data[data['Design'] == 'Old']['Engagement'])
    n2 = len(data[data['Design'] == 'New']['Engagement'])

    df = n1 + n2 - 2

    # 6. Calculate the p-value = 2 * (1 - cdf(abs(t-statistic), df))

    p = 2 * (1 - t.cdf(np.abs(t_stat), df))
    print(f"p value: {p}")

hypothesis_test_from_scratch()