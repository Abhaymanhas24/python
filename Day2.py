# Write a program with a function that the function will multiply the number N with three. 
def multipleofthree(N):
    return N*3
    
N=int(input())
print(multipleofthree(N))

# Write a program with a function that the function will check if the number N is divisible by 7. 
def divisible_by_seven(N):
    if N % 7 == 0:
        print(f"{N} is divisible by 7")
    else:
        print(f"{N} is not divisible by 7")

N=int(input())
print(divisible_by_seven(N))
