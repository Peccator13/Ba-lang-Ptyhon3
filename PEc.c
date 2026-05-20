#include <stdio.h>
int main() {
    printf("salve Peccator!\n");
    printf("yaşini yaz Peccator:\n");
    int yas;
    scanf("%d", &yas);
    if (yas < 18)
    {
        printf("Sen daha çocuksun!\n");

    }
    else if (yas >= 18)
    {
        printf("reşit olmuşsun sisteme hoşgeldin!\n");
    
    }
    return 0;
}
