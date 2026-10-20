#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <pwd.h>
#include <grp.h>
#include <time.h>

int main(int argc, char **argv) {
    if (argc != 2) {
        fprintf(stderr, "Usage : %s <chemin_du_fichier>\n", argv[0]);
        exit(1);
    }

    // Ouverture du fichier en lecture seule pour obtenir un descripteur de fichier
    int fd = open(argv[1], O_RDONLY);
    if (fd == -1) {
        fprintf(stderr, "Erreur à l'ouverture du fichier %s\n", argv[1]);
        exit(1);
    }

    struct stat stat_fic;

    // Utilisation de fstat avec le descripteur de fichier
    if (fstat(fd, &stat_fic) != 0) {
        fprintf(stderr, "Erreur à la lecture des informations via fstat\n");
        close(fd);
        exit(1);
    }

    // 1. Numéro d'inode
    printf("1. Numéro d'inode : %lu\n", (unsigned long) stat_fic.st_ino);

    // 2. Nombre de liens physiques
    printf("2. Nombre de liens : %lu\n", (unsigned long) stat_fic.st_nlink);

    // 3. Propriétaire
    struct passwd *pwd = getpwuid(stat_fic.st_uid);
    if (pwd != NULL) {
        printf("3. Propriétaire : %s (UID: %d)\n", pwd->pw_name, stat_fic.st_uid);
    } else {
        printf("3. Propriétaire UID : %d\n", stat_fic.st_uid);
    }

    // 4. Groupe propriétaire
    struct group *grp = getgrgid(stat_fic.st_gid);
    if (grp != NULL) {
        printf("4. Groupe : %s (GID: %d)\n", grp->gr_name, stat_fic.st_gid);
    } else {
        printf("4. Groupe GID : %d\n", stat_fic.st_gid);
    }

    // 5. Taille du fichier en octets
    printf("5. Taille : %ld octets\n", (long) stat_fic.st_size);

    // 6. Type du fichier
    printf("6. Type : ");
    switch (stat_fic.st_mode & S_IFMT) {
        case S_IFREG:
            printf("Fichier régulier\n");
            break;
        case S_IFDIR:
            printf("Répertoire\n");
            break;
        case S_IFLNK:
            printf("Lien symbolique\n");
            break;
        case S_IFCHR:
            printf("Fichier spécial caractère\n");
            break;
        case S_IFBLK:
            printf("Fichier spécial bloc\n");
            break;
        case S_IFIFO:
            printf("Tube nommé\n");
            break;
        case S_IFSOCK:
            printf("Socket\n");
            break;
        default:
            printf("Type de fichier inconnu\n");
            break;
    }

    // 7. Heure du dernier accès (format lisible via ctime)
    printf("7. Dernier accès : %s", ctime(&stat_fic.st_atime));

    // Fermeture du descripteur de fichier
    close(fd);

    return 0;
}