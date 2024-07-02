### T1A3 - Terminal Application | Jessica McHenry

This terminal application has been created to meet the requirements of Coder Academy Term 1 Assignment 3.

This application is a Task Tracker and helps users to manage and report accurately on their productivity levels over a range of tasks. Users input their tasks and use the application's timer to time how long they spend doing each task. The application can then give a daily summary showing how much time was spent on which task. This report can also be exported to CSV.

The [Help Documentation]() contains instructions for installing and utilising the application.

This [Github repository](https://github.com/mchjess/t1a3python) was used for this application.

This [Trello board](https://trello.com/b/tQ73kRWU/implementation-plan) was used to manage the project.

### Table of Contents

* [Features of the application](#features)
    1. [Timer](#1-timer)
    2. [Daily Summary](#2-daily-summary)
    3. [Exportabe CSV report](#3-exportable-csv-report)

* [Code Style Guide](#style-guide)
* [Implementation Plan](#implementation-plan)
* [Testing](#testing)
* [Help Documentation](#help-documentation)
* [References](#references)

### Features

This application has many transferrable uses. It accurately measures time spent on a user-inputted task and then returns a summary of all time spent on all tasks. This application captures and reports data for the user to interpret as they see fit.

The application has a simple menu interface with options 1 - 5 to complete the following operations:

* Task Management: Add, start, and stop tasks. 
* Time Tracking: Record time spent on each task.
* Daily Summary: Generate daily summaries of time spent per task category.
* Data Export: Export task data to a CSV file for further analysis.

#### 1. Timer

Users start and stop the timer after they have added the task they wish to track. The application relies on the user to initiate the timer and they must input the correct commands.

#### 2. Daily Summary

Users can access a Daily Summary of all tasks and time spent on the fly as they need it. Although this is called a 'daily' summary, this feature is really an intermittent summary which the user can choose to access at any time.

#### 3. Exportable CSV report

Users also have the option of exporting their summary data to a CSV report which they can separately store and review or input into applications like Excel for more detailed reporting and record storage.

### Style Guide

I have applied the standard style guide for [Python PEP 8](https://peps.python.org/pep-0008/).

The following conventions are adhered to in accordance with this style guide:

* Indentation - 4 spaces used for each level of indentation consistently throughout your code.
* Line length - lines are limited to 79 characters whereever possible.
* Naming conventions - I have used snake_case for functions and variables (add_task, start_task) and CamelCase for classes (ProductivityTracker, Task).
* Imports - libraries used listed on separate lines at the top of my file.

### Implementation Plan

### Testing

Once the application was fully coded, I tested the Menu functionality to ensure that all options worked. The following summary includes all testing and debugging required.

1. Tested adding tasks.
    First test - failed.
    Initial issue with tasks not saving to the list of tasks. Error addressed with syntax change and addition of confirmation of task added. 
    
    Second test - passed.

 2. Tested starting tasks.
    First test - passed.

3. Tested stopping tasks.
    First test - failed.
    Initial issue with timer. Syntax changed and error addressed.

    Second test - passed.

 4. Tested viewing the daily summary.

 5. Tested exporting to CSV.
    First test - passed.

 6. Ensured the exit option works.
    First test - passed.

### Help Documentation

### References



