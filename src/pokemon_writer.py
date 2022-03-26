"""
Downloads file from Poke API
"""

class PokemonWriter:
    """
    Downloads JSON file from Poke API endpoint
    """

    @classmethod
    def convert_pokemon_json_to_sql(cls, pokemon_json):
        """
        Create SQL file from pokemon data
        """

        pokemon_columns = [("pokemon_name", "varchar"),("id", "int"),  ("height", "varchar"),\
                        ("weight", "int"),("ability", "varchar"),("species", "varchar"),\
                        ("stats", "varchar"),("primary_type", "varchar"),\
                        ("secondary_type", "varchar")]
        table_name = "Pokemon"
        primary_key = "pokemon_name"
        sql_pokemon_creation = cls.create_table(table_name, pokemon_columns)
        sql_pokemon_creation = cls.create_primary_key(primary_key,table_name,sql_pokemon_creation)
        sql_pokemon_creation = cls.populate_table(pokemon_json, table_name, sql_pokemon_creation)
        return sql_pokemon_creation

    @classmethod
    def create_table(cls, table_name, columns):
        """
        Create SQL table using table and columns
        """

        column_name = 0
        column_datatype = 1
        sql_creation = "CREATE TABLE " + table_name + " ("

        for column in columns:
            sql_creation = sql_creation + "\t" + column[column_name] + \
            " " + column[column_datatype] + ",\n"

        sql_creation = cls.remove_last_comma(sql_creation, False)

        sql_creation = sql_creation + ");\n"

        return sql_creation

    @classmethod
    def create_primary_keys(cls,keys_tables, sql_creation_string):
        """
        Create set of SQL primary keys using Alter table method.
        """

        for key_table in keys_tables:
            sql_creation_string = sql_creation_string + "ALTER TABLE " + key_table[0] +\
                             " ADD PRIMARY KEY (" + key_table[1] + ");\n"

        return sql_creation_string

    @classmethod
    def create_primary_key(cls, primary_key, table_name, sql_creation_string):
        """
        Create single primary key
        """

        sql_creation_string = sql_creation_string + "ALTER TABLE " + table_name + \
                             " ADD PRIMARY KEY (" + primary_key + ");\n"

        return sql_creation_string

    @classmethod
    def create_relationships(cls, keys_tables, sql_creation_string):
        """
        Create SQL relationships using alter table method.
        """

        for key_table in keys_tables:
            sql_creation_string = sql_creation_string + "ALTER TABLE " + key_table[0] + \
            " ADD FOREIGN KEY (" +key_table[1] + ") REFERENCES " + key_table[2] + \
            " (" +key_table[3] + ");\n"

        return sql_creation_string

    @classmethod
    def populate_table(cls, pokemon_json, table_name, sql_creation_string):
        """
        Populate SQL table using values only
        """

        value_string = "("
        value_index = 1

        for element in pokemon_json.items():
            value = element[value_index]

            if not isinstance(value, str):
                value = str(value)

            value = value.strip()
            value_string = value_string + value +", "

        value_string = cls.remove_last_comma(value_string, True)

        value_string = value_string + ");"
        sql_creation_string = sql_creation_string + "INSERT INTO "+ table_name +\
                             " VALUES " + value_string

        return sql_creation_string

    @classmethod
    def remove_last_comma(cls, sql_creation, with_extra_space):
        """
        Remove the last comma in a string with or without spaces around comma.
        """

        only_comma = 1
        comma_and_space = 2
        amount_characters_skipped = only_comma

        if with_extra_space:
            amount_characters_skipped = comma_and_space

        last_comma_index = sql_creation.rfind(',')
        beginning_substring = sql_creation[0 : last_comma_index : ]
        ending_substring = sql_creation[last_comma_index + amount_characters_skipped : :]
        sql_creation = beginning_substring + ending_substring

        return sql_creation
