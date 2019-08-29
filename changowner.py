# importing necessary libraries 
import os, sys, stat 
  
  # Set given file written by the owner. 
  os.chmod("file.txt", stat.S_IWRITE) 
    
    # Set given file executed by the owner. 
    os.chmod("file.txt", stat.S_IXUSR) 
    print("File can be written and executed only by owner.")
