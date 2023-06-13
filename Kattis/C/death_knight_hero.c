#include <stdio.h>
#include <string.h>

// this avoids run-time error
#define MAX_LENGTH 1001

int main() {
    int n;
    scanf("%d", &n);

    int i = 0;
    int win = 0;
    while (i < n) {
        char command[MAX_LENGTH];
        scanf("%s", command);
        // strstr returns NULL if the string is not found
        if (strstr(command, "CD") == NULL) {
            win++;
        }
        
        i++;
    }

    printf("%d", win);

    return 0;
}
