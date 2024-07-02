import time
import csv


#Timer 

class Task:
    #Creates new task and includes name and category for reporting.
    def __init__(self, name, category) :
        self.name = name
        self.category = category
        self.start_time = None
        self.total_time = 0
    
    # Timer start
    def start(self):
        if self.start_time is None:
            self.start_time = time.time()
    
    # Timer stop
    def stop(self):
        if self.start_time is not None:
            self.total_time += time.time() - self.start
            self.start_time = None
    
    # Returns the total time spent on a task.
    def get_time_spent(self):
        if self.start is not None:
            return self.total_time + time.time() - self.start_time 
        return self.total_time 

#Task manager

class ProductivityTracker:
    def __init__(self):
        self.tasks = []
    
    #Adding a task
    def add_task(self, name, category):
        self.tasks.append(Task(name,category))
    
    #Starting the task
    def start_task(self, name):
        for task in self.tasks:
            if task.name == name:
                task.start()
                print(f"Started task: {name}")
                return
            print(f"Task {name} not found.")
    
    #Stopping the task
    def stop_task(self,name):
        for task in self.tasks:
            if task.name == name:
                task.stop()
                print(f"Task {name} stopped.")
                return
            print(f"Task {name} not found.")