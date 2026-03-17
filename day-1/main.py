
# ----------------------------------------------------------------------------------------------------------
print("to-do list")  # greeitngs 
task = [] 
status=[]
total_tasks=int(input("how many tasks are there:" )) # it get the number of tasks to finalize the len of the list fo rexit the programme when it hit the len
for i in range(total_tasks):   # loop that process the transfer of the user input to lists that will be used in future actions of the programme 
    user_task=input("add the task to get done:" )
    task.append(user_task)
    task_status=input("what the status of the task? (done/in progress/pending):" )
    status.append(task_status)# this line converts the task and status lists into tepmorary tuple to put it in dictionary format using zip function
# lot=dict(zip(task, status)) # list of tasks = 'lot'
# -------------------------------------------------------------------------------------------------
#this part of the code works to view the dictionary of the tasks with their status 
# view=input("view the list of the tasks! (y/n?):" )
# if view=="y":
        # print(lot)
# elif view!="y":
    #   print("okay, your to-do list is super-private.just trust us")
# -------------------------------------------------------------------------------------------
# this part removes the tasks from the task and status lists 
# rm=input('do you want to remove any tasks? (y/n?):' )
# norm= input("spell the task you want to remove:" )
# if rm=="y":
    #   del lot[norm]
# elif rm!="y":
#     #   print('keep all the tasks and never get them done!!!!')
# print(lot)
# pot=dict(zip(task ,status)) # post operational task = 'pot' 


# print(pot)

# -------------------------------------------------------------------



















































#sample code block to understand how dictionaries and zip function works to implement it in  main codebase


# a=[]
# b=[]
# for i in range (3):
#     a1=input("inset the tasks:")
#     b1=input("inset the status of the task:done/pending")
#     a.append(a1)
#     b.append(b1)

# z=dict(zip(a,b))

# print(z)



