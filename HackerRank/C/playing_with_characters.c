#include <stdio.h>

int main() {
    char ch;
    char s[100];
    char sen[100];

    scanf("%c", &ch);
    // %s is a format specifier for a string
    scanf("%s\n", &s);
    // %c is a format specifier for a character

    /*
    %[^\n] reads in a string of characters until it encounters a newline character (\n). The [^\n] means "any character that is not a newline".
    %*c reads in a single character and discards it. The * means "suppress assignment", so the character is read in but not stored anywhere.
    */
    scanf("%[^\n]%*c", &sen);

    printf("%c\n", ch);
    printf("%s\n", s);
    printf("%s\n", sen);

    return 0;
}