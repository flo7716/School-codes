#include <stdio.h>
#include <string.h>

int main() {
    char password[10];
    printf("Mot de passe: ");
    scanf("%s", password);

    if(strcmp(password, "secret123") == 0) {
        printf("Acces autorise\n");
    } else {
        printf("Refuse\n");
    }
    return 0;
}