
import string as s
from secrets import SystemRandom as Sr

letras = s.ascii_letters
digitos = s.digits
caracteres = '!@#$*-'


while True:
    try:
        tamanho_senha = input('Digite o tamanho da sua senha (superior a 8): ')
        tamanho_senha_int = int(tamanho_senha)

        if tamanho_senha_int < 8:
            print(
                'Por questões de Segurança a senha deve ter tamanho superior'
                ' ou igual a 8 ')
            print()
            continue

        concatenados = letras + digitos + caracteres

    except (ValueError) as error:
        print('Digite apenas valores numéricos ')
        print('MSG: ', error.__class__.__name__)  # nome da classe: IndexError
        print()
        continue

    while True:
        nova_senha = "".join(Sr().choices(concatenados, k=tamanho_senha_int))
        lista_caracteres = list(caracteres)
        lista_nova_senha = list(nova_senha)
        nova_lista = [x for x in lista_caracteres if x in lista_nova_senha]

        if tamanho_senha_int <= 10:    # Se o tamanho da senha for menor ou
            # igual a 10, a nova senha deverá ter no mínimo 2 caracteres
            # especiais

            if not len(nova_lista) >= 2:
                continue
            else:
                print(nova_senha)
                break
        elif tamanho_senha_int > 10:    # Se o tamanho da senha for maior que
            # 10, a nova senha deverá ter no mínimo 4 caracteres especiais
            if not len(nova_lista) >= 4:
                continue
            else:
                print(nova_senha)
                break
        else:
            break
    continue

## teste