def main():
    ''' Programa para teste da sua funcao potencia '''
    base = float(input("Digite a base real: "))
    exp  = int(input("Digite o expoente inteiro: "))
    pot  = potencia(base, exp)
    print("potencia(%f, %d) = %f"%(base, exp, pot))

def potencia(base, expoente):
    ''' (float, int) -> float
    retorna a base elevado ao expoente inteiro '''
    pot= base ** expoente
    # modifique o resto com o codigo da sua funcao
    print("O resultado é: ")

    return pot

main()



