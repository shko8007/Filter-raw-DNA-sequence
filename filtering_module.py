#This code is moduel, removing off-target amplicon generated after PCR.
#Load raw data analyzed
#Align and process each sequence with different ID
#Count totla number of bases of each sequence and remove longer or shorter DNA than target length
#Align and process each sequence filtered
#Save the modified data in a new file as txt format
 
def filter(input_file,output_file):
    
    raw_data=open(input_file,"r") 
    a=raw_data.read() # load and read raw sequencing file
    b=a.replace('\n','') # merge all separated lines
    c=b.split('>') # split into individual sequence based on sequence ID
    d='\n'.join(c) # convet list to string
    e=d.replace('\n','',1).replace('m','>m') # remove space and add additional characters
    f=e.split() #conver string to list

    # Count number of base in each seq x_mod='' # initialize x_mod
    x_mod=''
    for x in f:
        value_A=x.count("A")
        value_G=x.count("G")
        value_C=x.count("C")
        value_T=x.count("T")
        total_value=value_A+value_G+value_C+value_T # Sum of bases
        
        if total_value > 2500 and total_value < 3000 : # Size criteria to filter off-target
            x_mod = x_mod + x
        else:
            continue
        
   

    # post-processing of filtered data
    h=x_mod.split('>')
    i='\n'.join(h)
    j=i.replace('\n','',1).replace('m','>m').replace('s','s\n')
    print(j)

    # store filtered data
    mod_data=open(output_file, 'w')
    mod_data.write(j)
    mod_data.close()
