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
    # New task list
    def __init__(self):
        self.tasks = []
    
    # Adding a task
    def add_task(self, name, category):
        self.tasks.append(Task(name,category))
    
    # Starting the task
    def start_task(self, name):
        for task in self.tasks:
            if task.name == name:
                task.start()
                print(f"Started task: {name}")
                return
            print(f"Task {name} not found.")
    
    # Stopping the task
    def stop_task(self,name):
        for task in self.tasks:
            if task.name == name:
                task.stop()
                print(f"Task {name} stopped.")
                return
            print(f"Task {name} not found.")
    
    # Daily summary
    def daily_summary(self):
        summary = {}
        for tasks in self.tasks:
            time_spent = tasks.get_time_spent()
            if task.category in summary:
                summary[task.category] += time_spent
            else:
                summary[task.category] = time_spent
                
        print("Daily summary:")
        for category, time_spent in summary.items():
            print(f"{category}: {time_spent/60:2f} minutes.")
    
    #Exportable CSV report
    def export_csv(self,filename):
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Task Name','Category', 'Time Spent (minutes)'])
            for task in self.tasks:
                writer.writerow([task.name, task.catefory, task.get_time_spent()/60])
        print(f"Data exported to {filename}")