// #![feature(f128)]
use std::collections::HashSet;

fn mod_1(x: f64) -> f64 {
    x - x.floor()
}

fn repeat(x: f64) -> f64 {
    let a = x; 
    let mut i = 1.0; 
    let mut seen = HashSet::new();

    let mut t = mod_1(a * i);
    
    while !seen.contains(&t.to_string()) {
        seen.insert(t.to_string()); 
        i += 1.0;
        t = mod_1(a * i);
    }
    i
}

fn main() {
    let x = 3.1415926535897;
    println!("{:?}", mod_1(x));
    println!("{:?}", repeat(x));

}
