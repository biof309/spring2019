# dunder file
def print_name():
    print(__file__)


def multiply(x: int, y: int) -> int:
    """This function returns 5"""
    return x * y

def something_terrible():
    while True:
        print('hi')


if __name__ == '__main__':
    print_name()
