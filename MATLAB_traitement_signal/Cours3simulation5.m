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
X1=fft(x);
X2=fft(x,128);
X3=fft(x,256);
X4=fft(x,512);

%Tracé du module de la TFD du signal 
figure;
subplot(2,2,1)
plot(linspace(0,Fe,length(X1)),abs(X1))
xlabel('Fréquences en Hz')
subplot(2,2,2)
plot(linspace(0,Fe,length(X2)),abs(X2))
xlabel('Fréquences en Hz')
subplot(2,2,3)
plot(linspace(0,Fe,length(X3)),abs(X3))
xlabel('Fréquences en Hz')
subplot(2,2,4)
plot(linspace(0,Fe,length(X4)),abs(X4))
xlabel('Fréquences en Hz')