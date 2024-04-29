from datetime import date, timedelta
from tasks import Task, TaskList
from calendars import CalendarStub

def test_task_becomes_overdue():
    tomorrow = date.today() + timedelta(days=1)
    task = Task('some description', tomorrow)
    calendar = CalendarStub(date.today())
    tasks = TaskList(calendar)
    tasks.add_task(task)

    calendar.today = date.today() + timedelta(days=2)
    assert [task] == tasks.overdue_tasks