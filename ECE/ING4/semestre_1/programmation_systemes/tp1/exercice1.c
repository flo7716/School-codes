#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>
#include <time.h>
#include <pwd.h>
#include <grp.h>

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage : %s <chemin_du_fichier>\n", argv[0]);
        exit(EXIT_FAILURE);
    }

    struct stat file_stat;

    // Utilisation de stat avec le chemin du fichier
    if (stat(argv[1], &file_stat) == -1) {
        perror("Erreur lors de l'appel à stat");
        exit(EXIT_FAILURE);
    }

    printf("--- Informations du fichier (via stat) ---\n");
    
    // 1. Numéro d'inode
    printf("1. Numéro d'inode : %lu\n", (unsigned long) file_stat.st_ino);

    // 2. Nombre de liens
    printf("2. Nombre de liens : %lu\n", (unsigned long) file_stat.st_nlink);

    // 3. Propriétaire
    struct passwd *pwd = getpwuid(file_stat.st_uid);
    if (pwd != NULL) {
        printf("3. Propriétaire : %s (UID: %d)\n", pwd->pw_name, file_stat.st_uid);
    } else {
        printf("3. Propriétaire UID : %d\n", file_stat.st_uid);
    }

    // 4. Groupe
    struct group *grp = getgrgid(file_stat.st_gid);
    if (grp != NULL) {
        printf("4. Groupe : %s (GID: %d)\n", grp->gr_name, file_stat.st_gid);
    } else {
        printf("4. Groupe GID : %d\n", file_stat.st_gid);
    }

    // 5. Taille
    printf("5. Taille : %lld octets\n", (long long) file_stat.st_size);

    // 6. Type du fichier
    printf("6. Type : ");
    if (S_ISREG(file_stat.st_mode))      printf("Fichier régulier\n");
    else if (S_ISDIR(file_stat.st_mode)) printf("Répertoire\n");
    else if (S_ISLNK(file_stat.st_mode)) printf("Lien symbolique\n");
    else if (S_ISCHR(file_stat.st_mode)) printf("Périphérique mode caractère\n");
    else if (S_ISBLK(file_stat.st_mode)) printf("Périphérique mode bloc\n");
    else if (S_ISFIFO(file_stat.st_mode))printf("FIFO (tube nommé)\n");
    else if (S_ISSOCK(file_stat.st_mode))printf("Socket\n");
    else                                 printf("Inconnu\n");

    // 7. Heure du dernier accès
    printf("7. Dernier accès : %s", ctime(&file_stat.st_atime));

    return 0;
}