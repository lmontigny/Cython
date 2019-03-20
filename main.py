# import sum_cython
# sum_cython.test(5)
import timeit

cy = timeit.timeit('''sum_cython.test(5)''',setup='import sum_cython',number=100)
py = timeit.timeit('''sum_original.test(5)''',setup='import sum_original', number=100)

print(cy, py)
print('Cython is {}x faster'.format(py/cy))
