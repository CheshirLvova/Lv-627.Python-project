from validation import *


def reverse_n(self) -> str:
    print("""88. Given a natural number n.
    б) Change the order of digits of n by reversing its digits.""")
    n = input_natural_number()
    n = str(n)
    # if n[0] == '-':
    #     return int(n[:0:-1]))
    return f"Reversed number = {int(n[::-1])} "
