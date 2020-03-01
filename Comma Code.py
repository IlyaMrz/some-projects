# Comma Code
# Say you have a list value like this:
# spam = ['apples', 'bananas', 'tofu', 'cats']
# Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, with and inserted before the last item.
# For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'.
# But your function should be able to work with any list value passed to it. Be sure to test the case where an empty list [] is passed to your function.

spam = ['apples', 'bananas', 'tofu', 'cats', 'bear', 'dog', 'okay']


def fun(ls):
    z = ''
    if len(ls) == 0:
        pass
    else:
        ls.insert(-1, ' and ')
        for i in ls[:-3]:
            z += i + ', '
        z = z + ls[-3] + ls[-2] + ls[-1]

    return(z)


print(fun(spam))
