    .data
x:  .word 0        # espaço para o primeiro número
y:  .word 0        # espaço para o segundo número

    .text
    .globl _start

_start:
    # Inicialização dos valores (por simplicidade, valores fixos são usados aqui)
    li t0, 48      # carregando o valor 48 em t0
    la t1, x       # carregando o endereço de x em t1
    sw t0, 0(t1)   # armazenando o valor 48 na memória em x

    li t0, 18      # carregando o valor 18 em t0
    la t1, y       # carregando o endereço de y em t1
    sw t0, 0(t1)   # armazenando o valor 18 na memória em y

    # Carregar valores de x e y
    la t1, x       # carregando o endereço de x em t1
    lw t0, 0(t1)   # carregando o valor de x em t0

    la t1, y       # carregando o endereço de y em t1
    lw t1, 0(t1)   # carregando o valor de y em t1

proc_mdc:
    beq t0, t1, end_proc # se x == y, fim do procedimento

    blt t0, t1, less_than # se x < y, vá para less_than
    sub t0, t0, t1       # caso contrário, x = x - y
    j proc_mdc           # volta para o início do loop

less_than:
    sub t1, t1, t0       # y = y - x
    j proc_mdc           # volta para o início do loop

end_proc:
    # Armazenar o resultado de volta em x (ou y, já que são iguais agora)
    la t2, x
    sw t0, 0(t2)

    # Saída do programa (usando chamada de sistema para sair)
    li a7, 10           # código de saída do ecall
    ecall               # chamada do sistema para encerrar o programa
