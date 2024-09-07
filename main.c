#include <stdio.h>

int main() {
    int a = 5;
    int b = 0;

    if (b == 0) {
        printf("Error: cannot divide by zero!\n");
        return 1; // or exit() or any other error handling mechanism
    }

    int result = a / b;

    printf("Result: %d\n", result);

    return 0;
}