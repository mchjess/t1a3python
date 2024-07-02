import time
import csv
import sys

# Timer for tasks
class Activity:
    def __init__(self, name):
        self.name = name
        self.start_time = None
        self.total_time = 0
    
    def start(self):
        if self.start_time is None:
            self.start_time = time.time()
    
    def stop(self):
        if self.start_time is not None:
            self.total_time += time.time() - self.start_time
            self.start_time = None
    
    def get_time_spent(self):
        if self.start_time is not None:
            return self.total_time + time.time() - self.start_time
        return self.total_time 

# Task manager 
class ProductivityTracker:
    def __init__(self):
        self.activities = []
    
    def add_activity(self, name):
        self.activities.append(Activity(name))
        print("Current activities:")
        for activity in self.activities:
            print(f" - {activity.name}")
    
    def start_activity(self, name):
        for activity in self.activities:
            if activity.name == name:
                activity.start()
                print(f"Started activity: {name}")
                return
        print(f"Activity {name} not found.")
    
    def stop_activity(self, name):
        for activity in self.activities:
            if activity.name == name:
                activity.stop()
                print(f"Activity {name} stopped.")
                return
        print(f"Activity {name} not found.")
    
    def daily_summary(self):
        print("Daily summary:")
        for activity in self.activities:
            time_spent = activity.get_time_spent()
            print(f"{activity.name}: {time_spent / 60:.2f} minutes.")
    
    def export_csv(self, filename):
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Activity Name', 'Time Spent (minutes)'])
            for activity in self.activities:
                writer.writerow([activity.name, activity.get_time_spent() / 60])
        print(f"Data exported to {filename}")

# User interface
def main():
    tracker = ProductivityTracker()
    
    while True:
        print("\nMenu:")
        print("1. Add Activity")
        print("2. Start Activity")
        print("3. Stop Activity")
        print("4. Daily Summary")
        print("5. Export to CSV")
        print("6. Exit")
    
        choice = input("Please choose from the Menu options: ")
    
        if choice == '1':
            name = input("Enter activity name: ")
            tracker.add_activity(name)
        elif choice == '2':
            name = input("Enter activity name: ")
            tracker.start_activity(name)
        elif choice == '3':
            name = input("Enter activity name: ")
            tracker.stop_activity(name)
        elif choice == '4':
            tracker.daily_summary()
        elif choice == '5':
            filename = input("Enter a filename to save your report: ")
            tracker.export_csv(filename)
        elif choice == '6':
            print("Exiting the program. Goodbye.")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()