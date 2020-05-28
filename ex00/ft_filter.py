def ft_filter(function_to_apply, list_of_inputs):
    res = []
    for x in range(0, len(list_of_inputs)):
        if function_to_apply(list_of_inputs[x]) == True:
            res.append(list_of_inputs[x])
    return (iter(res))
    pass

def ft_pow(nb):
    return(bool(nb > 2))

test = [1,2,3,4,5]
testme = [1,2,3,4,5]

print('test', test)
print('meee', testme)

print(filter(ft_pow, test))
print(ft_filter(ft_pow, testme))

print(type(filter(ft_pow, test)))
print(type(ft_filter(ft_pow, testme)))

print(list(filter(ft_pow, test)))
print(list(ft_filter(ft_pow, testme)))

print('test', test)
print('meee', testme)
