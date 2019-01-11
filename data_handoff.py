import ctypes
import sample_data_set as sample
import numpy as np

def handoff(k):
    init_centers=[np.array([50, 17], dtype="float32"), np.array([20, 10], dtype="float32")] #Centers are in the same form as the points, i.e. the first array is the x's and the second is the y's
    x=np.array(sample.data['x'], dtype="float32")
    y=np.array(sample.data['y'], dtype="float32")
    
    data_size=len(x)
    
    #Declare it as a int8 because np.bool is one byte anyway so there's no difference in size, and it's easier to handoff to C in int8 form 
    clusters=[np.zeros(data_size, dtype=np.int8) for i in xrange(k)]
    
    
    centers_handlers=[np.ctypeslib.as_ctypes(array) for array in init_centers]
    
    centers_pointer=(ctypes.POINTER(ctypes.c_float)*k)(*centers_handlers)
    
    dataset_handlers=[np.ctypeslib.as_ctypes(x), np.ctypeslib.as_ctypes(y)]
    
    dataset_pointer=(ctypes.POINTER(ctypes.c_float)*2)(*dataset_handlers)

    clusters_handlers=[np.ctypeslib.as_ctypes(cluster) for cluster in clusters]

    clusters_pointer=(ctypes.POINTER(ctypes.c_int8)*k)(*clusters_handlers)
    
    #distance=0

    #distance_pointer=(ctypes.POINTER(ctypes.c_float))(distance)

    
    cdll=ctypes.CDLL("./k_means.so")
    
    cdll.k_means.restype=ctypes.c_double

    distance= cdll.k_means(ctypes.c_int(2), centers_pointer, dataset_pointer, clusters_pointer, ctypes.c_int(x.size)) 
    print distance, cdll.k_means.restype, clusters
