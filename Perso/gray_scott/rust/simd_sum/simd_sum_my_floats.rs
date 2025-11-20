// This is a hardware-dependent constant, here picked for x86's AVX
const HARDWARE_SIMD_WIDTH: usize = 8;

fn simd_sum_my_floats(v: &Vec<f32>) -> f32 {
    let mut accs = [0.0; HARDWARE_SIMD_WIDTH];
    let chunks = v.chunks_exact(HARDWARE_SIMD_WIDTH);
    let remainder = chunks.remainder();
    // We are not doing instruction-level parallelism for now. See next chapter.
    for chunk in chunks {
        // This loop will compile into a single fast SIMD addition instruction
        for (acc, element) in accs.iter_mut().zip(chunk) {
            *acc += *element;
        }
    }
    for (acc, element) in accs.iter_mut().zip(remainder) {
        *acc += *element;
    }
    // This would need to be tuned for optimal efficiency at small input sizes
    accs.into_iter().sum()
}
fn main() {
    let v = vec![1.2, 3.4, 5.6, 7.8, 9.0, 11.2, 13.4, 15.6];
    let result = simd_sum_my_floats(&v);
    println!("{:?}", result);
}