import fire

import config  # noqa: F401
from PyImporter import (
    BaseModel,
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

    # perform some basic data checking
    def validation(self, df, metadata):
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
                # set bundles to empty list if we want to create relationship_type
                # or related fields, but not create main records
                "bundles": [],
                "relationships": [
                    {
                        "target": "ca_objects",
                        "find_file_column": "Related Objects",
                        "relationship_type": "related",
                        # apply ca_transform to "find_file_column"
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
                "target": "ca_entities",
                "target_type": "ind",
                "find_file_column": "Collector",
                "relationship_type": "collector",
                "ca_entity_parser": "parse_name_org_surname_comma",
                "search_outcome": {
                    # create new record if no search result
                    "action": "create_records",
                    "idno_format": "integer",
                    "bundles": [{"preferred_labels": "Collector"}],
                },
            },
            {
                "target": "ca_places",
                "find_file_column": ["Continent", "Country"],
                "relationship_type": "located",
                # do not include not_found_action, if you want the script to
                # only log errors if no search result
            },
        ]

    def related_fields(self):
        return [
            {
                "target": "ca_entities",
                "target_type": "ind",
                "find_file_column": "Status By",
                "subject_field": "object_status_name",
                "search_outcome": {
                    # set fields if no search result
                    "action": "set_subject_fields",
                    "idno_format": "integer",
                    "bundles": [{"txt_status_name": "Status By"}],
                },
            },
        ]


if __name__ == "__main__":
    obj = Demo()
    fire.Fire(
        {
            "validation": obj.validation_from_metadata,
            "preview_create": obj.preview_create_query_from_metadata,
            "create_records": obj.create_records_from_metadata,
            "preview_edit": obj.preview_edit_query_from_metadata,
            "edit_records": obj.edit_records_from_metadata,
            "preview_replace": obj.preview_replace_query_from_metadata,
            "replace_records": obj.replace_records_from_metadata,
            "preview_delete": obj.preview_delete_query_from_metadata,
            "delete_records": obj.delete_records_from_metadata,
            "preview_delete_by_identifier": obj.preview_delete_records_by_identifier,
            "delete_records_by_identifier": obj.delete_records_by_identifier,
            "preview_edit_relationships": obj.preview_edit_relationships_from_metadata,
            "edit_relationships": obj.edit_relationships_from_metadata,
            "preview_delete_relationships": obj.preview_delete_relationships_from_metadata,  # noqa: E501
            "delete_relationships": obj.delete_relationships_from_metadata,
            "truncate_list": obj.truncate_list,
            "truncate_table": obj.truncate_table,
        }
    )
