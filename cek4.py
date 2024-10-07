import pdb

def modif_list(list_input):
    
    list_hasil = []
    
    for i in range(5):
        a = (list_input[i] + 2 )/5
        list_hasil.append(a)
    return list_hasil

list_1 = [1,2,3,4,5]
b = modif_list(list_1)

print(b)