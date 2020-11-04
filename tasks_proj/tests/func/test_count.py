import pytest
import tasks
from tasks import Task


def test_empty_returns_zero_count(tasks_db):
    assert tasks.count() == 0


def test_add_increases_count(db_with_3_tasks):
    tasks.add(Task('do something'))
    assert tasks.count() == 4
