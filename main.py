# 100 Days of Code: The Complete Python Pro Bootcamp by Dr. Angela Yu
# Day 24 - Intermediate - Files, Directories and Paths

# file = open("my_file.txt") # then file.close() will need to be used to free up resources, only use as many tabs as you need

## Open a file and read
# with open("my_file.txt") as file: # will close the file ones done
#     content = file.read()
#     print(content)

# Write to a file, default mode of open is read-only, w=write -> re-write everything, a=append -> adds more info
with open("my_file.txt", mode="a") as file: # will close the file ones done
    file.write("\nMore text 2.")

# With mode w=write if file doesn't exit, new file will be created
with open("new_file.txt", mode="w") as file: # will close the file ones done
    file.write("New text.")