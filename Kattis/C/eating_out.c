#include <stdio.h>

int main() {
    int m, a, b, c;
    scanf("%d %d %d %d", &m, &a, &b, &c);

    if (m * 2 < a + b + c) {
        printf("impossible");
    } else {
        printf("possible");
    }
    
    return 0;
}