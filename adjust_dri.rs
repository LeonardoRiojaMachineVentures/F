enum Amount {
	Microgram(usize),
	Milligram(usize),
	Gram(usize),
	Kilogram(f64),
}

struct NutrientAmount {
	calcium : Amount,
	vitamin_a : Amount,
	vitamin_b : Amount,
	vitamin_c : Amount,
}

enum Gender {
	Male,
	Female,
}

enum Group {
	Baby,
	Toddler,
	Child,
	EarlyTeen,
	MidTeen,
	LateTeen,
	EarlyTwenties,
	MidTwenties,
	LateTwenties,
	Thirties,
	Fourties,
	Fifthies,
	Elderly,
}

struct Alpha {
	
}
struct Mass {
	muscle : Amount::Kilogram,
	bone : Amount::Kilogram,
	fat : Amount::Kilogram,
	cartilage : Amount::Kilogram,
	organs : Amount::Kilogram,
}

struct PopStatistics {
	male_early_twenties : Vec<Data>,
	female_early_twenties : Vec<Data>,
}

struct Data {
	mass : Mass,
	sufficient_amount : NutrientAmount,
}

struct PMeasurement {
	gender : Gender,
	group : Group,
	data : Data,
}
impl PopStatistics {
	fn get_stats(x : Vec<PMeasurement>) -> PopStatistics {
		male_early_twenties = vec![];
		female_early_twenties = vec![];
		for i in x {
			match (i.gender, i.group) {
				(Gender::Male, Group::EarlyTwenties) => {
					male_early_twenties.push(i.data);
				},
				(Gender::Female, Group::EarlyTwenties) => {
					female_early_twenties.push(i.data);
				},
				_ => {},
			}
		}
		PopStatistics {
			male_early_twenties,
			female_early_twenties,
		}
	}
}

fn main() {
	let p : Vec<PMeasurement> = vec![];
	let s = PMeasurement::get_stats(p);
	
	
}