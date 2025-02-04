num = 6
base = 3 # baseshould not be 0

def num_string(integer, bs):
    convert_String = "0123456789ABCDEF"
    if integer < bs:
        return convert_String[integer]
    else:
        return num_string(integer//bs, bs) + convert_String[integer%bs]
    

string = num_string(num, base)
print(string)