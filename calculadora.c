#include <stdio.h>

int main(){
    int num1, num2, res;
    char operacao;
    printf("digite um número: \n");
    scanf("%d", &num1);
    printf("Escolha a operação: + - * / \n");
    scanf("%c", &operacao);
    printf("Escolha outro número: \n");
    scanf("%d", &num2);
    switch (operacao)
    {
    case '+':
        res = num1 + num2;
        printf("O resultado da operaçao é: %d", res);
        break;
    case '-':
        res = num1 - num2;
        printf("O resultado da operaçao é: %d", res);
        break;
    case '*':
        res = num1 * num2;
        printf("O resultado da operaçao é: %d", res);
        break;
    case'/':
        res = num1 / num2;
        printf("O resultado da operaçao é: %d", res);
        break;
    default:
        printf("Operação não reconhecida!!");
        break;
    }

    return (0);
}