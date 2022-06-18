from twitchio.ext import commands
from twitchio.client import Client
from datetime import datetime , time , date, timedelta
from dbfunctions import *
from keys import *
from random import randint

# The main controller you'll be using for most things
bot = commands.Bot(
    token = irctoken,
    client_id = clientid,
    nick = '', # This is the username of the bot account
    prefix = '!',
    initial_channels=[''] # You can add this in ANYONES channel O.o BE CAREFUL - Enter your channel name here
)

#If you need to access the client 
client = Client(
    token = irctoken,
    client_secret = clientsecret
)

#List help tasks
@bot.command(name='help')
async def test_command(ctx):

    user = ctx.author.name    
    await ctx.send(f"Hey {user}, here is the list of commands")
    await ctx.send(f"!task [title]- Create a new task - This also enters you into the raffle!")
    await ctx.send(f"!active - Lists your active tasks.")
    await ctx.send(f"!alldone - Complete ALL of your active tasks.")
    await ctx.send(f"!complete [id]- Complete the task by targeting the id of it")
    await ctx.send(f"!completed - Lists your completed tasks.")
    await ctx.send(f"!delete [id]- Delete the task by targeting the id of it")
    await ctx.send(f"!activefull - Lists your active tasks in full detail")
    await ctx.send(f"!completedfull - Lists your completed tasks in full detail")
    await ctx.send(f"!completedold - List your old completed tasks")
    await ctx.send(f"!activeuser [username] - Lists the active tasks of a user")
    await ctx.send(f"!completed [username] - Lists the completed tasks of a user")
    await ctx.send(f"!top [number]- List [number] users who've completed the most tasks")

#Create a new task
@bot.command(name='task')
async def test_command(ctx, *, msg=''):

    user = ctx.author.name    
    task = msg
    startdate = datetime.now().strftime("%B %d, %Y %I:%M%p")
    finishdate = 0
    completed = 0
    winner = 0
    winning_date = 0
    old = 0

    if msg == '':
        await ctx.send(f"Sorry {user}, you cannot add a blank task.")
    else:
        await ctx.send(f"{user} - Task: {task} - Started on: {startdate}")
        new_task(user, task, startdate, finishdate, completed, winner, winning_date, old)

#Get the top completionists!
@bot.command(name='top')
async def test_command(ctx, arg):

    results = top(arg)

    for x in results:
        x = list(x)
        result_user, result_count = x[0], x[1]
        await ctx.send(f"{result_user} {result_count}")

#Active tasks for the user
@bot.command(name='active')
async def test_command(ctx):

    user = ctx.author.name
    thecount = get_active_count(user)
    howmanytasks = thecount[0]
    results = get_active(user)

    for x in results:
        x = list(x)
        result_id, result_user, result_task, result_startdate, result_finishdate = x[0], x[1], x[2], x[3], x[4]

    if thecount[0] == 0:
        await ctx.send(f"Hey {user}, you don't have any tasks!")

    if thecount[0] == 1:
        await ctx.send(f"Hey {result_user}, you currently have {howmanytasks} ongoing task :)")
    
        for x in results:
            x = list(x)
            result_id, result_user, result_task, result_startdate, result_finishdate = x[0], x[1], x[2], x[3], x[4]
            #result_all= f"{result_id}, {result_user}, {result_task}, {result_startdate}, {result_finishdate}"
            await ctx.send(f'{result_user} - {result_task} - ID: {result_id} - Started on: {result_startdate}')
    
    if thecount[0] > 1:
        await ctx.send(f"Hey {result_user}, you currently have {howmanytasks} ongoing tasks NotLikeThis")
        
        for x in results:
            x = list(x)
            result_id, result_user, result_task, result_startdate, result_finishdate = x[0], x[1], x[2], x[3], x[4]
            #result_all= f"{result_id}, {result_user}, {result_task}, {result_startdate}, {result_finishdate}"
            await ctx.send(f'{result_user} - {result_task} - ID: {result_id} - Started on: {result_startdate}')

