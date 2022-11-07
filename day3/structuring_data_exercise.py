data = [[1., 2., 3.],
        [4., 5., 6.]]


def attach_names(data, names):
    output = []

    for i in range(len(data)):
        output.append({'name': names[i],
                       'data': data_row})

    return output


output = attach_names(data, ['Alice', 'Bob'])
print(output)