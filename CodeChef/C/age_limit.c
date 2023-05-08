#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    int i;

    for (i = 0; i < n; i++) 
    {
        int x, y, a;
        // we need to add & before the variable name because we are taking input from the user
        scanf("%d %d %d", &x, &y, &a);
        // we don't need to add & before the variable name because we are printing the value of the variable
        if (a >= x && y > a) 
        {
            printf("YES\n");
        } 
        else 
        {
            printf("NO\n");
        }

    }

    return 0;
}