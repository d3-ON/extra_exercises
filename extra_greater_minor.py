def run():
    in_list = []
    cp_list = []
    out_list = []
    stop = False

    
    while stop == False:
        number = int(input('Enter a number: '))
        
        if number == 0:
            stop = True
        else:
            in_list.append(number)
            cp_list.append(number)
            
    if len(in_list) < 5 or len(in_list) > 10:
        print('You should enter more of 10 number and minor of 20')
        in_list = []
        run()
        quit()
        
    while len(out_list) < len(in_list):
        greater = 0
        for i in cp_list:
            if i >= greater:
                greater = i
                indx = cp_list.index(i)
                
        out_list.append(greater)
        cp_list.pop(indx)

    print(out_list) 
                       
if __name__ == '__main__':
    run()
    
    