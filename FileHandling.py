#File Handling is the process of reading and writing data to files. In Python, you can use the built-in `open()` function to work with files. 

# create , read, write, update , append to files using different modes.

#mainly use txt , csv ,json and excel

#Syntax of file handling

#var = open("Filename.ext", "mode")  # mode can be 'x','r', 'w', 'a', 'r+', etc. File is opened in the specified mode.

#var.close()  # File closing after the operation 

#Create x
#file = open("NewFile.csv","x")  # Create a new file in exclusive creation mode. If the file already exists, it will raise a FileExistsError.

#if already exists then it will raise an error.
# try :
#     file = open("NewFile.csv","x")  
# except FileExistsError:
#     print("File already exists. Please choose a different name or delete the existing file.")   
#     print("try to create a new file with a different name or delete the existing file.") 
# else:
#     print("File created successfully.")    

#   Write w 
# Write_file = open("NewFile.txt","w")  # Open the file in write mode. If the file already exists, it will overwrite the content.
# Write_file.write("Hi i am mohan with pain full character")
# Write_file.close()  # Close the file after writing.


# #Append a
# Append_File = open("NewFile.txt","a")  # Open the file in append mode to add content to the end of the file.
# Append_File.write("\n I am the sensitive person")
# Append_File.close()  # Close the file after appending.


# #Read r
# #Read() , Readline() , Readlines() are the methods to read the content of the file.
# Read_File = open("NewFile.txt","r")  # Open the file in read mode.
# See_Content = Read_File.read()  # Read and print the content of the file.
# Read_File.close()  # Close the file after reading.
# print("Content of the file:", See_Content)
# print(type(See_Content))  # Check the type of the content read from the file. It will be a string.

#update r+
# update_file = open("NewFile.txt","r+")  # Open the file in read and write mode.
# update_file.write("\n I am the sensitive person")  # Write new content to the file
# update_file.close()  # Close the file after updating.


#Deleting a file : 
import os
Remove_File = os.remove("NewFile.csv")
print(Remove_File)  # Remove the specified file from the filesystem. It will delete the file permanently.
print("File deleted successfully.")  # Print a message indicating that the file has been deleted.
#check if the file exists after deletion. It will return False if the file has been deleted successfully.
os.path.exists("NewFile.csv")  # Check if the file exists after deletion. It will return False if the file has been deleted successfully.
print("File will not have ")