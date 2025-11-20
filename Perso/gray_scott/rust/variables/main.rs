fn main() {
    // Étape 1 : variable immuable x
    let x: i32 = 5;

    // Étape 2 : variable mutable y
    let mut y: i32 = 10;

    // Étape 3 : affichage
    println!("x = {}", x);
    println!("y = {}", y);

    // Étape 4 : modification de y
    y = y + 3;

    // Étape 5 : nouvel affichage
    println!("y après modification = {}", y);
}
