
Auf dieser Seite werden Schemas und Templates für die strukturierte Erfassung von Metadaten zu Forschungsprojekten und -datensätzen seitens des KompetenzwerkD bereitgestellt. 

|   |  Schema (.toml Format) | Template |  Version |
|---|---|---| --- |
| Forschungsdaten  |  [Schema](schemas/dcmi_dataset_pofile.toml) | [Template](templates/dcmi_dataset_pofile.txt)  |  0.3 |
| Forschungsprojekte  |  [Schema](schemas/project_metadata_schema.toml) | [Template](templates/project_metadata_schema.txt)  | 0.3 |

## Anleitung

Laden Sie sich die Templates herunter und füllen sie diese mit den nötigen Informationen zu Ihrem Projekt und Ihren Daten aus aus. Die auf diese Weise strukturiert erfassten Metadaten können später bei Veröffentlichung oder Archivierung beispielsweise als Teil der Dokumentation den Daten beigelegt werden. Ebenso können sie hilfreich sein, falls Metadaten für die Übergabe an ein Forschungsdatenrepositorium oder Archiv zusammengetragen werden müssen.
Das Template für Forschungsdaten dient der Beschreibung eines Datensatzes, kann aber auch für Einzeldaten oder Einzelobjekte eingesetzt werden.

Generell sind die Templates sehr allgemein / generisch gehalten, um eine breite Einsetzbarkeit zu gewährleisten. Im Gegenzug  
leidet die Spezifität und es werden eventuell nicht alle Anforderungen Ihres speziellen Szenarios erfüllt. In diesem Fall sollte die Erstellung eigener Lösungen zur Metadatenerhebung als Teil des Projekt- und Datenmanagementplans aufgeführt sein.

Für eine breite Anwendbarkeit der zusammengetragenen Daten ist ein Ausfüllen der Vorlagen in englischer Sprache anzuraten. Einzelne zentrale Felder wie Titel und Beschreibung sind zusätzlich ein zweites mal auf Deutsch vorhanden und explizit so gekennzeichnet.

Die Vorlagen bestehen aus einzelnen Blöcken, die jeweils eine Angabe zum Datensatz oder Projekt beschreiben. So dient der folgende Abschnitt der Eingabe des deutschsprachigen Titels.

    Titel="Leipziger Ausgabe der Werke von Felix Mendelssohn Bartholdy"  
    # Definition: Title of the resource in German as free text.  
    # Datatype: Text  
    # Obligation: mandatory, exactly once  

Auszufüllen ist dabei nur die erste Zeile. Die weiteren Zeilen dienen der Erläuterung, indem sie bespielsweise den Inhalt oder die Form (in diesem Fall Freitext) des einzutragenden Werts beschreiben. Auch Hinweise zur notwendigen oder freiwilligen Angabe sowie zu möglichen Mehrfachnennungen sind vorhanden. Kopieren sie in letzterem Fall einfach den gesamten Block und fügen Sie ihn ein zweites mal ein.

Andere Blöcke fordern mehr als eine Angabe.

    Subject=""  
    # Qualifier:  
        IdentifierType=""  
        Label=""  
    # Definition: A topic or scientific field of the resource.  
    # Datatype: ID  
    # Obligation: recommended, any number of times  
    # Comment: Please use a standard vocabulary for identifying the subject, we suggest using SKOS or Universal Decimal Classification. Please also state which authority file you used.  
        # Possible Vocabularies:  
        # "Universal Decimal Classification" http://www.udcsummary.info/php/index.php?lang=en  
        # "SKOS UNESCO Nomenclature" https://skos.um.es/unesco6/  
        # "Library of Congress Subject Headings" http://www.loc.gov/catdir/cpso/lcco/  
        # "Gemeinsame Normdatei" https://www.dnb.de/DE/Professionell/Standardisierung/GND/gnd.html  

TODO

## Lizenz
MIT

## Verfasser
[kompetenzwerkd@saw-leipzig.de](kompetenzwerkd@saw-leipzig.de)

