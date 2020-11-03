import pytest
import tasks
from tasks import Task


@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):
    tasks.start_tasks_db(str(tmpdir), 'tiny')
    yield
    tasks.stop_tasks_db()


@pytest.fixture()
def tasks_just_a_few():
    return (
        Task('Write some code', 'Brian', True),
        Task("Code review Brian's code", 'Katie', False),
        Task('Fix what Brian did', 'Michelle', False))


@pytest.fixture()
def tasks_mult_per_owner():
    return (
        Task('Make a cookie', 'Raphael'),
        Task('Use an emoji', 'Raphael'),
        Task('Move to Berlin', 'Raphael'),

        Task('Create', 'Michelle'),
        Task('Inspire', 'Michelle'),
        Task('Encourage', 'Michelle'),

        Task('Do a handstand', 'Daniel'),
        Task('Write some books', 'Daniel'),
        Task('Eat ice cream', 'Daniel'))