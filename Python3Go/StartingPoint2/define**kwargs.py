# **kwargs allows us to pass variable number of keyword argument like this func_name(name='tim', team='school')

def keywords_func(**key_args):
    for i, j in key_args.items():
        print(i, j)


keywords_func(
    name='Cenk',
    sport='football',
    roll=19,
    goba='stupid'

)  # istedigin kadar keywords pass et


def my_three(a, b, c):
    print(a, b, c)


a = [1, 2, 3]
b = [5, 6, 7]
my_three(*a)  # here list is broken into three elements
my_three(*b)
