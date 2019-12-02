use std::cmp;

fn main() {
    //println!("Karatsuba Multiple Problem set 1: ",
    //km(3141592653589793238462643383279502884197169399375105820974944592, 2718281828459045235360287471352662497757247093699959574966967627))

    println!("{}", km(343, 291));
    println!("{}", km(543, 2999));
    println!("{}", km(4879, 5647);
}

fn km(a:usize, b:usize) -> usize {
    if a < 10 || b < 10 {
        let o :usize = a*b;
        return o
    }

    let m = cmp::min(base_10size(a), base_10size(b));
    let m2 = (m/2);

    let (a1, a0) = split_at(a, m2);
    let (b1, b0) = split_at(b, m2);

    let z0 = km(a0, b0);
    let z1 = km(a0 + a1, b0 + b1);
    let z2 = km(a1, b1);

    let b_10: usize = 10;
    return (z2 * b_10.pow((m2*2) as u32)) +
        ((z1 - z2 - z0) * (b_10.pow(m2 as u32))) +
            z0

}

fn base_10size(n:usize) -> usize {
    let mut o = n as f64;
    o  = o.log10();
    o = o.floor();
    o = o + 1.0;

    return o as usize
}

fn split_at(n:usize, b:usize) -> (usize, usize) {
    let n1 = (n/(10.pow(b)) as usize;
    let n0 = n - (n1*(10.pow(b));

    return (n1, n0)
}