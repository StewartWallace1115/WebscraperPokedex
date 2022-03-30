CREATE TABLE Pokemon (	name varchar,
	id int,
	height varchar,
	weight int,
	ability varchar,
	species varchar,
	primary_type varchar,
	secondary_type varchar,
	official_artwork varchar
);
ALTER TABLE Pokemon ADD PRIMARY KEY (name);
CREATE TABLE Stats (	name varchar,
	hp int,
	attack int,
	defense int,
	special-attack int,
	special-defense int,
	speed int
);
ALTER TABLE Stats ADD PRIMARY KEY (name);
INSERT INTO Pokemon VALUES ('bulbasaur', 1, 7, 69, 'overgrow', 'Seed Pok�mon', 'grass', 'poison', 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/1.png');
INSERT INTO Stats VALUES ('bulbasaur', 45, 49, 49, 65, 65, 45);
