# inet_4031_adduser_script



This Python script simplifies the process of adding several users and groups to a Linux system. A list of users that need to be added to each system will be read into this script from another file. This procedure may be automated with the help of the given code rather than having to manually create each of these users, which can take a lot of time.

You may execute the "create-users.py" script in one of two ways:

copy and paste the following commands into the terminal/cmd:

cat create-users.input | sudo./create-users.py
or 
cat create-users.input | sudo./create-users.py

Remember to use the "sudo" Elevated Access is necessary to make changes to the group and passwd files.