#Active tasks for the user
@bot.command(name='activeuser')
async def test_command(ctx, arg):

    user = ctx.author.name
    thecount = get_active_count(arg)
    howmanytasks = thecount[0]
    results = get_active(arg)

    for x in results:
        x = list(x)
        result_id, result_user, result_task, result_startdate, result_finishdate = x[0], x[1], x[2], x[3], x[4]

    if thecount[0] == 0:
        await ctx.send(f"{arg} doesn't have any active tasks!")

    if thecount[0] == 1:
        await ctx.send(f"{result_user}, currently has {howmanytasks} ongoing task :)")
    
        for x in results:
            x = list(x)
            result_id, result_user, result_task, result_startdate, result_finishdate = x[0], x[1], x[2], x[3], x[4]
            #result_all= f"{result_id}, {result_user}, {result_task}, {result_startdate}, {result_finishdate}"
            await ctx.send(f'{result_user} - {result_task} - ID: {result_id}')
    
    if thecount[0] > 1:
        await ctx.send(f"{result_user}, currently has {howmanytasks} ongoing tasks NotLikeThis")
        
        for x in results:
            x = list(x)
            result_id, result_user, result_task, result_startdate, result_finishdate = x[0], x[1], x[2], x[3], x[4]
            #result_all= f"{result_id}, {result_user}, {result_task}, {result_startdate}, {result_finishdate}"
            await ctx.send(f'{result_user} - {result_task} - ID: {result_id}')

#Active tasks for the user with all the data
@bot.command(name='activefull')
async def test_command(ctx):

    user = ctx.author.name
    thecount = get_active_count(user)
    howmanytasks = thecount[0]
    results = get_active(user)

    for x in results:
        x = list(x)
        result_id, result_user, result_task, result_startdate, result_finishdate = x[0], x[1], x[2], x[3], x[4]

    if thecount[0] == 1:
        await ctx.send(f"Hey {result_user}, you currently have {howmanytasks} active task :)")

        for x in results:
            x = list(x)
            result_id, result_user, result_task, result_startdate, result_finishdate = x[0], x[1], x[2], x[3], x[4]
            #result_all= f"{result_id}, {result_user}, {result_task}, {result_startdate}, {result_finishdate}"
            await ctx.send(f'{result_user} -  {result_task} -  Started: {result_startdate} EST - ID: {result_id}')

    if thecount[0] > 1:
        await ctx.send(f"Hey {result_user}, you currently have {howmanytasks} active tasks NotLikeThis")

        for x in results:
            x = list(x)
            result_id, result_user, result_task, result_startdate, result_finishdate = x[0], x[1], x[2], x[3], x[4]
            #result_all= f"{result_id}, {result_user}, {result_task}, {result_startdate}, {result_finishdate}"
            await ctx.send(f'{result_user} -  {result_task} -  Started: {result_startdate} EST - ID: {result_id}')

    if thecount[0] == 0:
        await ctx.send(f"Hey {user}, you don't have any tasks!")

#Completed tasks for the user
@bot.command(name='completed')
async def test_command(ctx):

    user = ctx.author.name
    thecount = get_completed_count(user)
    howmanytasks = thecount[0]
    results = get_completed(user)

    for x in results:
        x = list(x)
        result_id, result_user, result_task, result_startdate, result_finishdate = x[0], x[1], x[2], x[3], x[4]

    if thecount[0] == 0:
        await ctx.send(f"Sorry {user}, you don't have any completed tasks :(")

    if thecount[0] == 1:
        await ctx.send(f"Hey {result_user}, you have {howmanytasks} completed task! PogChamp")
    
        for x in results:
            x = list(x)
            result_id, result_user, result_task, result_startdate, result_finishdate = x[0], x[1], x[2], x[3], x[4]
            #result_all= f"{result_id}, {result_user}, {result_task}, {result_startdate}, {result_finishdate}"
            await ctx.send(f'{result_user} - {result_task} - ID: {result_id}')
    
    if thecount[0] > 1:
        await ctx.send(f"Hey {result_user}, you have {howmanytasks} completed tasks! PogChamp")
        
        for x in results:
            x = list(x)
            result_id, result_user, result_task, result_startdate, result_finishdate = x[0], x[1], x[2], x[3], x[4]
            #result_all= f"{result_id}, {result_user}, {result_task}, {result_startdate}, {result_finishdate}"
            await ctx.send(f'{result_user} - {result_task} - ID: {result_id}')

