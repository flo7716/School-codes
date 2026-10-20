import sys
import os
import exifread
import webbrowser

def convert_to_degrees(value):
    """
    Convertit une coordonnée GPS (degrés, minutes, secondes) issue d'exifread
    en degrés décimaux.
    """
    d = float(value.values[0].num) / float(value.values[0].den)
    m = float(value.values[1].num) / float(value.values[1].den)
    s = float(value.values[2].num) / float(value.values[2].den)

    return d + (m / 60.0) + (s / 3600.0)

def extract_exif_gps(image_path):
    if not os.path.exists(image_path):
        print(f"Erreur : Le fichier '{image_path}' n'existe pas.")
        return

    print(f"=== Lecture de l'image : {image_path} ===\n")
    
    # 1. Ouverture et lecture de l'image avec exifread
    with open(image_path, 'rb') as f:
        tags = exifread.process_file(f)

    if not tags:
        print("Aucune métadonnée EXIF trouvée.")
        return

    # 2. Affichage de l'ensemble des métadonnées
    print("--- Métadonnées EXIF trouvées ---")
    for tag in tags.keys():
        if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
            print(f"{tag}: {tags[tag]}")
    print("-" * 40 + "\n")

    # 3. Récupération des tags GPS
    gps_latitude = tags.get('GPS GPSLatitude')
    gps_latitude_ref = tags.get('GPS GPSLatitudeRef')
    gps_longitude = tags.get('GPS GPSLongitude')
    gps_longitude_ref = tags.get('GPS GPSLongitudeRef')

    if gps_latitude and gps_latitude_ref and gps_longitude and gps_longitude_ref:
        print("--- Tags GPS détectés ---")
        print(f"Latitude  : {gps_latitude} {gps_latitude_ref}")
        print(f"Longitude : {gps_longitude} {gps_longitude_ref}\n")

        # 4. Conversion en coordonnées décimales (compatible Google Maps)
        lat = convert_to_degrees(gps_latitude)
        if gps_latitude_ref.values[0] != 'N':
            lat = -lat

        lon = convert_to_degrees(gps_longitude)
        if gps_longitude_ref.values[0] != 'E':
            lon = -lon

        print(f"Coordonnées au format décimal : {lat:.6f}, {lon:.6f}")

        # 5. Génération et ouverture du lien Google Maps
        maps_url = f"https://www.google.com/maps?q={lat},{lon}"
        print(f"\nLien Google Maps généré :\n{maps_url}")

        # Ouvrir automatiquement dans le navigateur par défaut
        webbrowser.open(maps_url)

    else:
        print("Aucune coordonnée GPS trouvée dans cette image.")

if __name__ == "__main__":
    # Vérification qu'un argument a bien été fourni
    if len(sys.argv) < 2:
        print("Usage: python3 exif_gps.py <chemin_vers_image>")
        sys.exit(1)

    # Récupération du chemin passé en argument
    image_file = sys.argv[1]
    extract_exif_gps(image_file)