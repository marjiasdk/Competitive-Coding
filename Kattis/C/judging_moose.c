#include <stdio.h>

int main(void) {
    int left, right;
    scanf("%d %d", &left, &right);
    if (left == 0 && right == 0) {
        printf("Not a moose");
    } else if (left == right) {
        printf("Even %d", left + right);
    } else if (left > right) {
        printf("Odd %d", 2 * left);
    } else {
        printf("Odd %d", 2 * right);
    }
    return 0;
}
