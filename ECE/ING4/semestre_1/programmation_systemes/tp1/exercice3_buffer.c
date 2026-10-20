#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>

int main(int argc, char **argv) {
    if (argc != 2) {
        fprintf(stderr, "Usage : %s <fichier_regulier>\n", argv[0]);
        exit(1);
    }

    int fd = open(argv[1], O_RDONLY);
    if (fd == -1) {
        fprintf(stderr, "Erreur à l'ouverture du fichier\n");
        exit(1);
    }

    struct stat stat_fic;
    if (fstat(fd, &stat_fic) != 0) {
        fprintf(stderr, "Erreur lors de l'appel à fstat\n");
        close(fd);
        exit(1);
    }

    if ((stat_fic.st_mode & S_IFMT) != S_IFREG) {
        fprintf(stderr, "Erreur : Ce n'est pas un fichier régulier.\n");
        close(fd);
        exit(1);
    }

    // Modification : Utilisation d'un buffer de 1024 octets
    char buffer[1024];
    ssize_t nb_lus;

    while ((nb_lus = read(fd, buffer, sizeof(buffer))) > 0) {
        write(STDOUT_FILENO, buffer, nb_lus);
    }

    close(fd);

    return 0;
}