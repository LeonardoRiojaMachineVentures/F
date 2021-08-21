struct Measurement {
	non_fat_mass : f64,
	fat_mass : f64,
	sufficient : usize,
}
fn generate_range(min : f64, max : f64, step : f64) -> Vec<f64> {
	let mut ans : Vec<f64> = vec![];
	let mut i = min;
	while (i <= max) {
		ans.append(i);
		i += step;
	}
	return(ans)
}
struct Alpha {
	non_fat_coefficient : f64,
	fat_coefficient : f64,
}
impl Measurement {
	fn try(pop : Vec<Measurement>, alphas : Vec<Alpha>) ->  {
		let mut stats = vec![];
		for alpha in alphas {
			stats.push((alpha, alpha.try_alpha(pop)));
		}
		return(
	}
}
impl Alpha {
	fn try_alpha(&self, pop : &Vec<Measurement>) -> (Vec<Measurement>, Vec<Measurement>){
		above_or_equal = vec![];
		below = vec![];
		calculated_sa = vec![];
		for p in pop {
			calculated_sufficient = self.non_fat_coefficient*p.non_fat_mass + self.fat_coefficient*p.fat_mass;
			match calculated_sufficient.cmp(&p.sufficient) {
				Greater | Equal => {above_or_equal.push(p.copy());},
				_ => {below.push(p.copy());},
			}
		}
		return((above_or_equal, below));
	}
	fn new(non_fat_coefficient : f64, fat_coefficient : f64) -> Alpha {
		Alpha {
			non_fat_coefficient,
			fat_coefficient,
		}
	}
	fn generate_range(min_non_fat : f64, max_non_fat : f64, step_non_fat : f64, min_fat : f64, max_fat : f64, step_fat : f64) -> Vec<Alpha> {
		let v = generate_range(min_non_fat : f64, max_non_fat : f64, step_non_fat : f64);
		let u = generate_range(min_fat : f64, max_fat : f64, step_fat : f64);
		let ans = vec![];
		for i in v.iter().zip(&u.iter()) {
			ans.push(Alpha::new(i));
		}
		return(ans)
	}
}


fn main() {
	let pop : Vec<Measurement> = vec![];
	
}