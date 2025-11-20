fn outsourcing(x: u8, y: u8) {
    let sum = |a: u8, b: u8| -> u8 { a + b };
    println!("{}", sum(x, y));
}
fn main() {
    let x: u8 = 5;
    let y: u8 = 10;

    outsourcing(x, y);
}