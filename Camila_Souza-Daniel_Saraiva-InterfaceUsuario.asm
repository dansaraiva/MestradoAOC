.data
x:          .word 0                 # espa�o para o primeiro n�mero
y:          .word 0                 # espa�o para o segundo n�mero

prompt1:    .ascii "Digite o primeiro n�mero: "
            .byte 0
prompt2:    .ascii "Digite o segundo n�mero: "
            .byte 0
result_msg: .ascii "O MDC �: "
            .byte 0

.text
.globl _start

_start:
    # Carrega o endere�o de x em t0
    la t0, x

    # Imprime o prompt para o primeiro n�mero
    la a0, prompt1      # carrega o endere�o do prompt1 em a0
    li a7, 4            # syscall para imprimir string
    ecall

    # L� o primeiro n�mero
    li a7, 5            # syscall para ler um inteiro
    ecall
    sw a0, 0(t0)        # armazena o n�mero lido em x

    # Carrega o endere�o de y em t1
    la t1, y

    # Imprime o prompt para o segundo n�mero
    la a0, prompt2      # carrega o endere�o do prompt2 em a0
    li a7, 4            # syscall para imprimir string
    ecall

    # L� o segundo n�mero
    li a7, 5            # syscall para ler um inteiro
    ecall
    sw a0, 0(t1)        # armazena o n�mero lido em y

    # Carrega x e y em t0 e t1
    lw t0, 0(t0)        # carrega o valor de x em t0
    lw t1, 0(t1)        # carrega o valor de y em t1

proc_mdc:
    beq t0, t1, end_proc   # se t0 == t1, fim do procedimento

    blt t0, t1, less_than  # se t0 < t1, v� para less_than
    sub t0, t0, t1         # caso contr�rio, t0 = t0 - t1
    j proc_mdc             # volta para o in�cio do loop

less_than:
    sub t1, t1, t0         # t1 = t1 - t0
    j proc_mdc             # volta para o in�cio do loop

end_proc:
   # Armazena o resultado em x
    la t2, x               # carrega o endere�o de x em t2
    sw t0, 0(t2)           # armazena o valor de t0 no endere�o de mem�ria apontado por t2

    # Imprime a mensagem do resultado
    la a0, result_msg      # carrega o endere�o da mensagem em a0
    li a7, 4               # syscall para imprimir string
    ecall

    # Carrega o resultado em a0 e imprime
    lw a0, 0(t2)           # carrega o resultado de x em a0
    li a7, 1               # syscall para imprimir inteiro
    ecall

    # Termina o programa
    li a7, 10              # syscall para terminar o programa
    ecall
