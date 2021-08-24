from __init__ import *


def choose_task():
    res = Tasks()
    number_of_task = str(input("""To choose the problem, enter the number of task from the list: 088a, 088b, 322.
If you want to quit, enter "exit" from the keyboard: """))
    if number_of_task == "088a":
        print(res.find_three_in_record_of_m())
        choose_task()
    elif number_of_task == "088b":
        print(res.reverse_n())
        choose_task()
    elif number_of_task == "322":
        print(res.max_sum_of_divisors())
        choose_task()
    else:
        if number_of_task == "exit":
            quit()
        print(f"There is no task {number_of_task}. Please, try again...")
        choose_task()


if __name__ == '__main__':
    print("Hi. Welcome to the problem-solver program.")
    choose_task()

