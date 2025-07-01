clear all;
close all;
clc

% Signal
x = [1, 2, 1, 0];

% Calcul du spectre d'amplitude
X = fft(x);

% Tracé du spectre d'amplitude
N = length(x);
f = (0:N-1)*(1/N); % Calcul des fréquences normalisées
stem(f, abs(X));
xlabel('Fréquence normalisée');
ylabel('Amplitude');
title('Spectre d\amplitude de x(n)');
grid on;

Nffts = [8, 16, 32]; % Différentes valeurs de Nfft

figure;
for i = 1:length(Nffts)
    Nfft = Nffts(i);
    X = fft(x, Nfft);
    f = (0:Nfft-1)*(1/Nfft); % Calcul des fréquences normalisées
    subplot(length(Nffts), 1, i);
    stem(f, abs(X));
    xlabel('Fréquence normalisée');
    ylabel('Amplitude');
    title(['Spectre d\amplitude de x(n) avec Nfft = ', num2str(Nfft)]);
    grid on;
end

zero_paddings = [4, 12]; % Différents nombres de zéros à ajouter

figure;
for i = 1:length(zero_paddings)
    zero_padding = zero_paddings(i);
    x_zero_padded = [x, zeros(1, zero_padding)];
    X = fft(x_zero_padded);
    N = length(x_zero_padded);
    f = (0:N-1)*(1/N); % Calcul des fréquences normalisées
    subplot(length(zero_paddings), 1, i);
    stem(f, abs(X));
    xlabel('Fréquence normalisée');
    ylabel('Amplitude');
    title(['Spectre d\amplitude de x(n) avec ', num2str(zero_padding), ' zéros ajoutés']);
    grid on;
end
