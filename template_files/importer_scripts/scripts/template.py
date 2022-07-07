import fire

import config  # noqa: F401
from PyImporter import (
    BaseModel,
)


class Object(BaseModel):
    def __init__(self):
        self.table = "ca_table"
        self.type = "ca_type"
        self.file = "demo.csv"

    def validation(self, df, metadata):
        pass

    def custom_clean_up_dataframe(self, df, metadata):
        return df

    def files_metadata(self):
        return [
            {
                "id": 1,
                "file": self.file,
                "file_type": "csv",
                "table": self.table,
                "type": self.type,
                "idno_file_column": "file_column_name",
                "idno_format": "slug",
                "bundles": [{"CollectiveAccess_field": "file_column_name"}],
                "related_fields": self.related_fields(),
                "relationships": self.relationships(),
            },
        ]

    def relationships(self):
        return [
            {
                "target_table": "ca_table",
                "target_type": "ca_table_type",
                "target_file_column": "file_column_name",
                "relationship": "relationship_name",
                "idno_format": "slug",
                "not_found_action": {
                    "action": "create_record",
                    "bundles": [{"CollectiveAccess_field": "file_column_name"}],
                },
            },
        ]

    def related_fields(self):
        return [
            {
                "target_table": "ca_table",
                "target_type": "ca_table_type",
                "target_file_column": "file_column_name",
                "subject_field": "Collective_Access_field",
                "not_found_action": {
                    "action": "update_field",
                    "bundles": [{"CollectiveAccess_field": "file_column_name"}],
                },
            },
        ]


if __name__ == "__main__":
    obj = Object()
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
