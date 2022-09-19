def marks_calculate():
    while True:
        sh = float(input("Enter the number of hours you study"))
        rank = input("How good are you at studying (low/below avg/avg/above avg/high)")
        if (rank == "low"):
            marks = sh*10 - 10
        elif (rank == "below avg"):
            marks = sh*10 - 5
        elif (rank == "avg"):
            marks = sh*10
        elif (rank == "above avg"):
            if (sh <= 9.5):
                 marks = sh*10 + 5
            else :
                 marks = 100
        elif (rank == "high"):
            if (sh <= 9):
                 marks = sh*10 + 10
            else :
                 marks = 100
        else :
            print("the key enetered is not valid, please try again")
        print("Your estimated marks is :",marks)
        ans=input("Do you want to try again (yes/no)")
        if (ans=="yes"):
            continue
        else:
            print("Thank You")
            break

marks_calculate()
    
