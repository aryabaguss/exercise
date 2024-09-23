# melakukan import library pdb
import pdb

# pembuatan fungsi
def fungsi_asal(n):
    
    # menggunakan library pdb untuk melakukan debugging
    pdb.set_trace()
    
    print(n)
    f = n + 5
    return f

fungsi_asal('test')
