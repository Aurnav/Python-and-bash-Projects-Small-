#!/bin/bash
echo "*************************************** Welcome to System.log finder ***************************************"
echo "Which Directory would you like  to find it in "
read log
cd "$log"
if [ -f "system.log" ]; then 
   echo "File exists"
   mkdir archive
   timestamp=$(date +"%y-%m-%d_%H-%M")
   echo $timestamp
   tar -czf "archive/log_backup_$timestamp.tar.gz" "system.log"
   > system.log
   echo -e "\033[1;32m The process is complete pls check your archive folder \033[0m"
else 
     echo -e "\033[1;31m Sorry cant find the file \033[0m"
     exit 1
fi
   
   
