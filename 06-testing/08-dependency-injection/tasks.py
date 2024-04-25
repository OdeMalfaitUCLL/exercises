from calendars import Calendar
from datetime import date, timedelta
class Task:
    def __init__(self,description,due_date):
        self.__description = description
        self.__due_date = due_date
        self.finished = False

    @property
    def description(self):
        return self.__description
    @property
    def due_date(self):
        return self.__due_date


# task = Task('bake birthday cake', date(2023, 10, 1))
# print(task.description)
# print(task.due_date)
# print(task.finished)
# task.finished = True
# print(task.finished)

class TaskList:
    def __init__(self,calendar):
        self.__task_list = []
        self.__calendar = calendar

    def add_task(self,task):
        if task.due_date < self.__calendar.today:
            raise RuntimeError("due date can not be in the future.")
        self.__task_list.append(task)
    def __len__(self):
        return len(self.__task_list)
    @property
    def finished_tasks(self):
        return [task for task in self.__task_list if task.finished]
    @property
    def due_tasks(self):
        return [task for task in self.__task_list if not task.finished]
    @property
    def overdue_tasks(self):
        return [task for task in self.__task_list if not task.finished
                and task.due_date < self.__calendar.today]
calendar = Calendar()
tasks = TaskList(calendar)
print(len(tasks))
tomorrow = date.today() + timedelta(days=1)
# yesterday = date.today() - timedelta(days=1)
# # task_in_past = Task('some description', yesterday)
# tasks.add_task(task_in_past)
task = Task('some description', tomorrow)
tasks.add_task(task)
print(len(tasks))
print(tasks.finished_tasks)
print(tasks.due_tasks)
task.finished = True
print(tasks.due_tasks)
print(tasks.overdue_tasks)