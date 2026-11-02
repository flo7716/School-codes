<?php
require __DIR__.'/db.php';
$conn = mysqli_connect($DB_HOST, $DB_USER, $DB_PASSWORD, $DB_NAME);
include __DIR__.'/layout_top.php';

$form = '<div class="box"><form method="post">
<input name="u" placeholder="Utilisateur"> <input name="p" type="password" placeholder="Mot de passe">
<button>Connexion</button></form></div>';

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    echo $form;
} else {
    $u = $_POST['u'] ?? ''; $p = $_POST['p'] ?? '';
    $stmt = mysqli_prepare($conn, "SELECT id FROM users WHERE username=? AND password=?");
    mysqli_stmt_bind_param($stmt, "ss", $u, $p);
    mysqli_stmt_execute($stmt);
    mysqli_stmt_store_result($stmt);
    if (mysqli_stmt_num_rows($stmt) === 1) {
        error_log("event=login_ok user=".$u);
        echo "<div class='box'>Bienvenue $u</div>";
    } else {
        error_log("event=login_fail user=".$u);
        http_response_code(401);
        echo $form."<p>Identifiants invalides.</p>";
    }
}
include __DIR__.'/layout_bottom.php';
