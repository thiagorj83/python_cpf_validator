from cpf_validation import ValidateCpfNumber


def main():

    cpf01=ValidateCpfNumber()
    cpf01.validate('113.472.377-63')

    cpf02=ValidateCpfNumber()
    cpf02.validate('111.111.111-11')

    cpf03=ValidateCpfNumber()
    cpf03.validate('11347237763')


if __name__=="__main__":

    main()