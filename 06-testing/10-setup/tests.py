from datetime import date, timedelta
from tasks import Task, TaskList
from calendars import CalendarStub
import pytest

def setup_function():
    global today, yesterday, tomorrow, calendar, sut
    today = date(2001, 1, 1)
    yesterday = today - timedelta(days=1)
    tomorrow = today + timedelta(days=1)
    calendar = CalendarStub(today)
    sut = TaskList(calendar)

def test_task_becomes_overdue():
    task = Task('some description', tomorrow)
    sut.add_task(task)

    calendar.today = tomorrow + timedelta(days=1)
    
    assert [task] == sut.overdue_tasks

def test_creation():
    assert 0 == len(sut)
    assert [] == sut.due_tasks == sut.overdue_tasks == sut.finished_tasks

def test_adding_task_with_due_day_in_future():
    task = Task('some description', tomorrow)

    sut.add_task(task)

    assert [task] == sut.due_tasks

def test_adding_task_with_due_day_in_past():
    task = Task("Finish Java stories.", yesterday)

    with pytest.raises(RuntimeError):
        sut.add_task(task)
        
def test_task_becomes_finished():
    task = Task('some description', tomorrow)
    sut.add_task(task)

    task.finished = True

    assert [] == sut.due_tasks
    assert [task] == sut.finished_tasks
