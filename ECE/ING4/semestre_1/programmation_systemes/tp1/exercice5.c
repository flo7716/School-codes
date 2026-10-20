#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>

int main(int argc, char **argv) {
    if (argc != 2) {
        fprintf(stderr, "Usage : %s <nom_du_fichier>\n", argv[0]);
        exit(1);
    }

    // 1. Création et ouverture du fichier en écriture seule
    int fd = open(argv[1], O_CREAT | O_WRONLY | O_TRUNC, 0644);
    if (fd == -1) {
        fprintf(stderr, "Erreur lors de la création du fichier\n");
        exit(1);
    }

    // 2. Positionnement de la tête de lecture/écriture sur le 10 000e octet (offset = 10000)
    // SEEK_SET indique que le déplacement se fait par rapport au début du fichier.
    off_t res = lseek(fd, 10000, SEEK_SET);
    if (res == -1) {
        fprintf(stderr, "Erreur lors de l'appel à lseek\n");
        close(fd);
        exit(1);
    }

    // 3. Écriture d'un caractère à cette position (ex: 'X')
    char c = 'X';
    if (write(fd, &c, 1) != 1) {
        fprintf(stderr, "Erreur lors de l'écriture\n");
        close(fd);
        exit(1);
    }

    // 4. Fermeture du fichier
    close(fd);
    printf("Fichier créé avec succès. Offset atteint : %lld\n", (long long) res);

    return 0;
}