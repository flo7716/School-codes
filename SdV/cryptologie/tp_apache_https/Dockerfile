FROM php:8.2-apache

# Activer le module SSL
RUN a2enmod ssl

# Copier configuration SSL personnalisée
COPY default-ssl.conf /etc/apache2/sites-available/default-ssl.conf

# Activer le site SSL
RUN a2ensite default-ssl.conf

# Copier le contenu web
COPY www/ /var/www/

# Exposer ports
EXPOSE 80
EXPOSE 443
