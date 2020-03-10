import numpy as np

# save data
arr = np.arange(5)
np.save('data/test', arr)
# load data
print(np.load('data/test.npy'))


# save multiple arrays
a = np.arange(5)
b = np.arange(6)
c = np.arange(7)
np.savez('data/test', a, b, c_array=c)

data = np.load('data/test.npz')
# {'arr_0':a, 'arr_1':b, 'c_array':c}
print('arr_0 : ', data['arr_0'])
print('arr_1 : ', data['arr_1'])
print('c_array : ', data['c_array'])
