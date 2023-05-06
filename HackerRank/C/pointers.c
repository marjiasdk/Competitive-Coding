/*

pointer is a way to share memory address among different contexts.
used whenever function need to modify content it doesn't own.

to access memory address of variable, prepend w/ &.

example: &val return memory address of val.

memory address is assigned to pointer & can be shared amongst various functions.

int*p = &val will assign memory address of val to pointer p.
to access content of memory to which it points, prepend w/ *.

example: *p will return content of val.

*/

#include <stdio.h>

// a & b have * before them because they are pointers
void update(int *a,int *b) {
    int sum = *a + *b;
    int diff = *a - *b;
    // if diff is negative, make it positive
    if (diff < 0) {
        diff = -diff;
    }
    *a = sum;
    *b = diff;  
}

int main() {
    int a, b;
    // pa & pb have * before them because they are pointers
    // we assign pa & pb to memory address of a & b
    // this allows us to modify a & b in update function
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}