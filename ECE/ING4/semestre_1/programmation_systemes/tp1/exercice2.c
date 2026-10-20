#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <sys/types.h>


int main(int argc, char *argv[]) {
    if (argc !=3) {
        fprintf(stderr, "Usage : %s <fichier1> <fichier2>\n", argv[0]);
        return -1;
    }

    struct stat stat_file1; 
    struct stat stat_file2;

    //2. Appel de la primitive stat sur le 1er fichier
    if (stat(argv[1], &stat_file1) == -1) {
        fprintf(stderr, "Erreur lors de l'appel à stat sur le 1er fichier : %s\n", argv[1]);
        return 2; // erreur code 2 sur l'appel a stat du fichier 1
    }

    //3. Appel de la primitive stat sur le 2eme fichier

    if (stat(argv[2], &stat_file2) == -1) {
        fprintf(stderr, "Erreur lors de l'appel à stat sur le 2eme fichier : %s\n", argv[2]);
        return 2; // erreur code 2 sur l'appel a stat du fichier 2
    }

    //4. Comparaison des informations des deux fichiers (i-noeuds et disque logique)
    if (stat_file1.st_ino == stat_file2.st_ino && stat_file1.st_dev == stat_file2.st_dev) {
        fprintf(stdout, "Les deux fichiers sont les mêmes.\n");
        return 0;
    } else {
        fprintf(stdout, "Les deux fichiers sont différents.\n");
        return 1;
    }

    return 0;
}

