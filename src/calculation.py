
# Primeira funcão em Python
def salaryCalc ():

    _salary = int(input(f'Digite o valor do seu salário: R$'))

    if _salary >= 5000:
        _discount = _salary * 0.27
        _salary_liquid = _salary - _discount
        print(f'Seu desconto é de 27% no valor do salário. O valor líquido que você receberá é: R$ {_salary_liquid}')

    elif _salary >= 3000:
        _discount = _salary * 0.23
        _salary_liquid = _salary - _discount
        print(f'Seu desconto é de 23% no valor do salário. O valor líquido que você receberá é: R$ {_salary_liquid}')

    else:
        _discount = _salary * 0.19
        _salary_liquid = _salary - _discount
        print(f'Seu desconto é de 19% no valor do salário. O valor líquido que você receberá é: R$ {_salary_liquid}')


print (salaryCalc())