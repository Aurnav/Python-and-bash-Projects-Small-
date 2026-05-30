#!/bin/bash

echo "What is your name and age?" 
read name 
read age      

Days=$(( age * 365 ))

# Fixed the forward slash to a backslash, and added the $Days variable
echo -e "\033[0;32mHello $name, you have been alive for roughly $Days days! :>\033[0m"
