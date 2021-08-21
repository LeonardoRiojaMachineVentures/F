fn make_matrix(a : f64) -> (f64, f64, f64, f64) {
	assert!(a > 0.0 && a < 1.0);
	(a, 0f64, 1f64 - a, 1f64)
}
#[derive(Debug, Copy, Clone)]
struct State {
	dumb : f64,
	smart : f64,
}

impl State {
	fn dumb_af() -> State {
		State {
			dumb : 1f64,
			smart : 0f64,
		}
	}
	fn evolve(&mut self, m : (f64, f64, f64, f64)) -> () {
		let d = self.dumb; //dont be dumb to forget this line
		self.dumb = m.0*d;
		self.smart = d + self.smart - m.0*d;
	}
	fn conservation(&self) -> f64 {
		self.dumb + self.smart
	}
}
fn main() {
	let m = make_matrix(0.999f64);
	let mut p = State::dumb_af();
	const N : usize = 10000usize;
	let mut evolution = [State::dumb_af(); N];
	let mut total = [0f64; N];
	let mut enlightment = [0f64; N];
	for i in 0..N {
		evolution[i] = p.clone();
		total[i] = p.conservation();
		p.evolve(m);
	}
	for e in evolution {
		println!("{:?}", e);
	}
	for t in total {
		println!("{:?}", t);	
	}
	enlightment[0] = evolution[0].smart;
	for i in 1..N {
		enlightment[i] = enlightment[i - 1] + (1f64 - m.0)*evolution[i - 1].dumb;
	}
	for e in enlightment {
		println!("{:?}", e);
	}
	println!("{:?}", enlightment[100]);
	println!("{:?}", enlightment[400]);

}
