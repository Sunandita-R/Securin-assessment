# PART A
DieA =[1,2,3,4,5,6]
DieB =[1,2,3,4,5,6]
# Question 1
""" Total number of combinations possible when rolling two dice can be represented as
No of possible outcomes of Die A * No of possible outcomes of Die B


No of possible outcomes for each Die is 6
so total combinations =  6*6 = 36

"""
pos_out=len(DieA)*len(DieB)
print("\nTotal number of combinations : ",pos_out)

#Question 2
"""
For each outcome of Die A there can be 6 different outcomes of Die B  leading to 36 combinations
of the form (1,1),(1,2).....(1,6)....(6,1)..(6,6)

"""
print("""\nThe combinations possible: \nFirst value in each ordered pair represents outcome of Die A
Second value represents outcome of Die B""")
for val1 in DieA:
    for val2 in DieB:
        print("(",val1,",",val2,")",end=" ")
    print()
    
#Question 3
"""Sum can range between 2 and 12. Now each possible sum is a key in the dictionary and
 the number of occurences is the value of the key."""
sum_dict={}
for val1 in DieA:
    for val2 in DieB:
        sum_=val1+val2
        if(sum_ not in sum_dict):
            sum_dict[sum_]=1
        else:
            sum_dict[sum_]+=1
print("\nProbality of sum \n")
for sum_ in sum_dict:
    print("P(Sum = ",sum_,") = ",sum_dict[sum_],"/",pos_out)


#Part B
def equaldict(l1,l2,sum_dict):
    d={}
    for val1 in l1:
        for val2 in l2:
            sum_=val1+val2
            if(sum_ not in d):
                d[sum_]=1
            else:
                d[sum_]+=1
    if(sum_dict==d):
        print(l1,l2)
l1=[0,1,0,0,0,0]
l2=[2,3,0,0,0,0]
def undoom_dice(l1,l2):
    for v3 in range(1,5):
                l1[2]=v3
                for v4 in range(1,5):
                    l1[3]=v4
                    for v5 in range(1,5):
                        l1[4]=v5
                        for v6 in range(1,5):
                            l1[5]=v6
                            for v9 in range(1,13):
                                        l2[2]=v9
                                        for v10 in range(1,13):
                                            l2[3]=v10
                                            for v11 in range(1,13):
                                                l2[4]=v11
                                                for v12 in range(1,13):
                                                    l2[5]=v12
                                                    equaldict(l1,l2,sum_dict)
                                                    
undoom_dice(l1,l2)
    
    
