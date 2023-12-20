fn encrypt(bytes: &Vec<u8>) -> Vec<u8> {
    let mut encrypted: Vec<u8> = vec![];
    for (i, byte) in bytes.iter().enumerate() {
        match i % 5 {
            0 => {
                encrypted.push(!(*byte).rotate_left(6u32.wrapping_mul(i as u32)));
            },
            1 => {
                encrypted.push(*byte ^ i.pow(4) as u8);
            },
            2 => {
                encrypted.push((*byte).wrapping_add((5u8.wrapping_mul(i as u8)) + 3));
            },
            3 => {
                encrypted.push((*byte).rotate_right(12usize.wrapping_sub(i) as u32));
            },
            4 => {
                encrypted.push((((*byte >> 0) & 1) << 3) | (((*byte >> 1) & 1) << 0) | (((*byte >> 2) & 1) << 7) | (((*byte >> 3) & 1) << 2) |
                               (((*byte >> 4) & 1) << 6) | (((*byte >> 5) & 1) << 1) | (((*byte >> 6) & 1) << 5) | (((*byte >> 7) & 1) << 4));
            },
            _ => unreachable!()
        }
    }

    for i in 0..encrypted.len() {
        let j = (i * 17 + 23) % encrypted.len();
        if i != j {
            encrypted.swap(i, j);
        }
    }

    encrypted
}

fn decrypt(bytes: &Vec<u8>) -> Vec<u8> {
    let mut encrypted = bytes.clone();
    for i in (0..encrypted.len()).rev() {
        let j = (i * 17 + 23) % encrypted.len();
        if i != j {
            encrypted.swap(i, j);
        }
    }

    let mut decrypted: Vec<u8> = vec![];
    for (i, byte) in encrypted.iter().enumerate() {
        match i % 5 {
            0 => {
                decrypted.push(!(*byte).rotate_right(6u32.wrapping_mul(i as u32)));
            },
            1 => {
                decrypted.push(*byte ^ i.pow(4) as u8);
            },
            2 => {
                decrypted.push((*byte).wrapping_sub((5u8.wrapping_mul(i as u8)) + 3));
            },
            3 => {
                decrypted.push((*byte).rotate_left(12usize.wrapping_sub(i) as u32));
            },
            4 => {
                decrypted.push((((*byte >> 3) & 1) << 0) | (((*byte >> 0) & 1) << 1) | (((*byte >> 7) & 1) << 2) | (((*byte >> 2) & 1) << 3) |
                               (((*byte >> 6) & 1) << 4) | (((*byte >> 1) & 1) << 5) | (((*byte >> 5) & 1) << 6) | (((*byte >> 4) & 1) << 7));
            },
            _ => unreachable!()
        }
    }

    decrypted
}

fn main() {
    let arg: Vec<String> = std::env::args().collect();
    if let Some(text) = arg.get(1) {
        let bytes = text.as_bytes().to_vec();
        let encoded = encrypt(&bytes);
        debug_assert_eq!(bytes, decrypt(&encoded));

        println!("{} -> {}", text, hex::encode(encoded));
    }
    else {
        println!("The first argument should be the plaintext that you want to encrypt!");
    }
}
