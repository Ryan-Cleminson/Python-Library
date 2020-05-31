import rosbag_pandas
import pandas as pd
import numpy

df = rosbag_pandas.bag_to_dataframe('Real_Test.bag’)

df.to_csv (r'C:\GitHub\Python-Library\RosBagFileHandling\export_dataframe.csv', index = False, header=True)