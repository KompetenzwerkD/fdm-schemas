import toml
import argparse

FILE = "schemas/project_metadata_schema.toml"
OUT_FILE = "templates/project_metadata_schema_userversion.txt"


HEADER = """
# {title}
#
# Schema verson: {version}
# Schema file: {schema}
#

"""

FOOTER = """

# ----------------------------
# Anmerkungen:
# Bitte Freitext stets in Englisch ausfüllen, außer es ist explizit anders angegeben.
# Falls Sie ein Attribut mehrfach ausfüllen wollen, kopieren Sie einfach den entsprechenden Block und fügen Sie ihn erneut ins Dokument ein.
# Bei Fragen wenden Sie sich gerne jederzeit an das KompetenzWerkD, z.B. per Mail: kompetenzwerkd@saw-leipzig.de
#
# Für Datumsangaben empfehlen wir stets den Standard ISO 8601.
# Eine Einführung bietet beispielsweise Wikipedia: https://de.wikipedia.org/wiki/ISO_8601
# Mögliche Schemata, die Sie verwenden können, sind zum Beispiel:
# YYYY-MM-DD
# YYYY-MM
# YYYY
# oder für Zeitspannen:
# YYYY-MM-DD/YYYY-MM-DD
# YYYY-MM/YYYY-MM
# YYYY/YYYY
"""

OCCURRENCE = {
    "1/1": "exactly once",
    "0/1": "once",
    "0/n": "any number of times",
    "1/n": "at least once"
}


def read_schema(filepath):
    """
    Read schema toml file
    """
    with open(filepath) as f:
        schema = toml.load(f)

    return schema

def build_userversion(schema, out_file):
    """
    Parse schema and write userversion to file
    """

    with open(out_file, "w") as f:
        f.write(HEADER.format(
            title=schema["Metadata"]["Title"],
            version=schema["Metadata"]["Version"],
            schema=schema["Metadata"]["Location"]
        ))

        for section, properties in schema.items():

            #skip metadata block
            if section == "Metadata":
                continue

            
            f.write("# {} \n\n".format(section))

            for prop in properties.values():

                f.write("{}=\"\"\n".format(prop["Label"]))
                if "Qualifier" in prop:
                    for qualifier in prop["Qualifier"]:
                        f.write(qualifier + "=\"\"\n")
                f.write("# Definition: {}\n".format(prop["Definition"]))
                f.write("# Datatype: {}\n".format(prop["Datatype"]))
                f.write("# Obligation: {}, {}\n".format(
                    prop["Obligation"], OCCURRENCE[prop["Occurrence"]]
                ))
                if "Hint" in prop:
                    f.write(prop["Hint"]+"\n")
                else:
                    f.write("\n")
                
        
        f.write(FOOTER)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Build Template from metadata schema.')
    parser.add_argument('schema', metavar='S', type=str, nargs=1,
                    help='Schema file position')

    args = parser.parse_args()
    filepath = args.schema[0]

    out_file = "templates/{}.txt".format(
                    filepath.replace(".toml", "").replace("schemas/", ""))

    schema = read_schema(filepath)
    build_userversion(schema, out_file)