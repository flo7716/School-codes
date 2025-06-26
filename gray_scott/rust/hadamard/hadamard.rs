fn hadamard(v1: Vec<f32>, v2: Vec<f32>) -> Vec<f32> {
    assert_eq!(v1.len(), v2.len());
    v1.into_iter().zip(v2)
                  .map(|(x1, x2)| x1 * x2)
                  .collect() 
}
assert_eq!(
    hadamard(vec![1.2, 3.4, 5.6], vec![9.8, 7.6, 5.4]),
    [
        1.2 * 9.8,
        3.4 * 7.6,
        5.6 * 5.4
    ]
);