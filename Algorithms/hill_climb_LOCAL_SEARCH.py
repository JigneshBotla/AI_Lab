def calculate(n):
    return n**2-4*n+4


def do_Hillclimb(x1, x2, step_size, max_iterations=1000):
    min_value = calculate(x1)
    minimum = x1
    iterations = 0
    
    while iterations < max_iterations:
        x_new = minimum + step_size
        if x_new <= x2:
            value_new = calculate(x_new)
            if value_new < min_value:
                min_value = value_new
                minimum = x_new
            else:
                break
        else:
            break
        iterations += 1
    return minimum


print("----------HILL CLIMBING-----------")
x1 = float(input("Enter the lower limit: "))
x2 = float(input("Enter the upper limit: "))
step_size = float(input("Enter the step size: "))
print("Hill Climbing:", do_Hillclimb(x1, x2, step_size))
print("Value :",calculate(do_Hillclimb(x1, x2, step_size)))


'''
LOCAL SEARCH:

def find_max(x1, x2, step_size):
    max_val = float("-inf")
    prev_value = float("-inf")
    i=x1
    while i<=x2:
        current_val = -i**3 - 3*(i**2) +2
        print(str(current_val)+"---->"+str(i))

        if prev_value > current_val :
            return prev_value
        
        if current_val > max_val:
            max_val = current_val
        i=round(i+step_size,5)
        prev_value = current_val

    return max_val

x1 = float(input("Enter the lower limit of the range: "))
x2 = float(input("Enter the upper limit of the range: "))
step_size = float(input("Enter the step size: "))
print("The maximum value of the given function is: " + str(find_max(x1, x2, step_size)))'''