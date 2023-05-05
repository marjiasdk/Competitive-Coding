#include <stdio.h>

int main() {
    char sentence[100];
    // read up to 99 characters from stdin and save them to "sentence"
    // fgets will read until it encounters a newline character
    // it is better than 'scanf("%[^\n]", sentence)' because it will not leave the newline character in the buffer & will not overflow the buffer
    // the "buffer" is the memory location where the input is stored, in this case "sentence", which is an array of characters
    fgets(sentence, sizeof(sentence), stdin);
    printf("Hello, World!\n%s", sentence);
    return 0;
}
