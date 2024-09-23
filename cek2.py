import pdb

def multiply(variabel_pertama, variabel_kedua):
    answer = variabel_pertama * variabel_kedua
    return answer

input_pertama = int(input("Enter first number : "))
input_kedua = int(input("Enter second number : "))
result = multiply(input_pertama, input_kedua)
print(result)