#Completed tasks for the user
@bot.command(name='completeduser')
async def test_command(ctx, arg):

    user = ctx.author.name
    thecount = get_completed_count(arg)
    howmanytasks = thecount[0]
    results = get_completed(arg)

    for x in results:
        x = list(x)
        result_id, result_user, result_task, result_startdate, result_finishdate = x[0], x[1], x[2], x[3], x[4]

    if thecount[0] == 0:
        await ctx.send(f"{arg} doesn't have any completed tasks!")

    if thecount[0] == 1:
        await ctx.send(f"{result_user}, currently has {howmanytasks} completed task :)")
    
        for x in results:
            x = list(x)
            result_id, result_user, result_task, result_startdate, result_finishdate = x[0], x[1], x[2], x[3], x[4]
            #result_all= f"{result_id}, {result_user}, {result_task}, {result_startdate}, {result_finishdate}"
            await ctx.send(f'{result_user} - {result_task} - ID: {result_id} - Stared on: {result_startdate} - Finished on: {result_finishdate}')
    
    if thecount[0] > 1:
        await ctx.send(f"{result_user}, has completed {howmanytasks} tasks PogChamp")
        
        for x in results:
            x = list(x)
            result_id, result_user, result_task, result_startdate, result_finishdate = x[0], x[1], x[2], x[3], x[4]
            #result_all= f"{result_id}, {result_user}, {result_task}, {result_startdate}, {result_finishdate}"
            await ctx.send(f'{result_user} - {result_task} - ID: {result_id} - Stared on: {result_startdate} - Finished on: {result_finishdate}')

#Old completed tasks for the user
@bot.command(name='completedold')
async def test_command(ctx):

    user = ctx.author.name
    thecount = get_old_completed_count(user)
    howmanytasks = thecount[0]
    results = get_old_completed(user)

    for x in results:
        x = list(x)
        result_id, result_user, result_task, result_startdate, result_finishdate = x[0], x[1], x[2], x[3], x[4]

    if thecount[0] == 0:
        await ctx.send(f"Sorry {user}, you don't have any old completed tasks :(")

    if thecount[0] == 1:
        await ctx.send(f"Hey {result_user}, you have {howmanytasks} old completed task!")
    
        for x in results:
            x = list(x)
            result_id, result_user, result_task, result_startdate, result_finishdate = x[0], x[1], x[2], x[3], x[4]
            #result_all= f"{result_id}, {result_user}, {result_task}, {result_startdate}, {result_finishdate}"
            await ctx.send(f'{result_user} - {result_task} - ID: {result_id} - Finishdate: {result_finishdate}')
    
    if thecount[0] > 1:
        await ctx.send(f"Hey {result_user}, you have {howmanytasks} old completed tasks! PogChamp")
        
        for x in results:
            x = list(x)
            result_id, result_user, result_task, result_startdate, result_finishdate = x[0], x[1], x[2], x[3], x[4]
            #result_all= f"{result_id}, {result_user}, {result_task}, {result_startdate}, {result_finishdate}"
            await ctx.send(f'{result_user} - {result_task} - ID: {result_id} - Finishdate: {result_finishdate}')

