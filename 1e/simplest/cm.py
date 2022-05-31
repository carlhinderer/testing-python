from contextlib import contextmanager

def test_method_one():
    with manager():
        print('Method one')

def test_method_two():
    with manager():
        print('Method two')

def test_method_three():
    with manager():
        print('Method three')


@contextmanager
def manager():
    print('Entering method...')
    yield
    print('Exiting method...')