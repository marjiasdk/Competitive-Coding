#include <stdio.h>
#include <math.h>

int main(void) {
    int a;
    scanf("%d", &a);

    // (int) is used to convert the result of pow() to integer
    // pow() returns double
    printf("%d\n", (int)pow(2, a) - a - 1);
    
    return 0;
}
