% Nombre de cercles à tracer
nombreCercles = 5;

% Définir les rayons et les centres de chaque cercle
rayons = linspace(0.2, 1, nombreCercles);
centres_x = linspace(-2, 2, nombreCercles);
centres_y = linspace(-2, 2, nombreCercles);

% Initialiser la figure
figure;

% Boucle pour tracer les cercles
for i = 1:nombreCercles
    % Les valeurs de theta pour un cercle complet
    theta = linspace(0, 2*pi, 100);

    % Les valeurs de x et y pour le cercle avec un rayon et centre spécifiques
    x = rayons(i) * cos(theta) + centres_x(i);
    y = rayons(i) * sin(theta) + centres_y(i);

    % Tracer le cercle
    plot(x, y, 'linewidth', 1.5);
    hold on;
end

hold off;

% Ajouter des titres et des labels
title('Cercles avec rayons et centres variables');
xlabel('X');
ylabel('Y');
grid on;
axis equal;