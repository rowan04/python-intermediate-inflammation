# What's the best way to structure our data?
import numpy as np

data = np.array([[1., 2., 3.],
                 [4., 5., 6.]])

# We can make this more meaningful by adding structure and metadata
patients = [
    {
        'name': 'Alice',
        'data': [1., 2., 3.]
    },
    {
        'name': 'Bob',
        'data': [4., 5., 6.]
    }
]