#include <stdio.h>

// int main() & int main(void) are both valid, there is no difference. 
// int main(int argc, char *argv[]) is also valid, but we will not use it.
// this is because we are not using command line arguments.

int main() {
    int a, b;
    scanf("%d %d", &a, &b);

    if (a > b) {
        printf("%d %d" , b, a);
    } else {
        printf("%d %d" , a, b);
    }
    return 0;
}