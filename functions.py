import numpy as np
from scipy.io import savemat, loadmat
import pandas as pd
import h5py

data = np.random.randn(4000, 4000)

file_path = '/Users/spencerlyon2/Desktop/test_data.'


def store_csv():
    pd_data = pd.DataFrame(data)
    pd_data.to_csv(file_path + 'csv')

def store_h5():
    f = h5py.File(file_path + 'h5')
    dset = f.create_dataset('data', (4000, 4000), 'f')
    dset[...] = data
    f.close()

def store_mat():
    sp_dat = {'data': data}
    savemat(file_path + 'mat', sp_dat)

def read_csv():
    pd_data_in = pd.DataFrame().from_csv(file_path + 'csv')
    return pd_data_in

def read_h5():
    f_in = h5py.File(file_path + 'h5', 'r')
    d_in = f_in['data']
    f_in.close()
    return d_in

def read_mat():
    mat_dict = loadmat(file_path + 'mat')
    return mat_dict['data']