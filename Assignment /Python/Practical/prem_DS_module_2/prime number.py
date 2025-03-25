print("Enter the number!!")
n = int(input("Enter the number: "))

prime = True  # Assume the number is prime
for i in range(2, n):
    if n % i == 0:
        prime = False
        break  # Exit loop as soon as a divisor is found

if prime:
    print("The number is prime!!")
else:
    print("Number is not prime!!")