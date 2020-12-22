#get the number and convert to int
tree_height=int(input("enter the height of the tree : "))
 
# get the starting spaces for the top of the tree
spaces = tree_height - 1

#there is one hash to start that will be incremented
hashes =1

# Save stup spaces till later
stump_spaces = tree_height - 1

# make sure the right number of rows are printed
while tree_height != 0:

    for i in range(spaces):
        print(' ',end="")
    
#print the hashes
    for i in range(hashes):
        print('#', end="")
#Newline after each row is printed 
    print()

    spaces -= 1

    hashes += 2

    tree_height -= 1





for i in range(stump_spaces):
    print(' ',end="")


print("#")
