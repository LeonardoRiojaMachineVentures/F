use std::fs;
use std::io::prelude::*;
use std::net::TcpListener;
use std::net::TcpStream;


enum AgeGroup {
	SmallChild,
	MediumChild,
	EarlyTeen,
	MidTeen,
	Twenties,
	ThirtiesOrFourties,
	FiftiesOrSixties,
	BeyondSeventies,
}

impl AgeGroup {
	fn new(x : u8) -> Result<AgeGroup, ()> {
		use crate::AgeGroup::*;
		match x {
		v if v < 1 => Err(()),
		v if v <= 3 => Ok(SmallChild),
		v if v <= 8 => Ok(MediumChild),
		v if v <= 13 => Ok(EarlyTeen),
		v if v <= 18 => Ok(MidTeen),
		v if v <= 30 => Ok(Twenties),
		v if v <= 50 => Ok(ThirtiesOrFourties),
		v if v <= 70 => Ok(FiftiesOrSixties),
		v if v <= 150 => Ok(BeyondSeventies),
		_ => Err(()),
		}
	}
}
enum Gender {
	Male,
	Female,
}
impl Gender {
	fn new(x : &str) -> Result<Gender, ()> {
		match x.to_lowercase().as_str() {
			use crate::Gender::*;
			"male" => Ok(Male)
			"female" => Ok(Female)
			_ => Err(())
		}
	}
}

struct User {
	gender : Gender,
	age : u8,
	weight : f64,
	coefficient : f64,
	age_group : AgeGroup,
}

impl User {
	fn new(x : &str) -> Result<User, ()> {
		let v = x.split_whitespace();
		let age = match v.next() {
			None => return Err(()),
			Some(v) => v,
		};
		let gender = match v.next() {
			None => return Err(()),
			Some(v) => v,
		};
		let weight = match v.next() {
			None => return Err(()),
			Some(v) => v,
		};
		let age = age.parse::<u8>() {
			Ok(v) => v,
			Err(()) => return Err(()),
		};
		let gender = Gender::new(gender)?;
		let weight = match weight.parse::<f64>() {
			Ok(v) => {
				match v.is_normal() {
					true => v,
					false => return Err(()),
				},
			},
			Err(()) => return Err(()),
		};
		/*
		let age = AgeGroup::new(v.next()?)?;
		let gender = Gender::new(v.next()?)?;
		let weight = v.next()?.parse::<f64>()?;
		if !weight.is_normal() return Err(());
		*/
		let mut aux = User {
			age,
			gender,
			weight,
			coefficient: 0f64,
			age_group,
		};
		
		aux.calculate_coefficient();
		Ok(aux)
		
	}
	fn calculate_coefficient(&self) -> () {
		let (average, sd) = match self.gender {
			Gender::Male => {
				male_average_weight_and_sd(age as f64)
			},
			Gender::Female => {
				female_average_weight_and_sd(age as f64)
			},
		};
		self.coefficient = (self.weight)/(average + 2*sd);
	}
}