#Active tasks for the user with all the data
@bot.command(name='completedfull')
async def test_command(ctx):

    user = ctx.author.name
    thecount = get_completed_count(user)
    howmanytasks = thecount[0]
    results = get_completed(user)

    for x in results:
        x = list(x)
        result_id, result_user, result_task, result_startdate, result_finishdate = x[0], x[1], x[2], x[3], x[4]

    if thecount[0] == 1:
        await ctx.send(f"Hey {result_user}, you have {howmanytasks} completed task :)")

        for x in results:
            x = list(x)
            result_id, result_user, result_task, result_startdate, result_finishdate = x[0], x[1], x[2], x[3], x[4]
            #result_all= f"{result_id}, {result_user}, {result_task}, {result_startdate}, {result_finishdate}"
            await ctx.send(f'{result_user} -  {result_task} ID: {result_id} - Started: {result_startdate} EST - Finished: {result_finishdate} EST')

    if thecount[0] > 1:
        await ctx.send(f"Hey {result_user}, you have {howmanytasks} completed tasks SeemsGood")

        for x in results:
            x = list(x)
            result_id, result_user, result_task, result_startdate, result_finishdate = x[0], x[1], x[2], x[3], x[4]
            #result_all= f"{result_id}, {result_user}, {result_task}, {result_startdate}, {result_finishdate}"
            await ctx.send(f'{result_user} -  {result_task} -  ID: {result_id} - Started: {result_startdate} EST - Finished: {result_finishdate} EST')

    if thecount[0] == 0:
        await ctx.send(f"Hey {user}, you don't have any completed tasks :(")

#Complete task by ID for user
@bot.command(name='complete')
async def test_command(ctx, arg):
    finishdate = datetime.now().strftime("%B %d, %Y %I:%M%p")
    user = ctx.author.name

    complete_task(finishdate, arg, user)

    check = check_if_complete_task(arg)

    for x in check:
        x = list(x)

    if x[0] > 0: 
        await ctx.send(f"Task {arg} for {user} has been completed <3")
    else:
        await ctx.send(f"I had a problem doing this, please make sure it's !complete [id] and it was entered properly")

#Complete all active tasks for user
@bot.command(name='alldone')
async def test_command(ctx):
    finishdate = datetime.now().strftime("%B %d, %Y %I:%M%p")
    user = ctx.author.name
        
    try:
        results = get_active(user)
        thecount = get_active_count(user)
    except Exception as e:
        print(e)
    else:
        howmanytasks = thecount[0]

        if howmanytasks > 0:
            for x in results:
                x = list(x)
                result_id, result_user, result_task, result_startdate, result_finishdate = x[0], x[1], x[2], x[3], x[4]
                await ctx.send(f'Marking task - "{result_task}" as completed!')

        howmany = complete_all_tasks(finishdate, user)
        totalhowmany = howmany[1]

        howmanycompleted = get_completed_count(user)
        totalcompleted = howmanycompleted[0]

        await ctx.send(f'Marked {totalhowmany} tasks completed for {user}, you now have {totalcompleted} completed tasks <3')

#Delete the task by ID
@bot.command(name='delete')
async def test_command(ctx, arg):

    user = ctx.author.name
    delete_task(arg, user)

#############################################
############### ADMIN CMDS ##################
#############################################

#List admin cmds
@bot.command(name='helpadmin')
async def test_command(ctx):
    user = ctx.author.name
    ismod = ctx.author.is_mod

    if ismod == True:
        await ctx.send(f"Nice to see you, {user}, here's all the admin commands :)")
        await ctx.send(f"!alltasks - Return everything about all entries")
        await ctx.send(f"!allactive - Returns all active tasks")
        await ctx.send(f"!allcompleted - Returns all completed tasks")
        await ctx.send(f"!activecount - Get usernames & the total number of active tasks for each user")
        await ctx.send(f"!completedcount - Get usernames & the total number of completed tasks for each user")
        await ctx.send(f"!oldcompletedcount - List all users and count for total amount of old completed tasks")
        await ctx.send(f"!generate [username] [title]- Create a new task for a ghost user")
        await ctx.send(f"!admincomplete [id] [username] - Complete the active task by [id] and pass in [username]")
        await ctx.send(f"!admindelete [id] - Delete the task by [id]")
        await ctx.send(f"!pickwinner - Pick a random winner from the list of completed entries & update the database <3")
        await ctx.send(f"!winners - Lists all previous winners <3")
        await ctx.send(f"!deleteall - Delete every task from the database")
        await ctx.send(f"!setallold - Set all tasks as old, and start a new raffle pool, use this after a winner has been picked")
        await ctx.send(f"!allold - List all old tasks, completed or not")
        await ctx.send(f"!alloldcompleted - List all old completed tasks for everyone")
        await ctx.send(f"!completedolduser - Old completed tasks for a specific user")
        await ctx.send(f"!droptable - Drop your table, delete literally everything, be careful")
    else:
        await ctx.send(f"Sorry {user}, but you don't have access to use this command :(")

