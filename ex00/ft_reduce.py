from functools import reduce

def ft_reduce(function_to_aplly, list_of_inputs):
    res = 0
    for x in range(0, len(list_of_inputs)):
        res = (function_to_aplly(res, list_of_inputs[x]))
    return(res)
    pass

def ft_pow(nb, nb2):
    return(nb + nb2)

test = [1,2,3,4,5]
testme = [1,2,3,4,5]

print('test', test)
print('meee', testme)

print(reduce(ft_pow, test))
print(ft_reduce(ft_pow, testme))

print(type(reduce(ft_pow, test)))
print(type(ft_reduce(ft_pow, testme)))

print('test', test)
print('meee', testme)
