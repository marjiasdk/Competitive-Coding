#include <stdio.h>

int main() {
    // [100] is the maximum length of the string
    char sentence[100];
    // %[^\n] is used to read the string with spaces
    scanf("%[^\n]", sentence);
    // %s is used to print the string
    printf("Hello, World!\n%s", sentence);
    return 0;
}