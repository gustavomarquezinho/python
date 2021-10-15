# 029 - Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2.

colorInfo_1 = {
    "White", "Black", "Red", 
}

colorInfo_2 = {
    "Red", "Green", 
}

print(colorInfo_1 - colorInfo_2)