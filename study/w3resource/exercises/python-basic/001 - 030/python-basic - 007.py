# 007 - Write a Python program to accept a filename from the user and print the extension of that.

fileName = input('Filename: ') 
print(f'File extension: {fileName[fileName.find(".") + 1:]}')