//FEMALE
fn female_average_weight_and_sd(age : f64) -> (f64, f64) {
	match age {
v if v >= 3f64 && v < 3.5f64 => (14.9f64, 1.70f64),
v if v >= 3.5f64 && v < 4f64 => (15.7f64, 2.65f64),
v if v >= 4f64 && v < 4.5f64 => (17.0f64, 2.85f64),
v if v >= 4.5f64 && v < 5f64 => (18.1f64, 2.61f64),
v if v >= 5.0f64 && v < 5.5f64 => (19.1f64, 3.38f64),
v if v >= 5.5f64 && v < 6.0f64 => (20.5f64, 4.23f64),
v if v >= 6.0f64 && v < 6.5f64 => (22.7f64, 4.41f64),
v if v >= 6.5f64 && v < 7.0f64 => (24.3f64, 5.17f64),
v if v >= 7.0f64 && v < 7.5f64 => (25.5f64, 5.67f64),
v if v >= 7.5f64 && v < 8.0f64 => (27.3f64, 6.19f64),
v if v >= 8.0f64 && v < 8.5f64 => (28.2f64, 6.86f64),
v if v >= 8.5f64 && v < 9.0f64 => (32.0f64, 7.74f64),
v if v >= 9.0f64 && v < 9.5f64 => (33.3f64, 8.17f64),
v if v >= 9.5f64 && v < 10.0f64 => (35.7f64, 8.85f64),
v if v >= 10.0f64 && v < 10.5f64 => (37.0f64, 9.92f64),
v if v >= 10.5f64 && v < 11.0f64 => (39.8f64, 9.87f64),
v if v >= 11.0f64 && v < 11.5f64 => (43.9f64, 11.11f64),
v if v >= 11.5f64 && v < 12.0f64 => (45.6f64, 12.28f64),
v if v >= 12.0f64 && v < 12.5f64 => (48.1f64, 11.23f64),
v if v >= 12.5f64 && v < 13.0f64 => (51.2f64, 14.07f64),
v if v >= 13.0f64 && v < 13.5f64 => (53.2f64, 11.98f64),
v if v >= 13.5f64 && v < 14.0f64 => (54.1f64, 12.10f64),
v if v >= 14.0f64 && v < 14.5f64 => (55.0f64, 12.14f64),
v if v >= 15.0f64 && v < 15.0f64 => (56.4f64, 11.27f64),
v if v >= 15.5f64 && v < 16.0f64 => (58.1f64, 9.87f64),
v if v >= 16.0f64 && v < 16.5f64 => (56.8f64, 9.89f64),
v if v >= 16.5f64 && v < 17.0f64 => (57.8f64, 10.44f64),
v if v >= 17.0f64 && v < 17.5f64 => (56.5f64, 9.45f64),
v if v >= 17.5f64 && v < 18.0f64 => (58.8f64, 9.48f64),
v if v >= 18.0f64 && v < 18.5f64 => (57.6f64, 8.94f64),
v if v >= 18.5f64 && v < 19.0f64 => (57.3f64, 9.74f64),
v if v >= 19.0f64 && v < 19.5f64 => (57.4f64, 7.99f64),
v if v >= 19.5f64 && v < 20.0f64 => (59.9f64, 10.41f64),
v if v >= 20.0f64 && v < 20.5f64 => (57.0f64, 8.84f64),
v if v >= 20.5f64 && v < 21.0f64 => (58.5f64, 9.08f64),
v if v >= 21.0f64 && v < 21.5f64 => (57.2f64, 7.93f64),
v if v >= 21.5f64 && v < 22.0f64 => (58.6f64, 7.78f64),
v if v >= 22.0f64 && v < 22.5f64 => (57.0f64, 7.48f64),
v if v >= 22.5f64 && v < 23.0f64 => (59.7f64, 11.76f64),
v if v >= 23.0f64 && v < 23.5f64 => (57.9f64, 8.89f64),
	}
}

