"""
Write a simple python function

"""


def my_function(first_name,last_name,age ):
    print('My First function in sample_script')
    print('first_name: {}, last_name: {}, age: {} '.format(first_name, last_name, age))


def f(required_arg, optional_arg1="1"):
    print(required_arg, optional_arg1)


def main():
    my_function(first_name='John', last_name='Jack', age=40 )
    f('Hello', 10)


if __name__ == "__main__":
    main()
