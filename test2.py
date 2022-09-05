fmt=3
def tablas(n:int, t:int):
    for i in range(t):
        multi(n, i+1)
        print(f"{16:c}")

def multi(number:int, table:int):
    for i in range(number):
        print(f"{table:^{fmt}}{'x':^{fmt}}{i+1:^{fmt}}{'=':^{fmt}}{table*(i+1):^{fmt}}")
    
if __name__=="__main__":

    table=5
    n_digits=10
    tablas(4,4)

#stram lit