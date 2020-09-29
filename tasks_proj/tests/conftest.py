import pytest
import tasks
from tasks import Task

@pytest.fixture()
def tasks_db(tmpdir):
    tasks.start_tasks_db(str(tmpdir), 'tiny')
    yield
    tasks.stop_tasks_db()