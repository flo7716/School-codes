%Paramètres
f0=100; %fréquence du cosinus
Fe=1000; %fréquence d'échantillonnage
Te=1/Fe; %période d'échantillonnage
N=100; %nombre d'échantillons

%Génération du signal
x=cos(2*pi*f0*(0:Te:N*Te));

%Tracé du signal
figure; plot((0:Te:N*Te),x)

%Calcul de la TFD du signal
X=fft(x);

%Tracé du module de la TFD du signal
figure; plot(linspace(-Fe/2,Fe/2,length(X)),fftshift(abs(X)))