//FEMALE
fn male_average_weight_and_sd(age : f64) -> (f64, f64) {
	match age {
v if v >= 3f64 && v < 3.5f64 => (15.7f64, 3.78f64),
v if v >= 3.5f64 && v < 4f64 => (16.1f64, 2.36f64),
v if v >= 4f64 && v < 4.5f64 => (17.3f64, 2.59f64),
v if v >= 4.5f64 && v < 5f64 => (18.3f64, 3.11f64),
v if v >= 5.0f64 && v < 5.5f64 => (19.6f64, 3.26f64),
v if v >= 5.5f64 && v < 6.0f64 => (21.2f64, 4.03f64),
v if v >= 6.0f64 && v < 6.5f64 => (22.8f64, 4.04f64),
v if v >= 6.5f64 && v < 7.0f64 => (25.1f64, 4.88f64),
v if v >= 7.0f64 && v < 7.5f64 => (25.7f64, 6.28f64),
v if v >= 7.5f64 && v < 8.0f64 => (27.6f64, 6.53f64),
v if v >= 8.0f64 && v < 8.5f64 => (28.8f64, 5.48f64),
v if v >= 8.5f64 && v < 9.0f64 => (33.0f64, 9.16f64),
v if v >= 9.0f64 && v < 9.5f64 => (33.8f64, 8.54f64),
v if v >= 9.5f64 && v < 10.0f64 => (35.6f64, 8.54f64),
v if v >= 10.0f64 && v < 10.5f64 => (37.9f64, 9.60f64),
v if v >= 10.5f64 && v < 11.0f64 => (39.8f64, 11.79f64),
v if v >= 11.0f64 && v < 11.5f64 => (43.4f64, 12.44f64),
v if v >= 11.5f64 && v < 12.0f64 => (43.3f64, 11.63f64),
v if v >= 12.0f64 && v < 12.5f64 => (47.4f64, 11.78f64),
v if v >= 12.5f64 && v < 13.0f64 => (51.3f64, 14.31f64),
v if v >= 13.0f64 && v < 13.5f64 => (51.1f64, 12.13f64),
v if v >= 13.5f64 && v < 14.0f64 => (54.2f64, 12.50f64),
v if v >= 14.0f64 && v < 14.5f64 => (58.0f64, 13.64f64),
v if v >= 15.0f64 && v < 15.0f64 => (60.1f64, 12.82f64),
v if v >= 15.5f64 && v < 16.0f64 => (67.1f64, 13.61f64),
v if v >= 16.0f64 && v < 16.5f64 => (66.2f64, 13.16f64),
v if v >= 16.5f64 && v < 17.0f64 => (67.5f64, 13.86f64),
v if v >= 17.0f64 && v < 17.5f64 => (67.8f64, 13.37f64),
v if v >= 17.5f64 && v < 18.0f64 => (70.1f64, 12.95f64),
v if v >= 18.0f64 && v < 18.5f64 => (70.5f64, 12.71f64),
v if v >= 18.5f64 && v < 19.0f64 => (70.5f64, 14.20f64),
v if v >= 19.0f64 && v < 19.5f64 => (70.9f64, 14.51f64),
v if v >= 19.5f64 && v < 20.0f64 => (74.3f64, 14.25f64),
v if v >= 20.0f64 && v < 20.5f64 => (73.2f64, 11.10f64),
v if v >= 20.5f64 && v < 21.0f64 => (73.1f64, 10.46f64),
v if v >= 21.0f64 && v < 21.5f64 => (71.9f64, 10.61f64),
v if v >= 21.5f64 && v < 22.0f64 => (71.9f64, 10.61f64),
v if v >= 22.0f64 && v < 22.5f64 => (57.0f64, 10.93f64),
v if v >= 22.5f64 && v < 23.0f64 => (59.7f64, 11.76f64),
v if v >= 23.0f64 && v < 23.5f64 => (57.9f64, 8.89f64),
	}
}



