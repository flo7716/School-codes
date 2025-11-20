use ndarray::ArrayViewMut2;

#[inline]
pub fn stencil_iter<'data, const SIMD_WIDTH: usize>(
    start_u: ArrayView2<'data, Vector<SIMD_WIDTH>>,
    start_v: ArrayView2<'data, Vector<SIMD_WIDTH>>,
    mut end_u_center: ArrayViewMut2<'data, Vector<SIMD_WIDTH>>,
    mut end_v_center: ArrayViewMut2<'data, Vector<SIMD_WIDTH>>,
) -> impl Iterator<
    Item = (
        ArrayView2<'data, Vector<SIMD_WIDTH>>, // <- Input u window
        ArrayView2<'data, Vector<SIMD_WIDTH>>, // <- Input v window
        &'data mut Vector<SIMD_WIDTH>,         // <- Output u
        &'data mut Vector<SIMD_WIDTH>,         // <- Output v
    ),
>
where
    LaneCount<SIMD_WIDTH>: SupportedLaneCount,
{
    // Assert that the sub-grids all have the expected memory layout.
    assert_eq!(start_u.shape(), start_v.shape());
    assert_eq!(end_u_center.shape(), end_v_center.shape());
    assert_eq!(start_u.shape().len(), 2);
    assert_eq!(end_u_center.shape().len(), 2);
    assert!(start_u
        .shape()
        .iter()
        .zip(end_u_center.shape())
        .all(|(start_dim, end_dim)| *start_dim == end_dim + 2));
    assert_eq!(start_u.strides(), start_v.strides());
    assert_eq!(start_u.strides(), end_u_center.strides());
    assert_eq!(start_u.strides(), end_v_center.strides());

    // Collect and check common layout information
    let in_shape = [start_u.shape()[0], start_u.shape()[1]];
    assert!(in_shape.into_iter().min().unwrap() >= 2);
    let strides = start_u.strides();
    assert_eq!(strides.len(), 2);
    assert!(strides.iter().all(|stride| *stride > 0));
    let [row_stride, col_stride] = [strides[0] as usize, strides[1] as usize];
    assert_eq!(col_stride, 1);
    let [out_rows, out_cols] = in_shape.map(|dim| dim - 2);

    // Determine how many elements we must skip in order to go from the
    // past-the-end element of one row to the first element of the next row.
    let next_row_step = row_stride - out_cols;

    // Prepare a way to access input windows and output refs by output position
    // The safety of the closures below is actually asserted on the caller's
    // side, but sadly unsafe closures aren't a thing in Rust yet.
    let stencil_shape = [STENCIL_WEIGHTS.len(), STENCIL_WEIGHTS[0].len()];
    let window_shape = (stencil_shape[0], stencil_shape[1]).strides((row_stride, 1));
    let unchecked_output = move |out_ptr: *mut Vector<SIMD_WIDTH>| unsafe { &mut *out_ptr };
    let unchecked_input_window = move |in_ptr: *const Vector<SIMD_WIDTH>| unsafe {
        ArrayView2::from_shape_ptr(window_shape, in_ptr)
    };

    // Recipe to emit the currently selected input windows and output references,
    // then move to the next column. As before, this is only safe if called with
    // correct element pointers.
    let emit_and_increment =
        move |in_u_ptr: &mut *const Vector<SIMD_WIDTH>,
              in_v_ptr: &mut *const Vector<SIMD_WIDTH>,
              out_u_ptr: &mut *mut Vector<SIMD_WIDTH>,
              out_v_ptr: &mut *mut Vector<SIMD_WIDTH>| unsafe {
            let win_u = unchecked_input_window(*in_u_ptr);
            let win_v = unchecked_input_window(*in_v_ptr);
            let out_u = unchecked_output(*out_u_ptr);
            let out_v = unchecked_output(*out_v_ptr);
            *in_u_ptr = in_u_ptr.add(1);
            *in_v_ptr = in_v_ptr.add(1);
            *out_u_ptr = out_u_ptr.add(1);
            *out_v_ptr = out_v_ptr.add(1);
            (win_u, win_v, out_u, out_v)
        };

    // Set up iteration state
    let mut in_u_ptr = start_u.as_ptr();
    let mut in_v_ptr = start_v.as_ptr();
    let mut out_u_ptr = end_u_center.as_mut_ptr();
    let mut out_v_ptr = end_v_center.as_mut_ptr();
    //
    // End of the current row processed by out_v_ptr
    let mut out_v_row_end = unsafe { out_v_ptr.add(out_cols) };
    //
    // End of the last row of the output grid
    let out_v_end = unsafe { out_v_row_end.add(out_rows.saturating_sub(1) * row_stride) };

    // Emit output iterator
    std::iter::from_fn(move || {
        // Common case : we are within the bounds of a row and advance normally
        if out_v_ptr < out_v_row_end {
            return Some(emit_and_increment(
                &mut in_u_ptr,
                &mut in_v_ptr,
                &mut out_u_ptr,
                &mut out_v_ptr,
            ));
        }

        // Otherwise, check if we reached the end of iteration
        if out_v_ptr == out_v_end {
            return None;
        }

        // We're at the end of a row, but not at the end of iteration:
        // switch to the next row then emit the next element as usual
        debug_assert_eq!(out_v_ptr, out_v_row_end);
        unsafe {
            in_u_ptr = in_u_ptr.add(next_row_step);
            in_v_ptr = in_v_ptr.add(next_row_step);
            out_u_ptr = out_u_ptr.add(next_row_step);
            out_v_ptr = out_v_ptr.add(next_row_step);
            out_v_row_end = out_v_ptr.add(out_cols);
        }
        Some(emit_and_increment(
            &mut in_u_ptr,
            &mut in_v_ptr,
            &mut out_u_ptr,
            &mut out_v_ptr,
        ))
    })
}

fn main() {
    // This is just a placeholder main function to make the code compile.
    // The actual usage of `stencil_iter` would be in a larger context where
    // the input and output arrays are defined and passed to this function.
}