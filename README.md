# FDM Schemas

Dieses Repositorium stellt Metadaten-Schemas für die strukturierte Erfassung von Forschungsprojekte und -datensätze bereit.

## Schemas

Die Schemas befinden sich im `schemas` Verzeichnis und sind im [TOML](https://github.com/toml-lang/toml)-Format verfasst.

* `dataset_metadata_schema.toml` - Metadatenschema für Forschungsdatensätze
* `project_metadata_schema.toml` - Schema zur Beschreibung von Forschungsprojekten

## Templates

Im `templates` Verzeichnis finden sich vereinfachte Vorlagen zum Erfassen der Metadaten als Textdateien.

Sollten Änderungen in den Schemas vorgenommen werden, können die Templates mittels des `build_templates.py` Skripts erzeugt werden.

```zsh
$ python build_templates.py <schema_file>
```

### Vorraussetzungen

* Python 3.8 
* [toml Python Module](https://pypi.org/project/toml/) (Installation mit `$ pip install toml`)

## Lizenz

MIT 

## Verfasser

[kompetenzwerkd@saw-leipzig.de](kompetenzwerkd@saw-leipzig.de)
