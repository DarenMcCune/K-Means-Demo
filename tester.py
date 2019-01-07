import numpy as np
import ctypes

count = 5
size = 1000

#create some arrays
arrays = [np.array([3,2,1,5],dtype="float32") for ii in range(count)]
print arrays
#get ctypes handles
ctypes_arrays = [np.ctypeslib.as_ctypes(array) for array in arrays]

#Pack into pointer array
pointer_ar = (ctypes.POINTER(ctypes.c_float) * count)(*ctypes_arrays)

ctypes.CDLL("./libfoo.so").foo(ctypes.c_int(count), pointer_ar, ctypes.c_int(4))
