# this is a file manipulaton script

filename = input("\nFilename.extension: ")

with open (filename,"x"):
    print()
    print(f"{filename} Created")
