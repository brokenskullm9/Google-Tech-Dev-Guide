#sequence and subsequece, input
S = "abppplee"
D = ["able", "ale", "apple", "bale", "kangaroo"]

#initializing some of the variables
d = []
ind = 0
count = 0
index = 0

#main class
class main:
    global d, ind, count, index     #refering to the global variables inside the main() class
    for i in D:                     #for loop for fetching one string at a time from list D
        for j in range(len(i)):     #for loop for fetching one character at a time from fetched string from the list D
            while ind<len(S):       #while loop for fetching one character from the string S
                if S[ind] == i[j]:  #checking the condition from the string~S(sequence) and D(subsequence), if both are equal then count will be incremented
                    count+=1        #incrementing count if condition is true
                    break           #breaking while loop when condition is satisfied
                ind+=1              #incrementing ind 
        d.append(count)             #appending  count to list d
        count = 0                   #reseting count to 0
        ind = 0                     #reseting ind to 0
            
    for e in d:                     #for loop to calculate index of maximum number in the list d
        if max(d) == e:             #if statement for checking the condition for max value of d to each number from the list d for each iteration
            break                   #breaking while loop when if  condition is true
        index+=1                    #increamenting index

#printing the value which contain max subsequence
if __name__ == "__main__":
    main()
    print(D[index])
