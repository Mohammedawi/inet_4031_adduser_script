#!/usr/bin/python3
import os  #Importing os module for operating system functionalities
import re  #Importing the re modue for regular expression operations
import sys #Importing the sys module for system specific parameters

def main(): #define the main func
    for line in sys.stdin: #read input lines from the standard input
        match = re.match('^#',line) #Using the re.match function to see if the line begins with the character "#"

        fields = line.strip().split(':') #strip any whitespace and split into an array 

        if match or len(fields) != 5: #Check to see whether the "match" variable is true or if the length of the "fields" list is less than 5.
            continue ## Continue to the next iteration if one of the above conditions is true.

        username = fields[0] #extract the username from a list of fields and assign it to a variable 
        password = fields[1] ## Extract the password from a list of fields and assign it to a variable

        gecos = "%s %s,,," % (fields[3],fields[2])## Combine the given name and surname from a list of fields to form the GECOS field and assign it to a variable

        groups = fields[4].split(',') #use a comma to separate the fifth element of the "fields" list and save the result list in the "groups" variable.The purpose for this is to extract individual group information from the fifth field in the list, which may have several values separated by a comma.

        print("==> Creating account for %s..." % (username)) #print a message indicating that an account is being created for the specified user
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username) #build a command to create a new user account using the 'adduser' command with the given GECOS field and username

        os.system(cmd) #execute the command using the 'os' module
        print("==> Setting the password for %s..." % (username)) #print a message indicating that the password is being set for the specified user
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username) #build a command to set the user's password using the 'passwd' command with the specified password and username
        os.system(cmd)
        for group in groups: ## Iterate through the list of "groups" elements.Individually process each group in the "groups" list.
            if group != '-':
                print ("==> Assigning %s to the %s group..." % (username,group)) #print a message indicating that the specified user is being assigned to a group
                cmd = "/usr/sbin/adduser %s %s" % (username,group) #build a command to add the user to the specified group using the 'adduser' command
                os.system(cmd) #execute the command using the 'os' module

if __name__ == '__main__': #check if the module is being run as the main program
    main() #calling the main funtction
