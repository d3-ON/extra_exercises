def count_ants(amount, months):
    stop = 0
    
    while stop < months:
        if amount < 28000:
            amount = (amount + ((amount * 40) / 100)) - 7000
        elif amount > 28000:
            amount = (amount - ((amount * 31) / 100)) - 7000
        
        stop += 1
    
    return amount

def run():
    initial_amount = int(input('Enter the ants amount: '))
    months = int(input('Enter the months amount: '))    
    
    total = count_ants(initial_amount, months)

    print(f'The total amount of ants in {months} be {round(total)}')

if __name__ == '__main__':
    run()