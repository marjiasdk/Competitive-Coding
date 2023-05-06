#include <stdio.h>

int main(void) {
	int n;

    // the & operator is used to get the address of a variable
    // the address is used to read or write to the variable
    scanf("%d", &n);
    printf("%d", n);
	return 0;
}