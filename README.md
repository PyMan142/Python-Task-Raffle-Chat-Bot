# Python-Task-Raffle-Chat-Bot
This is a bot for chat memebers to create tasks. Every completed task enters the user into a raffle. You can run the !pickwinner command to pick a winner from the list of users that have completed a task. 

# Setup
pip install -U twitchio
Must be python version 3.7+ (Or higher)

#User Commands
!help - List all commands for the users

!task [title] - Create a new task - This also enters you into the raffle!

!active - Lists your active tasks
!alldone - Complete ALL of your active tasks
!complete [id]- Complete the task by targeting the id of it
!completed - Lists your completed tasks
!delete [id]- Delete the task by targeting the id of it
!activefull - Lists your active tasks in full detail
!completedfull - Lists your completed tasks in full detail
!completedold - List your old completed tasks
!activeuser [username] - Lists the active tasks of a user
!completed [username] - Lists the completed tasks of a user
!top [number]- List [number] users who've completed the most tasks

#Admin Commands
!helpadmin - List allll the admin commands
!alltasks - Return everything about all entries
!allactive - Returns all active tasks
!allcompleted - Returns all completed tasks
!activecount - Get usernames & the total number of active tasks for each user
!completedcount - Get usernames & the total number of completed tasks for each user
!oldcompletedcount - List all users and count for total amount of old completed tasks
!generate [username] [title]- Create a new task for a ghost user
!admincomplete [id] [username] - Complete the active task by [id] and pass in [username]
!admindelete [id] - Delete the task by [id]
!pickwinner - Pick a random winner from the list of completed entries & update the database
!winners - Lists all previous winners
!deleteall - Delete every task from the database
!setallold - Set all tasks as old, and start a new raffle pool, use this after a winner has been picked
!allold - List all old tasks, completed or not
!alloldcompleted - List all old completed tasks for everyone
!completedolduser - Old completed tasks for a specific user
!droptable - Drop your table, delete literally everything, be careful
