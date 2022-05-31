import pytest
import tasks
from tasks import Task


def test_add_raises():
    """add() should raise an exception with wrong type param."""
    with pytest.raises(TypeError):
        tasks.add('not a task object')
    with pytest.raises(ValueError):
        tasks.add(Task(2))
    with pytest.raises(ValueError):
        tasks.add(Task('owner not a string', owner=2))
    with pytest.raises(ValueError):
        tasks.add(Task('id not None', id=1))


def test_start_tasks_db_raises():
    """Make sure unsupported db raises an exception."""
    with pytest.raises(ValueError) as excinfo:
        tasks.start_tasks_db('some/great/path', 'mysql')
    exception_msg = excinfo.value.args[0]
    assert exception_msg == "db_type must be a 'tiny' or 'mongo'"


@pytest.mark.smoke
def test_list_raises():
    """list() should raise an exception with wrong type param."""
    with pytest.raises(TypeError):
        tasks.list_tasks(owner=123)


@pytest.mark.get
@pytest.mark.smoke
def test_get_raises():
    """get() should raise an exception with wront type param."""
    with pytest.raises(TypeError):
        tasks.get(task_id='123')
