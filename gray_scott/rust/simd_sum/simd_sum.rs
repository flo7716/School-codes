#![feature(portable_simd)]  // Release the nightly compiler kraken

use multiversion::{multiversion, target::selected_target};
use std::simd::prelude::*;

// While targets("simd") is a thing, and you may want to use it where full
// hardware portability is desired, it will result in a lot of code bloat
// that will make your build very slow in more realistic code.
#[multiversion(targets("x86_64+avx2+fma", "x86_64+avx", "x86_64+sse2"))]
fn simd_sum(v: &Vec<f32>) -> f32 {
    // This code uses a few advanced language feature that we do not have time
    // to cover during this short course. But feel free to ask the teacher about
    // it, or just copy-paste it around.
    const SIMD_WIDTH: usize = const {
        if let Some(width) = selected_target!().suggested_simd_width::<f32>() {
            width
        } else {
            1
        }
    };
    let (peel, body, tail) = v.as_simd::<SIMD_WIDTH>();
    let simd_sum = body.into_iter().sum::<Simd<f32, SIMD_WIDTH>>();
    let scalar_sum = peel.into_iter().chain(tail).sum::<f32>();
    simd_sum.reduce_sum() + scalar_sum
}

fn main() {
    let v = vec![1.2, 3.4, 5.6, 7.8, 9.0, 11.2, 13.4, 15.6];
    let result = simd_sum(&v);
    println!("{:?}", result);
}