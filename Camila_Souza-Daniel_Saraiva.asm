    .data
x:  .word 0        # espa�o para o primeiro n�mero
y:  .word 0        # espa�o para o segundo n�mero

    .text
    .globl _start

_start:
    # Inicializa��o dos valores (por simplicidade, valores fixos s�o usados aqui)
    li t0, 48      # carregando o valor 48 em t0
    la t1, x       # carregando o endere�o de x em t1
    sw t0, 0(t1)   # armazenando o valor 48 na mem�ria em x

    li t0, 18      # carregando o valor 18 em t0
    la t1, y       # carregando o endere�o de y em t1
    sw t0, 0(t1)   # armazenando o valor 18 na mem�ria em y

    # Carregar valores de x e y
    la t1, x       # carregando o endere�o de x em t1
    lw t0, 0(t1)   # carregando o valor de x em t0

    la t1, y       # carregando o endere�o de y em t1
    lw t1, 0(t1)   # carregando o valor de y em t1

proc_mdc:
    beq t0, t1, end_proc # se x == y, fim do procedimento

    blt t0, t1, less_than # se x < y, v� para less_than
    sub t0, t0, t1       # caso contr�rio, x = x - y
    j proc_mdc           # volta para o in�cio do loop

less_than:
    sub t1, t1, t0       # y = y - x
    j proc_mdc           # volta para o in�cio do loop

end_proc:
    # Armazenar o resultado de volta em x (ou y, j� que s�o iguais agora)
    la t2, x
    sw t0, 0(t2)

    # Sa�da do programa (usando chamada de sistema para sair)
    li a7, 10           # c�digo de sa�da do ecall
    ecall               # chamada do sistema para encerrar o programa
