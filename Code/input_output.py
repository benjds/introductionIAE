
###################
## INPUT/OUTPUT
###################

import pandas as pa
import numpy as np


col1 = [i for i in range(4)]
col2 = [float(i**2) for i in range(4) ]
col3 = ['cat1', 'cat2', 'cat3', 'cat1']

MyDataframe = pa.DataFrame({'INDEX':col1,
                  'DATE':pa.Timestamp('20130102'),
                  'SQUARED':col2,
                  'THREE':np.array([3]*4, dtype='int32'),
                  'SET':pa.Categorical(["test", "train",
                                        "test", "train"]),
                  'CAT':col3})

# setting a generic path
import os
outpath = os.path.abspath('../Results/export.csv')
print(outpath)

if not os.path.exists(os.path.abspath("../Results")):
    os.makedirs("../Results")

# exporting to csv file (without row numbers)
MyDataframe.to_csv(outpath, index_label=False, sep=";")

# reading csv file
Trainset = pa.read_csv(outpath)
print(Trainset)

# Reading file
Trainset_2 = pa.read_csv(os.path.abspath('../Data/input.csv'), sep=";")
print(Trainset_2)



