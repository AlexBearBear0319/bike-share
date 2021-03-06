import pandas as pd

from glob import glob

data_files = sorted(glob('Divvy Trips*.csv'))

mergeddata = pd.concat(pd.read_csv(datafile).assign(sourcefilename = datafile) for datafile in data_files)

mergeddata.to_csv('merged.csv')