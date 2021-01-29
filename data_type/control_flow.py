import time
import logging
import sample_script


def my_function():
    print('My First function')


def get_list_of_fruits():
    fruits = ["apple", "banana", "grape"]
    # for (int i = 0; i >= 10; i++)
    # for (String str : MyList)
    for i in range(2):
        print('Name of fruits: {}'.format(fruits[i]))
    return fruits


def while_demo():
    count = 0
    while count < 5:
        print('to continue {}'.format(count))
        count = count + 1
    else:
        print("While condition is false")


def if_else_demo():
    money = True

    if money == True:
        print('I have money {}'.format(money))
    else:
        print('I am poor, please arrange GoFundMe')


def get_tick_time():
    ticks = time.time()
    print('Current time {}'.format(ticks))
    localtime = time.asctime(time.localtime(ticks))
    print(localtime)
    logging.info('Localtime {}'.format(localtime))


def try_catch_demo():
    try:
        x = int(input("Enter a number"))
    except ValueError:
        print('Invalid number')


def use_smaple_script_function():
    sample_script.my_function()


def main():
    # my_function()
    # list_fruits = get_list_of_fruits()
    # print(list_fruits)
    # while_demo()
    # get_tick_time()
    use_smaple_script_function()


if __name__ == "__main__":
    main()
