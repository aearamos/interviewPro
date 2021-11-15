def flatten_dictionary(d, separator ='.', prefix =''):
    return { prefix + separator + k if prefix else k : v 
             for kk, vv in d.items() 
             for k, v in flatten_dictionary(vv, separator, kk).items() 
             } if isinstance(d, dict) else { prefix : d } 


d = {
    'a': 1,
    'b': {
        'c': 2,
        'd': {
            'e': 3
        }
    }
}
print(flatten_dictionary(d))
# {'a': 1, 'b.c': 2, 'b.d.e': 3}
