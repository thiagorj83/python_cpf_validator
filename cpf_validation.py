import re

class ValidadeCpfNumber:

    def validate(self,cpf: str) -> bool:
        
        # Salva cada dígito na variável numbers
        numbers = [int(digit) for digit in cpf if digit.isdigit()]
    
        # Efetua o cálculo da soma dos produtos de cada dígito
        sum_of_products = sum(a*b for a, b in zip(numbers[0:9], range(10, 1, -1)))
        expected_digit1 = (sum_of_products * 10 % 11) % 10
        
        sum_of_products = sum(a*b for a, b in zip(numbers[0:10], range(11, 1, -1)))
        expected_digit2 = (sum_of_products * 10 % 11) % 10
        
        if (re.match("^[0-9]{11}$", cpf) or re.match(r'\d{3}.\d{3}.\d{3}-\d{2}$', cpf)) and not len(set(numbers)) == 1 and numbers[9] == expected_digit1 and numbers[10] == expected_digit2:
            return print('O C.P.F. '+ str(cpf) + ' é válido!')
        else:
            return print('O C.P.F. '+ str(cpf) + ' não é válido!')
        
        