/*
struct Nutrients {
	vitamin_a : Need,
	vitamin_c : Need,
	vitamin_d : Need,
	vitamin_e : Need,
	vitamin_k : Need,
	thiamin : Need,
	riboflavin : Need,
	niacin : Need,
	vitamin_b6 : Need,
	folate : Need,
	vitamin_b12 : Need,
	pantothenic_acid : Need,
	biotin : Need,
	choline : Need,
	
	calcium : Need,
	chromium : Need,
	copper : Need,
	fluoride : Need,
	iodine : Need,
	iron : Need,
	magnesium : Need,
	manganese : Need,
	molybdenum : Need,
	phosphorus : Need,
	selenium : Need,
	zinc : Need,
	potassium : Need,
	sodium : Need,
	chloride : Need,
}

enum Need {
	RDA(Amount),
	AI(Amount),
}
impl Need {
	fn repr(&self) -> String {
		let (k, u, a) = match self {
			RDA(x) => match x {
				Gram(v) => ("bold", "g", v),
				Milligram(v) => ("bold", "mg", v),
				Microgram(v) => ("bold", "ug", v),
				Nanogram(v) => ("bold", "ng", v),
			},
			AI(x) => match(x) {
				Gram(v) => ("*", "g", v),
				Milligram(v) => ("*", "mg", v),
				Microgram(v) => ("*", "ug", v),
				Nanogram(v) => ("*", "ng", v),	
			},
		};
		println!("{} {} {}", k, a, u);
	}
	fn from_str(x : &str) -> Need {
		let x = x.trim().to_lowercase().split_whitespace();
		let a = x.next().unwrap();
		let b = x.next().unwrap().parse::<u16>().unwrap();
		let c = x.next().unwrap();
		match a {
			"rda" => {
				RDA(Amount::new(c, b)),
			},
			"ai" => {
				AI(Amount::new(c, b)),
			},
			_ => {panic!();},
		}
	}
}
enum Amount {
	Gram(u16),
	Milligram(u16),
	Microgram(u16),
	Nanogram(u16),
}
impl Amount {
	fn new(c : &str, b : u16) -> Amount {
		match c {
			"g" => Gram(b),
			"mg" => Milligram(b),
			"ug" => Microgram(b),
			"ng" => Nanogram(b),
			_ => {panic!();},
		}
	}
}

macro_rules! n {
	(RDA g $e:expr) => (Need::RDA(Amount::Gram($e)));
	(RDA mg $e:expr) => (Need::RDA(Amount::Milligram($e)));
	(RDA ug $e:expr) => (Need::RDA(Amount::Microgram($e)));
	(RDA ng $e:expr) => (Need::RDA(Amount::Nanogram($e)));
	
	(AI g $e:expr) => (Need::AI(Amount::Gram($e)));
	(AI mg $e:expr) => (Need::RDA(Amount::Milligram($e)));
	(AI ug $e:expr) => (Need::RDA(Amount::Microgram($e)));
	(AI ng $e:expr) => (Need::RDA(Amount::Nanogram($e)));
	
}
*/