#Everyones tasks, active & completed - mod cmd
@bot.command(name='alltasks')
async def test_command(ctx):

    user = ctx.author.name
    ismod = ctx.author.is_mod
    results = get_all()

    for x in results:
        x = list(x)
        #Not going to define all, but can use as needed :) 
        result_id, result_user, result_task, result_startdate, result_finishdate, result_completed, result_winner, result_winning_date, result_old = x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8]

    if ismod == True:
        for x in results:
            x = list(x)
            result_id, result_user, result_task, result_startdate, result_finishdate = x[0], x[1], x[2], x[3], x[4]
            await ctx.send(f'{result_user} -  {result_task} -  Started: {result_startdate} EST - Finished: {result_finishdate} EST - ID: {result_id}')
    else:
        await ctx.send(f"Sorry {user}, but you don't have access to use this command :(")

#Everyones active tasks
@bot.command(name='allactive')
async def test_command(ctx):

    user = ctx.author.name
    ismod = ctx.author.is_mod
    results = get_all_active()

    for x in results:
        x = list(x)
        result_id, result_user, result_task, result_startdate, result_finishdate = x[0], x[1], x[2], x[3], x[4]

    if ismod == True:
        for x in results:
            x = list(x)
            result_id, result_user, result_task, result_startdate, result_finishdate = x[0], x[1], x[2], x[3], x[4]
            await ctx.send(f'{result_user} -  {result_task} -  Started: {result_startdate} EST - ID: {result_id}')
    else:
        await ctx.send(f"Sorry {user}, but you don't have access to use this command :(")

#Everyones completed tasks
@bot.command(name='allcompleted')
async def test_command(ctx):

    user = ctx.author.name
    ismod = ctx.author.is_mod
    results = get_all_completed()

    if ismod == True:
        itteration = 0
        for x in results:
            itteration += 1
            x = list(x)
            result_id, result_user, result_task, result_startdate, result_finishdate = x[0], x[1], x[2], x[3], x[4]
            if results == []:
                await ctx.send(f'No completed tasks / entries currently')
            else:
                await ctx.send(f'#{itteration} - {result_user} -  {result_task} -  Started: {result_startdate} EST - Finished: {result_finishdate} EST - ID: {result_id}')
    else:
        await ctx.send(f"Sorry {user}, but you don't have access to use this command :(")

#Everyones active tasks with count
@bot.command(name='activecount')
async def test_command(ctx):

    user = ctx.author.name
    ismod = ctx.author.is_mod
    results = get_all_active_count()

    for x in results:
        x = list(x)
        result_user, result_qty  = x[0], x[1]

    if ismod == True:
        for x in results:
            x = list(x)
            result_user, result_qty = x[0], x[1]

            if result_qty == 1:
                await ctx.send(f'{result_user} has {result_qty} active task!')
            if result_qty > 1:
                await ctx.send(f'{result_user} has {result_qty} active tasks!')
    else:
        await ctx.send(f"Sorry {user}, but you don't have access to use this command :(")

#Everyones completed task count
@bot.command(name='completedcount')
async def test_command(ctx):

    user = ctx.author.name
    ismod = ctx.author.is_mod
    results = get_all_completed_count()

    for x in results:
        x = list(x)
        result_user, result_qty  = x[0], x[1]

    if ismod == True:
        for x in results:
            x = list(x)
            result_user, result_qty = x[0], x[1]

            if result_qty == 1:
                await ctx.send(f'{result_user} has {result_qty} completed task!')
            if result_qty > 1:
                await ctx.send(f'{result_user} has {result_qty} completed tasks!')
    else:
        await ctx.send(f"Sorry {user}, but you don't have access to use this command :(")

