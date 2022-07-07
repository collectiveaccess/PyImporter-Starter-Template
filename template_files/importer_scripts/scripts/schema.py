import fire
import config  # noqa: F401
from PyImporter import BaseModel, create_get_tables_query


class Schema(BaseModel):
    def __init__(self):
        pass

    def custom_clean_up_dataframe(self, df, metadata):
        return df

    def get_tables(self):
        create_get_tables_query()


if __name__ == "__main__":
    obj = Schema()
    fire.Fire(
        {
            "get_tables": obj.get_tables,
        }
    )