/*
const SMALL_CHILD : Nutrients = Nutrients {
	use crate::Need::*;
	vitamin_a : n!(RDA ug 300),
	vitamin_c : n!(RDA mg 15),
	vitamin_d : n!(RDA ug 15),
	vitamin_e : n!(RDA mg 6),
	vitamin_k : n!(AI ug 30),
	thiamin : n!(RDA ug 500),
	riboflavin : n!(RDA ug 500),
	niacin : n!(RDA mg 6),
	vitamin_b6 : n!(RDA ug 500),
	folate : n!(RDA ug 150),
	vitamin_b12 : n!(AI ng 900),
	pantothenic_acid : n!(AI mg 2),
	biotin : n!(AI ug 8),
	choline : n!(AI mg 200),
	
	calcium : n!(RDA mg 700),
	chromium : n!(AI ug 11),
	copper : n!(RDA ug 340),
	fluoride : n!(AI ug 700),
	iodine : n!(RDA ug 90),
	iron : n!(RDA mg 7),
	magnesium : n!(RDA mg 80),
	manganese : n!(AI ug 1200),
	molybdenum : n!(RDA ug 17),
	phosphorus : n!(RDA mg 460),
	selenium : n!(RDA ug 20),
	zinc : n!(RDA mg 3),
	potassium : n!(AI mg 2000),
	sodium : n!(AI mg 800),
	chloride : n!(AI mg 1500),
};
*/
/*
const MEDIUM_CHILD : Nutrients = Nutrients {
	use crate::Need::*;
	vitamin_a : n!(RDA ug 400),
	vitamin_c : n!(RDA mg 25),
	vitamin_d : n!(RDA ug 15),
	vitamin_e : n!(RDA mg 7),
	vitamin_k : n!(AI ug 55),
	thiamin : n!(RDA ug 600),
	riboflavin : n!(RDA ug 600),
	niacin : n!(RDA mg 8),
	vitamin_b6 : n!(RDA ug 600),
	folate : n!(RDA ug 200),
	vitamin_b12 : n!(AI ng 1200),
	pantothenic_acid : n!(AI mg 3),
	biotin : n!(AI ug 12),
	choline : n!(AI mg 250),
	
	calcium : n!(RDA mg 1000),
	chromium : n!(AI ug 15),
	copper : n!(RDA ug 440),
	fluoride : n!(AI mg 1),
	iodine : n!(RDA ug 90),
	iron : n!(RDA mg 10),
	magnesium : n!(RDA mg 130),
	manganese : n!(AI ug 1500),
	molybdenum : n!(RDA ug 22),
	phosphorus : n!(RDA mg 500),
	selenium : n!(RDA ug 30),
	zinc : n!(RDA mg 5),
	potassium : n!(AI mg 2300),
	sodium : n!(AI mg 1000),
	chloride : n!(AI mg 1900),
};
*/
/*
const EARLY_TEEN : Nutrients = Nutrients {
	use crate::Need::*;
	vitamin_a : n!(RDA ug 600),
	vitamin_c : n!(RDA mg 45),
	vitamin_d : n!(RDA ug 15),
	vitamin_e : n!(RDA mg 11),
	vitamin_k : n!(AI ug 60),
	thiamin : n!(RDA ug 900),
	riboflavin : n!(RDA ug 900),
	niacin : n!(RDA mg 12),
	vitamin_b6 : n!(RDA ug 600),
	folate : n!(RDA ug 200),
	vitamin_b12 : n!(AI ng 1200),
	pantothenic_acid : n!(AI mg 3),
	biotin : n!(AI ug 12),
	choline : n!(AI mg 250),
	
	calcium : n!(RDA mg 1000),
	chromium : n!(AI ug 15),
	copper : n!(RDA ug 440),
	fluoride : n!(AI mg 1),
	iodine : n!(RDA ug 90),
	iron : n!(RDA mg 10),
	magnesium : n!(RDA mg 130),
	manganese : n!(AI ug 1500),
	molybdenum : n!(RDA ug 22),
	phosphorus : n!(RDA mg 500),
	selenium : n!(RDA ug 30),
	zinc : n!(RDA mg 5),
	potassium : n!(AI mg 2300),
	sodium : n!(AI mg 1000),
	chloride : n!(AI mg 1900),
};
*/


fn main() {
	let u = User::new("");
	println!("{}", u);
	/*
	let listener = TcpListener::bind("127.0.0.1:7878").unwrap();
	for stream in listener.incoming() {
		let stream = stream.unwrap();
		handle_connection(stream);
	}
	*/
}


/*
POST / HTTP/1.1\r\n
Host: foo.com\r\n
Content-Type: application/x-www-form-urlencoded\r\n
Content-Length: 13\r\n\r\n
say=Hi&to=Mom\r\n
\r\n
*/

/*
enum ErrorFromConnection {
	PageNotFound,
	MalformedStr,
}
fn handle_connection(mut stream: TcpStream) -> () {
	
	let mut buffer = [0u8; 1024];
	stream.read(&mut buffer).unwrap();
	let post = b"POST / HTTP/1.1\r\n";

	let (user, status_line, filename) = if buffer.starts_with(post) {
		(User::from_buffer(&buffer), "HTTP/1.1 200 OK", "exact_needs.html")
	} else {
		(Err(ErrorFromConnection::PageNotFound), "HTTP/1.1 404 NOT FOUND", "404.html")
	}
	match user

	
	let contents = fs::read_to_string(filename).unwrap();
	let response = format!("{}\r\nContent-Length: {}\r\n\r\n{}",
		status_line,
		contents.len(),
	contents);
	
	stream.write(response.as_bytes()).unwrap();
	stream.flush().unwrap();
}
*/