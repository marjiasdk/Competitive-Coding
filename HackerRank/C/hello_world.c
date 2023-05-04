#include <stdio.h>

int main() {
    // declares array of characters called "sentence", with a size of 100
    char sentence[100];
    // read line of input from stdin and save it to "sentence"
    // until it encounters a new line character 
    // [^\n] means "read until you encounter a new line character"
    scanf("%[^\n]", sentence);
    // %s means "print a string"
    printf("Hello, World!\n%s", sentence);
    return 0;
}