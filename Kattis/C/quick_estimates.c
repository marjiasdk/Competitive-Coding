#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main() {
    int n;
    scanf("%d", &n);
    int i = 0;
    while (i < n) {
        char a[100];
        scanf("%s", a);
        printf("%d\n", strlen(a));
        i++;
    }
    return 0;
}