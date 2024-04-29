from datetime import date, timedelta
from tasks import Task, TaskList
from calendars import CalendarStub
import pytest

def create_today():
    return date(2001, 1, 1)

def create_tomorrow(today):
    return today + timedelta(days=1)

def create_yesterday(today):
    return today - timedelta(days=1)

def create_calendar(today):
    return CalendarStub(today)

def create_sut(calendar):
    return TaskList(calendar)

def create_task(*, description='some task', due_date=date(2000, 1, 1), finished=False):
    task = Task(description, due_date)
    if finished:
        task.finished = True
    return task



def test_task_becomes_overdue():
    today = create_today()
    task = create_task(due_date=create_tomorrow(today))
    calendar = create_calendar(today)
    sut = create_sut(calendar)
    sut.add_task(task)

    calendar.today += timedelta(days=5)
    
    assert [task] == sut.overdue_tasks

def test_creation():
    sut = create_sut(create_calendar(create_today()))

    assert 0 == len(sut)
    assert [] == sut.due_tasks == sut.overdue_tasks == sut.finished_tasks

def test_adding_task_with_due_day_in_future():
    today = create_today()
    sut = create_sut(create_calendar(today))
    task = create_task(due_date = create_tomorrow(today))

    sut.add_task(task)

    assert [task] == sut.due_tasks

def test_adding_task_with_due_day_in_past():
    today = create_today()
    sut = create_sut(create_calendar(today))
    task = create_task(due_date=create_yesterday(today))

    with pytest.raises(RuntimeError):
        sut.add_task(task)
        
def test_task_becomes_finished():
    today = create_today()
    sut = create_sut(create_calendar(today))
    task = create_task(due_date=create_tomorrow(today))
    sut.add_task(task)

    task.finished = True

    assert [] == sut.due_tasks
    assert [task] == sut.finished_tasks