def main():
    phone="617-495-1000"
    print(phone)
    #what this does is simply print phone string
    #but what if i want specif things such as first four of last four or somewhat
    #there i can use indexing with the help of a list 
    print(phone[0:3])
    #this prints the first 4 because index starts from 0 even if i leave the 0 blank python starts from the beginning
    #what if i wanna print from suppose last 4
    print(phone[8:])
    #this prints from index 8 to the last number
    #or i could do it another way such as.
    print(phone[-4:])
    #this simply print the last four 

main()