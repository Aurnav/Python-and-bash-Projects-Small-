#!/bin/bash
Sjunk=("cache" ".temp" ".tmp" "log" ".bak" ".old" ".part" ".cache")
Wjunk=("history" "thumbnail" "thumbs" "crash" "dump" "lock" "pid")
Impo=(".pdf" ".docx" ".xlsx" ".odt" ".txt" ".jpg" ".jpeg" ".png" ".gif" ".mp4" ".zip" ".tar")
echo "Enter Which Directory you would Like to search in: "
read Directory
Dir=$(find "$Directory" -type d \( -name "temp" -o -name "Temp" -o -name "Cache" -o -name "cache" \))
for open in $Dir
do 
   echo "Checking directory: $open"
   point=0

  
   for file in "$open"/*
   do
     
      filename=$(basename "$file")
      
     
      [ -e "$file" ] || continue

     
      for trash in "${Sjunk[@]}"
      do
         if [[ "$filename" == *"$trash" ]]; then 
             ((point+=3))
             break 
         fi
      done

     
      for wtrash in "${Wjunk[@]}"
      do
         if [[ "$filename" == *"$wtrash" ]]; then 
             ((point+=1))
             break
         fi
      done

     
      for important in "${Impo[@]}"
      do
         
         if [[ "$filename" == *"$important" ]]; then
             ((point-=1))
             break
         fi
         if [ point >= 15 ]; then 
            echo "Your folder score": $point
            echo "Do you want to remove it Y/n"
            read yes_no   
   done
    if [ "$point" -ge 15 ]; then 
      echo "Your folder score: $point"
      echo "Do you want to remove it Y/n"
      read yes_no
      
      if [ "$yes_no" == "y" ] || [ "$yes_no" == "Y" ]; then
          rm -rf "$open"
          echo "Deleted the directory: $open"
      elif [ "$yes_no" == "n" ] || [ "$yes_no" == "N" ]; then
          echo "Skipping deletion."
      else
          echo "Invalid choice. Skipping folder."
      fi
   fi
done      
      
