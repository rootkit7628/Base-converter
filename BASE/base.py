def turn_in_decimal(nb_init,base_init) :
    dizaine=["A","B","C","D","E","F"]
    nb_init=list(nb_init)
    nb_decimal=0
    for i in  range(len(nb_init)) :
        if nb_init[i] in dizaine : nb_init[i]=str((dizaine.index(j))+10)
        nb_decimal+=( int(nb_init[i]) * (base_init**(len(nb_init)-i-1)))
    return nb_decimal

def turn_decimal_in(nb_decimal,base_final) :
    dizaine = ["A","B","C","D","E","F"]
    list_finale = []
    while base_final <= nb_decimal :
        rest = nb_decimal % base_final
        nb_decimal = int(nb_decimal/base_final)
        if rest > 9 : rest = dizaine[rest - 10]
        list_finale.append(str(rest))
    list_finale.append(str(nb_decimal))
    list_finale.reverse()
    return ''.join(list_finale)

def turn_in_base(nb_init,base_init,base_final) :
    a = turn_in_decimal(nb_init,base_init)
    return turn_decimal_in(a,base_final)
