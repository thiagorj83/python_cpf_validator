from cpf_validation import ValidadeCpfNumber


def main():

    cpf01=ValidadeCpfNumber()
    cpf01.validate('113.472.377-63')

    cpf02=ValidadeCpfNumber()
    cpf02.validate('111.111.111-11')

    cpf03=ValidadeCpfNumber()
    cpf03.validate('11347237763')


if __name__=="__main__":

    main()