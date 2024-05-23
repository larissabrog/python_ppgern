# Desafio 3:	
# Problem Given: A string s of length at most 200 letters and four integers a, b, c and d.
# Return: The slice of this string from indices a through b and c through d (with space in between), inclusively. In other words, we should include elements s[b] and s[d] in our slice.

# Criando uma função para a string (s) e os índices do slicing (a, b, c e d)
def f_string (s, a, b, c, d):

# Fazendo o slicing pelos índices
    slice1 = s[a:b+1]
    slice2 = s[c:d+1]

# Utilizando f-string para juntar as slices no resultado
    final_string = f’{slice1} {slice2}’
    return final_string