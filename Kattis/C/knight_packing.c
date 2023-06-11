#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);

    if (n % 2 == 0) {
        printf("second\n");
    } else {
        printf("first\n");
    }
    return 0;
}