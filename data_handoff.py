import ctypes
import sample_data_set as sample
import numpy as np

def handoff(k):
    init_centers=[np.array([50, 175], dtype="float32"), np.array([20, 10], dtype="float32")] #Centers are in the same form as the points, i.e. the first array is the x's and the second is the y's
    x=np.array(sample.data['x'])
    y=np.array(sample.data['y'])
    clusters=[[[],[]],[[],[]]]
    
    print init_centers
    centers_ctypes_array=[np.ctypeslib.as_ctypes(array) for array in init_centers]
    
    centers_pointer_array=(ctypes.POINTER(ctypes.c_float)*k)(*centers_ctypes_array)
    
    ctypes.CDLL("./k_means.so").tester(centers_pointer_array)
    #ctypes.CDLL("./k_means.so").k_means(ctypes.c_int(2), , , , ctypes.c_int(x.size))

