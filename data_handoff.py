import ctypes
import sample_data_set as sample
import numpy as np

def handoff(k):
    init_centers=[np.array([50, 175], dtype="float32"), np.array([20, 10], dtype="float32")] #Centers are in the same form as the points, i.e. the first array is the x's and the second is the y's
    x=np.array(sample.data['x'])
    y=np.array(sample.data['y'])
    
    data_size=len(x)

    clusters=[np.array([np.zeroes(data_size),np.zeroes(data_size)], dtype="float32"),np.array([np.zeros(data_size),np.zeros(data_size)], dtype="float32")]
    
    print init_centers
    centers_handlers=[np.ctypeslib.as_ctypes(array) for array in init_centers]
    
    centers_pointer=(ctypes.POINTER(ctypes.c_float)*k)(*centers_handlers)
    
    dataset_handlers=[np.ctypeslib.as_ctypes(x), np.ctypes.as_ctypes(y)]
    
    dataset_pointers=(ctypes.POINTER(ctypes/c_float)*2)(dataset_handlers)

    #TODO figure out how to handle clusters handler

    #ctypes.CDLL("./k_means.so").tester(centers_pointer_array)
    #ctypes.CDLL("./k_means.so").k_means(ctypes.c_int(2), centers_pointer, dataset_pointer, , ctypes.c_int(x.size))

