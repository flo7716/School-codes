#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>


int main(int argc, char **argv) {
    struct stat stat_fic;
    if(stat(argv[1], &stat_fic) != 0){
        fprintf(stderr, "Erreur lors de l'ouverture du fichier %s\n", argv[1]);
        exit(1);
    }
    switch (stat_fic.st_mode & S_IFMT) {
        case S_IFREG:
            printf("Le fichier %s est un fichier régulier.\n", argv[1]);
            break;
        case S_IFDIR:
            printf("Le fichier %s est un répertoire.\n", argv[1]);
            break;
        case S_IFLNK:
            printf("Le fichier %s est un lien symbolique.\n", argv[1]);
            break;
        default:
            printf("Le fichier %s est d'un type non reconnu.\n", argv[1]);
    }
    return 0;
}