<?php
require __DIR__.'/db.php';
$conn = mysqli_connect($DB_HOST, $DB_USER, $DB_PASSWORD, $DB_NAME);
include __DIR__.'/layout_top.php';

$q = $_GET['q'] ?? '';
// VOLONTAIREMENT VULNÉRABLE (CWE-89) : concaténation directe, pas de requête préparée
$sql = "SELECT nom, description FROM produits WHERE nom LIKE '%$q%'";
echo "<div class='box'>";
$res = mysqli_query($conn, $sql);
if ($res === false) {
    // Message d'erreur verbeux volontaire (facilite la découverte de l'injection)
    echo "<p>Erreur SQL : ".htmlspecialchars(mysqli_error($conn))."</p>";
} else {
    echo "<table>";
    while ($row = mysqli_fetch_assoc($res)) {
        echo "<tr><td><b>".htmlspecialchars($row['nom'])."</b></td><td>".htmlspecialchars($row['description'])."</td></tr>";
    }
    echo "</table>";
}
echo "</div>";
include __DIR__.'/layout_bottom.php';
