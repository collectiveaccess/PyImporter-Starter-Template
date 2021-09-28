import fire
import pandas as pd

import config  # noqa: F401
from PyImporter import (
    BaseModel,
    format_data_file_path,
    validate_dimension_column,
    add_dimension_unit_to_column,
    duplicate_values_for_column,
)


# Setup class to inherit from PyImporter BaseModel
class Demo(BaseModel):
    def __init__(self):
        # table is required
        self.table = "ca_objects"
        #
        self.type = "archeology"
        # if you only import one file per script, set self.file and self.file_path
        self.file = "demo.csv"
        self.file_path = format_data_file_path(self.file)

    # perform some basic data checking
    def validation(self):
        # set dtype=str to prevent pandas from converting data types
        df = pd.read_csv(self.file_path, dtype=str)
        df = df.dropna(axis="index", how="all")

        # check if ids are unique
        column = "Object ID"
        duplicate_values_for_column(df, column)

        # check if dimensions end with a unit of measurement (e.g. kg)
        columns = [
            ["Dimensions: Length", "cm"],
            ["Dimensions: Weight", "kg"],
        ]
        for col in columns:
            validate_dimension_column(df, col[0], col[1])

    # perform in-memory data wrangling
    def custom_clean_up_dataframe(self, df, metadata):
        if metadata["id"] == 1:
            # add missing unit to "Dimensions: Length"
            add_dimension_unit_to_column(df, "Dimensions: Length", "cm")

        return df

    def files_metadata(self):
        return [
            {
                "id": 1,
                "file": self.file,
                "file_type": "csv",
                "idno_file_column": "Object ID",
                "idno_format": "column",
                "table": self.table,
                "type": self.type,
                "bundles": [
                    {"preferred_labels": "Object Name"},
                    {
                        "dimensions": [
                            {"dimensions_length": "Dimensions: Length"},
                            {"dimensions_width": "Dimensions: Weight"},
                        ]
                    },
                    {
                        "cont_other_numbers": [
                            {"other_number": "Other Object Number"},
                            # apply ca_transform to a field
                            {
                                "type": "other",
                                "ca_transform": [{"action": "plain_text"}],
                            },
                        ],
                        # apply ca_transform to a container
                        "ca_transform": [
                            {
                                "action": "delimited_values",
                                "separator": "; ",
                                "target": "Other Object Number",
                            }
                        ],
                    },
                ],
                "related_fields": self.related_fields(),
                "relationships": self.relationships(),
            },
            {
                "id": 2,
                "file": self.file,
                "file_type": "csv",
                "idno_file_column": "Object ID",
                "idno_format": "column",
                "table": self.table,
                "type": self.type,
                # set bundles to empty list if we want to create relationships
                # or related fields, but not create main records
                "bundles": [],
                "relationships": [
                    {
                        "target_table": "ca_objects",
                        "target_column": "Related Objects",
                        "relationship": "related",
                        "idno_format": "column",
                        # apply ca_transform to "target_column"
                        "ca_transform": [
                            {"action": "delimited_values", "separator": "; "}
                        ],
                    },
                ],
            },
        ]

    def relationships(self):
        return [
            {
                "target_table": "ca_entities",
                "target_type": "ind",
                "target_column": "Collector",
                "relationship": "collector",
                "idno_format": "integer",
                "not_found_action": {
                    # create new record if no search result
                    "action": "create_record",
                    "bundles": [
                        {
                            "preferred_labels": [
                                {
                                    "preferred_labels": "Collector",
                                    "ca_transform": [
                                        {
                                            "action": "parse_name_org_surname_comma",
                                        }
                                    ],
                                }
                            ]
                        }
                    ],
                },
            },
            {
                "target_table": "ca_places",
                "target_column": ["Continent", "Country"],
                "relationship": "located",
                "idno_format": "slug",
                # do not include not_found_action, if you want the script to
                # only log errors if no search result
            },
        ]

    def related_fields(self):
        return [
            {
                "target_table": "ca_entities",
                "target_type": "ind",
                "target_column": "Status By",
                "subject_field": "object_status_name",
                "idno_format": "integer",
                "not_found_action": {
                    # set fields if no search result
                    "action": "update_field",
                    "bundles": [{"txt_status_name": "Status By"}],
                },
            },
        ]


if __name__ == "__main__":
    obj = Demo()
    fire.Fire(
        {
            "validation": obj.validation,
            "create_records": obj.create_records_from_metadata,
            "preview_create": obj.preview_create_query_from_metadata,
            "truncate_table": obj.truncate_table,
            "delete_records": obj.delete_records,
            "delete_relationships": obj.delete_relationships_from_metadata,
        }
    )
