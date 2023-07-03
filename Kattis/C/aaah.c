#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {
    char jon[1000];
    char doc[1000];

    scanf("%s", jon);
    scanf("%s", doc);

    if (strlen(jon) < strlen(doc)) {
        printf("no\n");
    } else {
        printf("go\n");
    }
    return 0;
}