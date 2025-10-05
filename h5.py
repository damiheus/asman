import h5py 
import numpy as np 

with h5py.File('x.hdf', 'r') as f: 

 print("Keys: %s" % f.keys()) 

 a_group_key = list(f.keys())[0] 


 data = list(f[a_group_key])
