import unittest
import json
from src.pokemon_writer import PokemonWriter

Parsed_pokemon_data ="""{ "id ": 35,  "name ":  "clefairy ",  "height ": 6,  "weight ": 75,  "species ":  "Fairy Pokémon ",  "ability ":  "friend-guard ",  "primary_type ":  "fairy ",  "secondary_type ":  "none "}"""
 

class Pokemon_Downloader_Test(unittest.TestCase):
    
    
    def test_create_tables(self):
        pokemon_writer = PokemonWriter()

        columns = [("pokemon_name", "varchar"),("id", "int"),  ("height", "varchar"),("weight", "int"),("ability", "varchar"),\
                  ("species", "varchar"),("stats", "varchar"),("primary_type", "varchar"),("secondary_type", "varchar")]
        pokemon_sql = pokemon_writer.create_table("Pokemon", columns)

        expected_result = "CREATE TABLE Pokemon (\tpokemon_name varchar,\n\tid int,\n\theight varchar,\n\tweight int,\n\tability varchar,\n\tspecies varchar,\n\tstats varchar,\n\tprimary_type varchar,\n\tsecondary_type varchar\n);\n"
        self.assertEquals(expected_result, pokemon_sql)
    
    def test_create_primary_keys(self):
        pokemon_writer = PokemonWriter()
        primary_keys = [("Pokemon","pokemon_name"),("Moves", "name")]
        pokemon_sql = pokemon_writer.create_primary_keys(primary_keys,"")

        expected_result = "ALTER TABLE Pokemon ADD PRIMARY KEY (pokemon_name);\nALTER TABLE Moves ADD PRIMARY KEY (name);\n"
        self.assertEquals(expected_result, pokemon_sql)
    
    def test_create_primary_key(self):
        pokemon_writer = PokemonWriter()
        pokemon_sql = pokemon_writer.create_primary_key("pokemon_name", "Pokemon","")

        expected_result = "ALTER TABLE Pokemon ADD PRIMARY KEY (pokemon_name);\n"
        self.assertEquals(expected_result, pokemon_sql)

    def test_create_relationships(self):
        pokemon_writer = PokemonWriter()
        primary_keys = [("Moves", "pokemon_name","Pokemon","pokemon_name"),("Moves", "name","Types", "name")]
        pokemon_sql = pokemon_writer.create_relationships(primary_keys,"")

        expected_result = "ALTER TABLE Moves ADD FOREIGN KEY (pokemon_name) REFERENCES Pokemon (pokemon_name);\nALTER TABLE Moves ADD FOREIGN KEY (name) REFERENCES Types (name);\n"

        self.assertEquals(expected_result, pokemon_sql)

    def test_populate_table(self):
        pokemon_writer = PokemonWriter()
        pokemon_data_json = json.loads(Parsed_pokemon_data)

        pokemon_sql = pokemon_writer.populate_table(pokemon_data_json,"Pokemon","")

        expected_result = "INSERT INTO Pokemon VALUES (35, clefairy, 6, 75, Fairy Pokémon, friend-guard, fairy, none);"

        self.assertEquals(expected_result, pokemon_sql)
    
    def test_convert_pokemon_json_to_sql(self):
        pokemon_writer = PokemonWriter()
        pokemon_data_json = json.loads(Parsed_pokemon_data)

        pokemon_sql = pokemon_writer.convert_pokemon_json_to_sql(pokemon_data_json)
        expected_creation = "CREATE TABLE Pokemon (\tpokemon_name varchar,\n\tid int,\n\theight varchar,\n\tweight int,\n\tability varchar,\n\tspecies varchar,\n\tstats varchar,\n\tprimary_type varchar,\n\tsecondary_type varchar\n);\n"
        expected_alter = "ALTER TABLE Pokemon ADD PRIMARY KEY (pokemon_name);\n"
        expected_populate = "INSERT INTO Pokemon VALUES (35, clefairy, 6, 75, Fairy Pokémon, friend-guard, fairy, none);"

        expected_result =expected_creation + expected_alter + expected_populate

        self.assertEquals(expected_result, pokemon_sql)
     