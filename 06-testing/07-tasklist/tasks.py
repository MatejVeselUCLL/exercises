from datetime import date, timedelta

class Task:
    def __init__(self, description, due_date):
        self.__description = description
        self.__due_date = due_date
        self.__finished = False
    
    @property
    def description(self):
        return self.__description
    
    @property
    def due_date(self):
        return self.__due_date
    
    @property
    def finished(self):
        return self.__finished
    @finished.setter
    def finished(self, finished):
        self.__finished = finished

    def __repr__(self):
        return f"{self.due_date}"


# from datetime import date
# task = Task('bake birthday cake', date(2023, 10, 1))
# print('bake birthday cake', task.description)
# print('datetime.date(2023, 10, 1)', task.due_date)
# print(False, task.finished)
# task.finished = True
# print(True, task.finished)

class TaskList:
    def __init__(self):
        self.task_list = []
    
    def add_task(self, task):
        if task.due_date < date.today():
            raise RuntimeError()
        self.task_list.append(task)

    def __len__(self):
        return len(self.task_list)
    
    @property
    def finished_tasks(self):
        return [task for task in self.task_list if task.finished]
    
    @property
    def due_tasks(self):
        return [task for task in self.task_list if not task.finished]
    
    @property
    def overdue_tasks(self):
        return [task for task in self.due_tasks if task.due_date < date.today()]
    
# from datetime import date, timedelta
# tasks = TaskList()
# print(0 == len(tasks))
# tomorrow = date.today() + timedelta(days=1)
# yesterday = date.today() - timedelta(days=1)
# # task_in_past = Task('some description', yesterday)
# # tasks.add_task(task_in_past)
# task = Task('some description', tomorrow)
# tasks.add_task(task)
# print(1 == len(tasks))
# print(0 == len(tasks.finished_tasks))
# print([task] == tasks.due_tasks)
# print(0 == len(tasks.overdue_tasks))
# print(0 == len(tasks.finished_tasks))
# print([task] == tasks.due_tasks)
# print([] == tasks.overdue_tasks)
# task.finished = True
# print([task] == tasks.finished_tasks)
# print(0 == len(tasks.due_tasks))
# print(0 == len(tasks.overdue_tasks))



