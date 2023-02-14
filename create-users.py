#!/usr/bin/python3
import os
import re
import sys

def main():
    for line in sys.stdin:
        match = re.match('#',line) #Using the re.match function to see if the line begins with the character "#"

        fields = line.strip().split(':') #strip any whitespace and split into an array 

        if match or len(fields) != 5: #Check to see whether the "match" variable is true or if the length of the "fields" list is less than 5.
            continue ## Continue to the next iteration if one of the above conditions is true.

        username = fields[0]
        password = fields[1]

        gecos = "%s %s,,," % (fields[3],fields[2])

        groups = fields[4].split(',') # Use a comma to separate the fifth element of the "fields" list and save the result list in the "groups" variable.The purpose for this is to extract individual group information from the fifth field in the list, which may have several values separated by a comma.

        print("==> Creating account for %s..." % (username))
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

        os.system(cmd) #Calling the os.system function and passing the cmd variable as an argument and print it out.
        print("==> Setting the password for %s..." % (username))
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)
        os.system(cmd)
        for group in groups: ## Iterate through the list of "groups" elements.Individually process each group in the "groups" list.
            if group != '-':
                print ("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                os.system(cmd)

if __name__ == '__main__':
    main()
