import sys
import subprocess 
if len(sys.argv)== 1 :
   print("*************************************** WELCOME TO THE LINUX COMMAND SET ***************************************")
   while True:
     print(" Choose what you want to do \n 1 for Ram usage \n ")
     print("Choose 2 for Disk check \n")
     print("Choose 3 for checking what is inside the directory  \n")
     print("Choose 4 for checking who is running the system  \n ")
     print("Choose 5 for checking for how long the system is running \n ")
     user_input = int(input("Here ==>  "))
     if user_input == 1:
         subprocess.run(['free', '-h'], text=True)
     elif user_input == 2:
         direct = input("Choose Which Directory and leave blank for default ")
         if direct == "":
            subprocess.run(['df', '-h'], text=True)
         else:
            subprocess.run(['df', '-h', direct], text=True)
     elif user_input == 3:
          check = input("which directory you want to check and leave blank for default")
          if check == "":
             subprocess.run(['ls'], text=True)
          else:
             subprocess.run(['ls' , check],text=True)
     elif user_input == 4:
          subprocess.run(['whoami'],text=True)
     
     elif user_input == 5:
          subprocess.run(['uptime'],text=True)
     else:
          print("Invalid no .. try again")
     
     print("Do you want to try again ?")
     retry = input("yes or no ")
     if retry.lower() == "yes":
        continue
     else:
        break
else:
     
     if sys.argv[1] == "ram":
         subprocess.run(['free', '-h'], text=True)
     elif sys.argv[1] == "disk" and len(sys.argv) == 2: 
         subprocess.run(['df', '-h'], text=True)
     elif sys.argv[1] == "disk" and len(sys.argv) == 3: 
          subprocess.run(["df" , "-h" ,sys.argv[2]]) 
         
     elif sys.argv[1] =="ls" and len(sys.argv) == 2:
          subprocess.run(['ls'], text=True)
     elif sys.argv[1] == "ls" and len(sys.argv) == 3 :
          subprocess.run(["ls" , sys.argv[2]]) 
              
     elif sys.argv[1] =="user":
          subprocess.run(['whoami'],text=True)

     elif sys.argv[1] == "uptime":
          subprocess.run(['uptime'],text=True)
    
     elif sys.argv[1] == "help":
          print("Command [directory] or it can be left blank for default \n ")
          print("df -h for disk \n ls for ls \n whoami for user \n uptime for uptime")
     else:
          print("command not found")
