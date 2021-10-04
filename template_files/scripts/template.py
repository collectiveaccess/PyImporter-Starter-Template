import fire

import config  # noqa: F401
from PyImporter import (
    BaseModel,
    format_data_file_path,
)


class Demo(BaseModel):
    def __init__(self):
        self.table = "ca_table"
        self.type = "ca_type"
        # if you only import one file per script, set self.file and self.file_path
        self.file = "demo.csv"
        self.file_path = format_data_file_path(self.file)

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
                "target_column": "file_column_name",
                "relationship": "relationship_name",
            },
        ]

    def related_fields(self):
        return [
            {
                "target_table": "ca_table",
                "target_type": "ca_table_type",
                "target_column": "file_column_name",
                "subject_field": "Collective_Access_field",
            },
        ]


if __name__ == "__main__":
    obj = Demo()
    fire.Fire(
        {
            "validation": obj.validation_from_metadata,
            "create_records": obj.create_records_from_metadata,
            "preview_create": obj.preview_create_query_from_metadata,
            "truncate_table": obj.truncate_table,
            "delete_records": obj.delete_records,
            "delete_relationships": obj.delete_relationships_from_metadata,
            "preview_update": obj.preview_update_query_from_metadata,
            "update_records": obj.update_records_from_metadata,
        }
    )
