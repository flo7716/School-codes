#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>

int main(int argc, char **argv) {
    // 1. Vérification du nombre d'arguments (nom du programme + source + destination)
    if (argc != 3) {
        fprintf(stderr, "Usage : %s <fichier_source> <fichier_destination>\n", argv[0]);
        exit(1);
    }

    // 2. Ouverture du fichier source en lecture seule (bas niveau)
    int fd_src = open(argv[1], O_RDONLY);
    if (fd_src == -1) {
        fprintf(stderr, "Erreur : impossible d'ouvrir le fichier source '%s'\n", argv[1]);
        exit(1);
    }

    // 3. Récupération des attributs du fichier source (notamment st_mode pour les droits) via fstat
    struct stat stat_src;
    if (fstat(fd_src, &stat_src) != 0) {
        fprintf(stderr, "Erreur lors de l'appel à fstat sur le fichier source\n");
        close(fd_src);
        exit(1);
    }

    // 4. Vérification optionnelle : s'assurer que la source est un fichier régulier
    if ((stat_src.st_mode & S_IFMT) != S_IFREG) {
        fprintf(stderr, "Erreur : '%s' n'est pas un fichier régulier.\n", argv[1]);
        close(fd_src);
        exit(1);
    }

    // 5. Ouverture/Création du fichier de destination
    // On utilise O_CREAT pour le créer s'il n'existe pas, O_WRONLY pour écrire, et O_TRUNC pour vider le fichier s'il existait déjà.
    // On extrait les droits d'accès du fichier source (st_mode & 0777) pour les appliquer au nouveau fichier.
    int fd_dest = open(argv[2], O_CREAT | O_WRONLY | O_TRUNC, stat_src.st_mode & 0777);
    if (fd_dest == -1) {
        fprintf(stderr, "Erreur : impossible de créer ou d'ouvrir le fichier destination '%s'\n", argv[2]);
        close(fd_src);
        exit(1);
    }

    // 6. Recopie du contenu par blocs de 1024 octets (read / write)
    char buffer[1024];
    ssize_t nb_lus, nb_ecrits;

    while ((nb_lus = read(fd_src, buffer, sizeof(buffer))) > 0) {
        nb_ecrits = write(fd_dest, buffer, nb_lus);
        if (nb_ecrits != nb_lus) {
            fprintf(stderr, "Erreur lors de l'écriture dans le fichier destination\n");
            close(fd_src);
            close(fd_dest);
            exit(1);
        }
    }

    if (nb_lus == -1) {
        fprintf(stderr, "Erreur lors de la lecture du fichier source\n");
    }

    // 7. Fermeture des descripteurs de fichiers ouverts
    close(fd_src);
    close(fd_dest);

    return 0;
}