#List all users and count for total amount of old completed tasks
@bot.command(name='oldcompletedcount')
async def test_command(ctx):

    user = ctx.author.name
    ismod = ctx.author.is_mod
    results = get_all_old_completed_count()

    for x in results:
        x = list(x)
        result_user, result_qty  = x[0], x[1]

    if ismod == True:
        for x in results:
            x = list(x)
            result_user, result_qty = x[0], x[1]

            if result_qty == 1:
                await ctx.send(f'{result_user} has {result_qty} completed old task!')
            if result_qty > 1:
                await ctx.send(f'{result_user} has {result_qty} completed dol tasks!')
    else:
        await ctx.send(f"Sorry {user}, but you don't have access to use this command :(")

#Complete task by ID
@bot.command(name='admincomplete')
async def test_command(ctx, arg, arg2):

    user = ctx.author.name
    ismod = ctx.author.is_mod

    if ismod == True:
        finishdate = datetime.now().strftime("%B %d, %Y %I:%M%p")
        chatter = arg2

        complete_task(finishdate, arg, chatter)

        check = check_if_complete_task(arg)

        for x in check:
            x = list(x)

        if x[0] > 0: 
            await ctx.send(f"I completed task {arg} for {arg2} <3")
        else:
            await ctx.send(f"I had a problem doing this, please make sure it's !admincomplete [id] [username]")

    else:
        await ctx.send(f"Sorry {user}, but you don't have permission to use this command :(")

#Delete the task by ID
@bot.command(name='admindelete')
async def test_command(ctx, arg, arg2):

    user = ctx.author.name
    ismod = ctx.author.is_mod

    if ismod == True:
        delete_task(arg, arg2)
        await ctx.send(f"Hey {user}, I deleted task {arg} <3")
    else:
        await ctx.send(f"Sorry {user}, but you don't have permission to use this command :(")

#Pick a winner!
@bot.command(name='pickwinner')
async def test_command(ctx):

    howmany = 0
    results = get_all_completed()

    user = ctx.author.name
    ismod = ctx.author.is_mod

    if ismod == True:
        for x in results:
            x = list(x)
            howmany += 1

        winningnumber = random.randint(0, howmany) - 1
        print(f'winningnumber == {winningnumber}')
        winner = results[winningnumber][1]
        
        winningid = results[winningnumber][0]
        new = winningnumber + 1
        winning_date = datetime.now().strftime("%B %d, %Y %I:%M%p")

        try:
            set_winner(winning_date, winningid, winner)
        except Exception as e:
            print(e)
        else:
            await ctx.send(f"The winner is - {winner}, we had {howmany} entries, winning number was {new}, and the winning entry was ID#{winningid}")

    else:
        await ctx.send(f"Sorry {user}, but you don't have permission to use this command :(")

#Show the winners
@bot.command(name='winners')
async def test_command(ctx):
    user = ctx.author.name
    ismod = ctx.author.is_mod
    results = show_winners()

    if ismod == True:
        for x in results:
            x = list(x)
            result_user, result_task, result_id, result_winning_date  = x[0], x[1], x[2], x[3]

            await ctx.send(f"{result_user}'s winning task was: '{result_task}', on '{result_winning_date}',and ID was '{result_id}' <3")
    else:
        await ctx.send(f"Sorry {user}, but you don't have access to use this command :(")

#Create a new task for a ghost
@bot.command(name='generate')
async def test_command(ctx, arg, *, msg=''):

    user = ctx.author.name
    ismod = ctx.author.is_mod

    task = msg
    startdate = datetime.now().strftime("%B %d, %Y %I:%M%p")
    finishdate = 0
    completed = 0
    winner = 0

    if ismod == True:
        if msg == '':
            await ctx.send(f"Sorry {user}, you cannot add a blank task.")
        else:
            await ctx.send(f"{arg} - Task: {task} - Started on: {startdate}")
            new_task(arg, task, startdate, finishdate, completed, winner)
    else:
        await ctx.send(f"Sorry {user}, but you don't have permission to use this command :(")

#Delete every task from the database
@bot.command(name='deleteall')
async def test_command(ctx,):

    user = ctx.author.name
    ismod = ctx.author.is_mod
    if ismod == True:

        try:
            howmany = delete_all_tasks()
        except Exception as e:
            print(e)
        else:
            await ctx.send(f"Deleted {howmany} rows!")
    else:
        await ctx.send(f"Sorry {user}, but you don't have permission to use this command :(")

