#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int n;
    scanf("%d", &n);
    for (int i = 1; i < n + 1; i++) {
        printf("%d Abracadabra\n", i);
    }
    return 0;
}