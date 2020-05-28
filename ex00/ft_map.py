def ft_map(function_to_aply, list_of_inputs):
    res = []
    for x in range(0, len(list_of_inputs)):
        res.append(function_to_aply(list_of_inputs[x]))
    return(iter(res))
    pass

def ft_pow(nb):
    return(nb *nb)

test = [1,2,3,4,5]
testme = [1,2,3,4,5]

print('test', test)
print('meee', testme)

print(map(ft_pow, test))
print(ft_map(ft_pow, testme))

print(type(map(ft_pow, test)))
print(type(ft_map(ft_pow, testme)))

print(list(map(ft_pow, test)))
print(list(ft_map(ft_pow, testme)))

print('test', test)
print('meee', testme)
