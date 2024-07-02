import time

class Task:
    #Starts new task and includes name and category for reporting.
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