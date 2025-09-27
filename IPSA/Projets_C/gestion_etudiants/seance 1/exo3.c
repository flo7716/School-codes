#include <stdio.h>
#include <math.h>
int main()
{
    int x;
    printf("donner un entier svp: ");
    scanf("%d",&x);
    if(x%2==0)
    {
        printf("%d est pair",x);
    }
    else
    {
        printf("%d est impair",x);
    }
    return 0;
}

