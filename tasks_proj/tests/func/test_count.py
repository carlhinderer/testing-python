import pytest
import tasks
from tasks import Task


def test_empty_count_returns_zero():
    assert tasks.count() == 0


def test_nonempty_count_returns_nonzero():
    tasks.add(Task('do something'))
    tasks.add(Task('do something else'))
    assert tasks.count() == 2
