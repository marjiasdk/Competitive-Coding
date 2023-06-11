#include <stdio.h>

int main(void) {
    // unsigned long long is used instead of integer to avoid overflow
    // overflow occurs when the number is too large to be stored in the variable
    // long long is at least 64 bits, which is enough to store 2^64 - 1
    unsigned long long n;
    // llu is used to print unsigned long long
    while (scanf("%llu", &n) != EOF) {
        unsigned long long temp = 1;
        while (temp < n) {
            temp *= 9;
            if (temp >= n) {
                printf("Stan wins.\n");
                break;
            }
            temp *= 2;
            if (temp >= n) {
                printf("Ollie wins.\n");
                break;
            }
        }
    }
    return 0;
}