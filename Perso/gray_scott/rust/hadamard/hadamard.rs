fn hadamard(v1: Vec<f32>, v2: Vec<f32>) -> Vec<f32> {
    assert_eq!(v1.len(), v2.len());
    v1.into_iter().zip(v2)
                  .map(|(x1, x2)| x1 * x2)
                  .collect() 
}

fn main() {
    let v1 = vec![1.2, 3.4, 5.6];
    let v2 = vec![9.8, 7.6, 5.4];
    let result = hadamard(v1, v2);
    println!("{:?}", result);
}