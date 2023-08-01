import sys # for accessing command line arguments

if __name__ == '__main__':
    # get number of arguments and arguments as a list
    num_args = len(sys.argv) - 1
    arg_list = sys.argv[1:]

    # print number of arguments and argument list
    print("Number of argument"+("s" if num_args>1 else "")+": "+str(num_args)+(":" if num_args>0 else ".")+"\n")
    for i,arg in enumerate(arg_list):
        print(str(i+1)+": "+arg)