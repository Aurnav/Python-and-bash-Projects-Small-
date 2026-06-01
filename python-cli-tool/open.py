with open("/proc/meminfo","r") as f:
    content = f.readlines()
    print(content,"\n")
   
