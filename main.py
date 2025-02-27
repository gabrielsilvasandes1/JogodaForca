palavra = ['P', 'Y', 'T', 'H', 'O', 'N']
letras_adivinhadas = []
tentativas_restantes = 7
while tentativas_restantes > 0:
    user = input('Informe uma Letra ou Palavra: ').upper().strip()
    if user == "".join(palavra):
        print(f'Parabéns! Você acertou a palavra {user}.')
        break
    if len(user) == 1:
        if user in palavra and user not in letras_adivinhadas:
            letras_adivinhadas.append(user)
            print(f'A letra {user} tem na palavra!', end=' ')
            print(f'Até agora você acertou {len(letras_adivinhadas)} letras.')
        elif user in letras_adivinhadas:
            print(f'Você já informou a letra {user}. Tente outra!')
        else:
            tentativas_restantes -= 1
            print(f'Não tem a letra {user} na palavra. Você tem {tentativas_restantes} tentativas restantes.')
    if set(letras_adivinhadas) == set(palavra):
        print(f'Parabéns! Você descobriu a palavra {''.join(palavra)}.')
        break
if tentativas_restantes == 0:
    print(f'Fim de jogo! Você perdeu. A palavra era {''.join(palavra)}.')
