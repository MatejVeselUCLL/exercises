from datetime import date, timedelta
from tasks import Task, TaskList
from calendars import CalendarStub
import pytest

@pytest.fixture
def today():
    return date(2001, 1, 1)

@pytest.fixture
def tomorrow(today):
    return today + timedelta(days=1)

@pytest.fixture
def yesterday(today):
    return today - timedelta(days=1)

@pytest.fixture
def calendar(today):
    return CalendarStub(today)

@pytest.fixture
def sut(calendar):
    return TaskList(calendar)

def test_task_becomes_overdue(sut, tomorrow, calendar):
    task = Task('some description', tomorrow)
    sut.add_task(task)

    calendar.today += timedelta(days=5)
    
    assert [task] == sut.overdue_tasks

def test_creation(sut):
    assert 0 == len(sut)
    assert [] == sut.due_tasks == sut.overdue_tasks == sut.finished_tasks

def test_adding_task_with_due_day_in_future(sut, tomorrow):
    task = Task('some description', tomorrow)

    sut.add_task(task)

    assert [task] == sut.due_tasks

def test_adding_task_with_due_day_in_past(yesterday, sut):
    task = Task("Finish Java stories.", yesterday)

    with pytest.raises(RuntimeError):
        sut.add_task(task)
        
def test_task_becomes_finished(tomorrow, sut):
    task = Task('some description', tomorrow)
    sut.add_task(task)

    task.finished = True

    assert [] == sut.due_tasks
    assert [task] == sut.finished_tasks