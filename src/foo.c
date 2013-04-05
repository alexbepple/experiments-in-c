#include <stdio.h>
#include <stdlib.h>
#include "Bar.h"

int foo() {
    return bar();
}

int main()
{
    printf("%d", foo());
    return 0;
}
