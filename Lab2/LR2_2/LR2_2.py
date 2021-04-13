def file_Reader():

    file_open = input("\nPlease enter the file name: ")
    file = open(file_open, 'r')
    linecount = 0

    for line in file:
        linecount = linecount + 1

    print("The number of lines in this txt. file is", linecount)

    with open(file_open, 'r') as fileopen:
        text_list = [line.strip() for line in fileopen]
        print(text_list)

    while True:
        linenum = 0

        num = int(input("Please enter a line number or press 0 to quit: "))
        if num >=1 and num <= linecount:
            file = open(file_open, 'r')
            print(text_list[num-1])
        elif num == 0:
            print("Thanks for using the program")
            break
        else :
            print ("Out of Range, Exiting")


def main():
    print("Welcome!")
    file_Reader()


main()