#Set all tasks as old, and start a new raffle pool
@bot.command(name='setallold')
async def test_command(ctx,):

    user = ctx.author.name
    ismod = ctx.author.is_mod

    if ismod == True:

        try:
            howmany = set_all_old()
        except Exception as e:
            print(e)
        else:
            await ctx.send(f"Set {howmany} rows as old!")
    else:
        await ctx.send(f"Sorry {user}, but you don't have permission to use this command :(")

#Get all old tasks, completed or not
@bot.command(name='allold')
async def test_command(ctx,):

    user = ctx.author.name
    ismod = ctx.author.is_mod

    if ismod == True:
        try:
            results = get_all_old()
        except Exception as e:
            print(e)
        else:
            for x in results:
                x = list(x)
                result_id, result_user, result_task, result_startdate, result_finishdate, result_completed, result_winner, result_winning_date  = x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7]
                await ctx.send(f'User: {result_user}, ID: {result_id}, Task: {result_task}, Started: {result_startdate}, Finished: {result_finishdate}, Completed: {result_completed}, Winner: {result_winner}, Winning Date: {result_winning_date}')
    else:
        await ctx.send(f"Sorry {user}, but you don't have access to use this command :(")

#Get all old completed tasks for everyone
@bot.command(name='alloldcompleted')
async def test_command(ctx,):

    user = ctx.author.name
    ismod = ctx.author.is_mod

    if ismod == True:
        try:
            results = get_all_old_completed()
        except Exception as e:
            print(e)
        else:
            for x in results:
                x = list(x)
                result_id, result_user, result_task, result_startdate, result_finishdate, result_completed, result_winner, result_winning_date  = x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7]
                await ctx.send(f'User: {result_user}, ID: {result_id}, Task: {result_task}, Started: {result_startdate}, Finished: {result_finishdate}, Completed: {result_completed}, Winner: {result_winner}, Winning Date: {result_winning_date}')
    else:
        await ctx.send(f"Sorry {user}, but you don't have access to use this command :(")

#Old completed tasks for a specific user
@bot.command(name='completedolduser')
async def test_command(ctx, arg):

    user = arg
    thecount = get_old_completed_count(user)
    howmanytasks = thecount[0]
    results = get_old_completed(user)

    for x in results:
        x = list(x)
        result_id, result_user, result_task, result_startdate, result_finishdate = x[0], x[1], x[2], x[3], x[4]

    if thecount[0] == 0:
        await ctx.send(f"Sorry {user}, doesn't have any old completed tasks :(")

    if thecount[0] == 1:
        await ctx.send(f"Hey {result_user}, you have {howmanytasks} old completed task!")
    
        for x in results:
            x = list(x)
            result_id, result_user, result_task, result_startdate, result_finishdate = x[0], x[1], x[2], x[3], x[4]
            #result_all= f"{result_id}, {result_user}, {result_task}, {result_startdate}, {result_finishdate}"
            await ctx.send(f'{result_user} - {result_task} - ID: {result_id} - Finishdate: {result_finishdate}')
    
    if thecount[0] > 1:
        await ctx.send(f"Hey {result_user}, you have {howmanytasks} old completed tasks! PogChamp")
        
        for x in results:
            x = list(x)
            result_id, result_user, result_task, result_startdate, result_finishdate = x[0], x[1], x[2], x[3], x[4]
            #result_all= f"{result_id}, {result_user}, {result_task}, {result_startdate}, {result_finishdate}"
            await ctx.send(f'{result_user} - {result_task} - ID: {result_id} - Finishdate: {result_finishdate}')

#Drop your table, delete literally everything, be careful
@bot.command(name='droptable')
async def test_command(ctx):

    user = ctx.author.name
    ismod = ctx.author.is_mod

    if ismod == True:
        try:
            success = drop_table()
        except Exception as e:
            print(e)
        else:
            if success == 1:
                await ctx.send(f"Table dropped - New table made!")
            else:
                await ctx.send(f"Error dropping table")
    else:
        await ctx.send(f"Sorry {user}, but you don't have permission to use this command :(")

if __name__ == '__main__':
    bot.run()