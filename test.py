import sys

print(sys.version)
print(sys.executable)


def greetfunc(variable):

        greetingmodule = 'Hello, {}'.format(variable)
        return greetingmodule

print(greetfunc('World'))
print(greetfunc('Eden'))

#define a function (i named it greetfunc) that 
#can plug parameters in for different outcomes
#to make it even easier to define
#i created a module as the backend function
#then call it   

