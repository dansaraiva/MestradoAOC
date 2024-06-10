/*
# Disciplina: Arquitetura de Computadores
# Atividade: Avaliação 01 – Programação em Linguagem de Montagem
# Alunos: Camila de Souza e Daniel Saraiva
*/
#include <stdio.h>

// Função para calcular o MDC usando o algoritmo de Euclides
int calcularMDC(int a, int b) {
    // Enquanto b não for zero
    while (b != 0) {
        int temp = b;  // Armazena o valor de b temporariamente
        b = a % b;     // Atualiza b para ser o resto da divisão de a por b
        a = temp;      // Atualiza a para ser o valor antigo de b
    }
    // Quando b se tornar zero, a conterá o MDC
    return a;
}

int main() {
    int num1, num2;

    // Leitura dos dois números
    printf("Digite o primeiro numero: ");
    scanf("%d", &num1);
    printf("Digite o segundo numero: ");
    scanf("%d", &num2);

    // Cálculo do MDC
    int mdc = calcularMDC(num1, num2);

    // Exibição do resultado
    printf("O maximo divisor comum entre %d e %d: %d\n", num1, num2, mdc);
   
     // Inserir uma pausa para permitir que o usuário leia o resultado
    printf("Pressione Enter para sair...");
    getchar(); // Captura o caractere de nova linha deixado pelo scanf
    getchar(); // Espera o usuário pressionar Enter

    return 0;
}