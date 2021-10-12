def show_menu():
    print('1. Citire lista')
    print('2. Determinare cea mai lunga subsecventa cu proprietatea 6')
    print('3. Determinare cea mai lunga subsecventa cu proprietatea 18')
    print('4. Iesire')

def read_list():
    lst=[]
    lst_str=input('Dati numerele separate prin spatiu: ')
    lst_str_split= lst_str.split(' ')
    for num_str in lst_str_split:
        lst.append(int(num_str))
    return lst

def get_longest_div_k(lst: list[int], k:int) -> list[int]:
    '''
    Determina cea mai lunga subsecventa in care toate elementele sunt divizibile cu k.
    param list: lista de numere; k: numar intreg
    return: o lista cu subsecventa ceruta
    '''
    n=len(lst)
    result=[]
    for st in range (n):
        for dr in range(st,n):
            all_div_k=True
            for num in lst[st:dr+1]:
                if num%k!=0:
                    all_div_k=False
                    break
            if all_div_k:
                if dr-st+1>len(result):
                    result = lst[st:dr+1]
    return result
def test_get_longest_div_k():
    assert get_longest_div_k([5, 6, 3, 8], 2) == [6, 8]
    assert get_longest_div_k([3, 6, 9, 11], 3) == [3, 6, 9]
    assert get_longest_div_k([5, 11, 24], 6) == [24]
    assert get_longest_div_k([88, 77, 44, 7], 7) == [77, 7]

def desc(n):
    '''
    Determina daca un nr. are cifrele in ordine descrescatoare
    param: n- nr intreg
    return: True/False daca indeplineste sau nu conditia
    '''
    while n>9:
        if n//10%10<n%10:
            return False
        n//=10
    return True

def get_longest_digit_count_desc(lst: list[int])->list[int]:
    '''
    Determina cea mai lunga subsecventa in care numarul de cifre este in ordine descrescatoare.
    param list: lista de numere
    return: o lista cu subsecventa ceruta
    '''
    n=len(lst)
    result=[]
    for st in range(n):
        for dr in range(st,n):
            digit_count_desc=True
            for num in lst[st:dr+1]:
                if desc(num)==0 :
                    digit_count_desc=False
                    break
            if digit_count_desc:
                if dr-st+1>len(result):
                 result= lst[st:dr+1]
    return result

def test_get_longest_digit_count_desc():
    assert get_longest_digit_count_desc([24, 82, 910]) == [82, 910]
    assert get_longest_digit_count_desc([13, 21, 31, 46, 87, 90, 32]) == [87, 90, 32]
    assert get_longest_digit_count_desc([54, 32, 64, 61, 70]) == [54, 32, 64, 61, 70]
    assert get_longest_digit_count_desc([31, 24, 17, 63]) == [31]


def main():
    lst=[]
    while True:
        show_menu()
        opt = input('Optiunea: ')
        if opt == '1':
             lst = read_list()
        elif opt == '2':
             k=int(input('Alegeti un numar k pentru a verifica proprietatea 6: '))
             print('Cea mai lunga subsecventa cu proprietatea ca toate numerele sunt divizibile cu k este: ', get_longest_div_k(lst,k))
        elif opt == '3':
           print('Cea mai lunga subsecventa cu proprietatea ca toate numerele au nr. de cifre in ordine descrescastoare este: ', get_longest_digit_count_desc(lst))
        elif opt == '4':
              break
        else:
              print('Optiune invalida.')


if __name__ == '__main__':
    main()