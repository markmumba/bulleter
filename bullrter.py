# Take a file and add * in front of every line and capitalize the first word. Write updated items in a another file. Also copy the new file to the clipboard

# Outline all the behaviors your application will have.
# Create unit tests for all the behaviours.
# Create doc-strings for the modules, functions and methods



f=open('safe.txt' ,'r')
n=open('new.txt','w')
for x in f:
    output="*"+x.title()
    n.write(output)
    print(output)
    
    
    
f.close()
n.close()


        
