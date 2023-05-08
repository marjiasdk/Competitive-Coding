// add two numbers
/*

input:
3
1 2
100 200
10 40

output:
3
300
50

*/

#include <stdio.h>

int main() {
    int n;
    int i;

    scanf("%d", &n);

    for (i = 0; i < n; i++) {
        int a, b;
        // we do not write sum = a + b; here because we do not need to store the sum
        // if we do then we will get wrong answer
        scanf("%d %d", &a, &b);
        // we can also write printf("%d\n", a + b);
        int sum = a + b;
        printf("%d\n", sum);
    }

    return 0;
}