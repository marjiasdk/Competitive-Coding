#include <stdio.h>
#include <string.h>

int main() {
    char str[100];
    // %s is used because we are printing a string
    scanf("%s", str);

    for (int i = 0; i < strlen(str); i++) {
        if (str[i] >= 'A' && str[i] <= 'Z') {
            // %c is used and not %s because we are printing a single character
            printf("%c", str[i]);
        }
    }

    return 0;
}