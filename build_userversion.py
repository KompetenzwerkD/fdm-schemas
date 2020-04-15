import toml

FILE = "project_metadata_schema.toml"
OUT_FILE = "project_metadata_schema_userversion.txt"


HEADER = """
#Project metadata
#
#Schema verson: {version}
#Schema file: {schema}
#

"""

FOOTER = """

----------------------------
Anmerkungen:
Bitte Freitext stets in Englisch ausfüllen, außer es ist explizit anders angegeben.
Falls Sie ein Attribut mehrfach ausfüllen wollen, kopieren Sie einfach den entsprechenden Block und fügen Sie ihn erneut ins Dokument ein.
Bei Fragen wenden Sie sich gerne jederzeit an das KompetenzWerkD, z.B. per Mail: kompetenzwerkd@saw-leipzig.de

Für Datumsangaben empfehlen wir stets den Standard ISO 8601.
Eine Einführung bietet beispielsweise Wikipedia: https://de.wikipedia.org/wiki/ISO_8601
Mögliche Schemata, die Sie verwenden können, sind zum Beispiel:
YYYY-MM-DD
YYYY-MM
YYYY
oder für Zeitspannen:
YYYY-MM-DD/YYYY-MM-DD
YYYY-MM/YYYY-MM
YYYY/YYYY
"""

OCCURRENCE = {
    "1/1": "exaclty once",
    "0/1": "once",
    "0/n": "any number of times",
    "1/n": "at least once"
}


def read_schema(filepath):
    """
    Read schema toml file
    """
    with open(FILE) as f:
        schema = toml.load(f)

    return schema

def build_userversion(schema):
    """
    Parse schema and write userversion to file
    """

    with open(OUT_FILE, "w") as f:
        f.write(HEADER.format(
            version=schema["Metadata"]["Version"],
            schema=FILE
        ))

        for section, properties in schema.items():

            #skip metadata block
            if section == "Metadata":
                continue

            
            f.write("#{} \n\n".format(section))

            for prop in properties.values():

                f.write("{}=\"\"\n".format(prop["Label"]))
                f.write("Definition: {}\n".format(prop["Definition"]))

                f.write("Obligation: {}, {}\n\n".format(
                    prop["Obligation"], OCCURRENCE[prop["Occurrence"]]
                ))
        
        f.write(FOOTER)

if __name__ == "__main__":

    schema = read_schema(FILE)
    build_userversion(schema)