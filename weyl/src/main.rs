use std::collections::HashMap;
use std::f64;

fn fractional_part(x: f64) -> f64 {
    x - x.floor()
}

fn to_binary_string(mut x: f64, bits: usize) -> String {
    let mut binary = String::new();
    for _ in 0..bits {
        x *= 2.0;
        if x >= 1.0 {
            binary.push('1');
            x -= 1.0;
        } else {
            binary.push('0');
        }
    }
    binary
}

fn find_repetition(binary: &str) -> Option<usize> {
    let mut seen = HashMap::new();
    for (i, window) in binary.chars().enumerate() {
        if let Some(&first_occurrence) = seen.get(&window) {
            return Some(i - first_occurrence);
        }
        seen.insert(window, i);
    }
    None
}

fn find_repetition_start(s: &str) -> Option<usize> {
    let chars: Vec<char> = s.chars().collect();
    let len = chars.len();
    for i in 1..=len / 2 {
        if len % i == 0 {
            let pattern = &chars[..i];
            if chars.chunks(i).all(|chunk| chunk == pattern) {
                return Some(i);
            }
        }
    }
    None
}


fn main() {
    let sqrt2 = 1.1; // sqrt(2)
    let k = 100000; 
    let bits = 16;
    let mut full_binary = String::new();

    for i in 1..=k {
        let value = sqrt2 * (i as f64);
        let frac_part = fractional_part(value);
        let binary_rep = to_binary_string(frac_part, bits);
        full_binary.push_str(&binary_rep);
    }
    // println!("{:?}", full_binary);
    match find_repetition_start(&full_binary) {
        Some(pos) => println!("String repeats after {} characters", pos),
        None => println!("No repetition found"),
    }

}
