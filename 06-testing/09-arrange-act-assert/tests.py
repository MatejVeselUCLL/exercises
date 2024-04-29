from datetime import date, timedelta
from tasks import Task, TaskList
from calendars import CalendarStub
import pytest

def test_task_becomes_overdue():
    tomorrow = date(2001, 1, 1) + timedelta(days=1)
    task = Task('some description', tomorrow)
    calendar = CalendarStub(date(2001, 1, 1))
    tasks = TaskList(calendar)
    tasks.add_task(task)

    calendar.today = date(2001, 1, 1) + timedelta(days=2)
    
    assert [task] == tasks.overdue_tasks

def test_creation():
    # Arrange
    today = date(2001, 1, 1)
    calendar = CalendarStub(today)
    
    # Act
    sut = TaskList(calendar)

    # Assert
    assert 0 == len(sut)
    assert [] == sut.due_tasks == sut.overdue_tasks == sut.finished_tasks

    # sut.add_task(Task("Finish Java stories.", today + timedelta(days=2)))
    # sut.add_task(Task("Finish IT & Business report.", today + timedelta(days=8))))

def test_adding_task_with_due_day_in_future():
    today = date(2001, 1, 1)
    calendar = CalendarStub(today)
    sut = TaskList(calendar)
    task = Task("Finish Java stories.", today + timedelta(days=2))

    sut.add_task(task)

    assert [task] == sut.due_tasks

def test_adding_task_with_due_day_in_past():
    today = date(2001, 1, 1)
    calendar = CalendarStub(today)
    sut = TaskList(calendar)
    task = Task("Finish Java stories.", today - timedelta(days=2))


    with pytest.raises(RuntimeError):
        sut.add_task(task)
        
def test_task_becomes_finished():
    today = date(2001, 1, 1)
    calendar = CalendarStub(today)
    sut = TaskList(calendar)
    task = Task("Finish Java stories.", today + timedelta(days=2))
    sut.add_task(task)

    task.finished = True

    assert [] == sut.due_tasks
    assert [task] == sut.finished_tasks
