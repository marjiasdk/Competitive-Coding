#include <stdio.h>

int main() {
    int a, b;
    scanf("%d%d", &a, &b);

    float result = (a * b) / 2.0;

    if (result == (int)result) {
        printf("%d", (int)result);
    } else {
        printf("%g", result);
    }

    return 0;
}
