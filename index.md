# Metadatenerfassung für Forschungsdaten und Projekte

## Metadatenschemata / Vorlagen

|   |  Schema (.toml Format) | Template |  Version |
|---|---|---| --- |
| Forschungsdaten  |  [Schema](schemas/dcmi_dataset_pofile.toml) | [Template](templates/dcmi_dataset_pofile.txt)  |  0.3 |
| Forschungsprojekte  |  [Schema](schemas/project_metadata_schema.toml) | [Template](templates/project_metadata_schema.txt)  | 0.3 |
<br>

## Informationen

Auf dieser Seite werden Schemas und Templates für die strukturierte Erfassung von Metadaten zu Forschungsprojekten und -datensätzen seitens des KompetenzwerkD bereitgestellt.

Die auf diese Weise strukturiert erfassten Metadaten können später bei Veröffentlichung oder Archivierung beispielsweise als Teil der Dokumentation den Daten beigelegt werden. Ebenso können sie eine hilfreiche Basis sein, falls Metadaten für die Übergabe an ein Forschungsdatenrepositorium oder Archiv zusammengetragen werden müssen.

Von technischer Seite sei auf die maschinelle Auswertbarkeit...

Generell sind die Templates sehr allgemein / generisch gehalten, um eine breite Einsetzbarkeit zu gewährleisten. Im Gegenzug  
leidet die Spezifität und es werden eventuell nicht alle Anforderungen Ihres speziellen Szenarios erfüllt. In diesem Fall sollte die Erstellung eigener Lösungen zur Metadatenerhebung möglichst schon als Teil des Projektantrags und des Datenmanagementplans aufgeführt sein.

## Anleitung

Laden Sie sich die Templates (rechte Spalte) herunter, öffnen Sie sie in einem beliebigen Texteditor und füllen sie diese mit den nötigen Informationen zu Ihrem Projekt und Ihren Daten aus.

Das Template für Forschungsdaten dient der Beschreibung eines Datensatzes, kann aber auch für Einzeldaten oder Einzelobjekte eingesetzt werden.

Für eine möglichst breite Nutzbarkeit der zusammengetragenen Daten ist ein Ausfüllen der Vorlagen in englischer Sprache anzuraten. Einzelne zentrale Felder wie Titel und Beschreibung sind zusätzlich ein zweites mal auf Deutsch vorhanden und explizit so gekennzeichnet.

Die Vorlagen bestehen aus einzelnen Blöcken, die jeweils eine Angabe zum Datensatz oder Projekt beschreiben. So dient der folgende Abschnitt der Eingabe des deutschsprachigen Titels.

    Titel="Leipziger Ausgabe der Werke von Felix Mendelssohn Bartholdy"  
    # Definition: Title of the resource in German as free text.  
    # Datatype: Text  
    # Obligation: mandatory, exactly once  

Auszufüllen ist dabei nur die erste Zeile, was hier bereits geschehen ist. Die weiteren Zeilen dienen der Erläuterung, indem sie bespielsweise den Inhalt oder die Form (in diesem Fall Freitext) des einzutragenden Werts beschreiben. Auch Hinweise zur notwendigen oder freiwilligen Angabe sowie zu möglichen Mehrfachnennungen sind vorhanden. Kopieren sie in letzterem Fall einfach den gesamten Block und fügen Sie ihn ein zweites mal ein.

Andere Blöcke fordern mehr als eine Angabe. Im Folgenden soll das "Subject" also das Fachgebiet angegeben werden.

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
        # "Dewey Decimal Classification" - https://www.oclc.org/en/dewey.html  
        # "SKOS UNESCO Nomenclature" https://skos.um.es/unesco6/  
        # "Library of Congress Subject Headings" http://www.loc.gov/catdir/cpso/lcco/  
        # "Gemeinsame Normdatei" https://www.dnb.de/DE/Professionell/Standardisierung/GND/gnd.html  

In einem solchen Fall macht es Sinn, statt freien Text zu nutzen, auf ein vorgegebenes standardisiertes Vokabular bzw. einen Identifikator (ID) zurückzugreifen. Übergreifend wird für Fachgebiete beispielsweise die Dewey Decimal Classification genutzt, aber auch andere von uns angegebene Klassifikationssysteme sind möglich.

Bei Nutzung von Dewey würde man das gewünschte Fachgebiet im entsprechenden Katalog nachschlagen, z.B unter https://deweysearchde.pansoft.de/webdeweysearch/mainClasses.html

Nehmen wir an, das Ergebnis wäre die Kategorie "Geschichtsphilosophie und Geschichtstheorie" mit der Identifikationsnummer "901". Dann sollte in das Feld "Subject" die ID eingetragen werden, ergänzt durch das dazugehörige natürlichsprachliche Label der Kategorie und Informationen zum genutzten Klassifikationssystem.

    Subject="901"  
    # Qualifier:  
        IdentifierType="Dewey Decimal Classification"  
        Label="Geschichtsphilosophie und Geschichtstheorie"  

Wir hoffen, diese Kurzanleitung war hilfreich und erläutert in ausreichender Weise Erstellung und Nutzen
Wenden Sie sich bei offenen Fragen oder genereller Beratung zum Thema Forschungsdatenmanagement gern jederzeit an Ihr KompetenzwerkD!

## Lizenz
MIT https://opensource.org/licenses/mit-license.php

## Verfasser
[kompetenzwerkd@saw-leipzig.de](kompetenzwerkd@saw-leipzig.de)

