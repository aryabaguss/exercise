import pdb
def fungsi_pembagian_list(list_input):
    pdb.set_trace()

    list_hasil = []
    
    for angka in list_input:
        
            pembagi = angka
            hasil = (5 / pembagi)
            list_hasil.append(hasil)
        
    return list_hasil

inputs = [1,2,3,4,5,6,7]
print(fungsi_pembagian_list(inputs))