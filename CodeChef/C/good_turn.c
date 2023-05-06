/*

sample input:
4
1 4
3 4
4 2
2 6

sample output:
NO
YES
NO
YES

*/

#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);
    int i = 0;
    while (i < n) {
        int a, b;
        scanf("%d %d", &a, &b);
        if (a + b > 6) {
            printf("YES\n");
        } else {
            printf("NO\n");
        }
    i++;
    }
	return 0;
}
