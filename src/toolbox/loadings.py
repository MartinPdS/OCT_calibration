
'''_____Standard imports_____'''
import numpy as np
import pickle
import pandas


def load_data(dir: str, type=float):

    data = []

    data = np.load(dir)

    return data


def load_Bscan_spectra(file_dir: str, dimension=(1,1024,3147)):

    data = np.load(file_dir)
    data = np.reshape(data, dimension)

    return data


def load_calibration(dir: str=None):

    return  pickle.load( open( dir, "rb" ) )


def make_dataframe(dimension: tuple) -> pandas.DataFrame:

    Aline_name = list(range(dimension[0]))*dimension[1]

    Bscan_name = np.repeat( range(dimension[1]),dimension[0])

    rows_name = list(zip(Bscan_name, Aline_name))

    cols_name = range(dimension[2])

    index = pandas.MultiIndex.from_tuples(rows_name, names=['Bscan', 'Aline'])

    return pandas.DataFrame(np.nan,index=index, columns = cols_name)
