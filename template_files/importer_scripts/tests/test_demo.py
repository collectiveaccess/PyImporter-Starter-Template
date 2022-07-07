import scripts.demo as demo


class TestCreateRecordsFromMetadata:
    def test_creates_records_for_all_records_in_file(self, mocker):
        instance = demo.Demo()
        instance.search_cache = {}
        connect_mock = mocker.patch(
            "scripts.utils.connect_api.execute",
            return_value={"find": {"count": 0}, "add": {"id": [1], "idno": ["idno1"]}},
        )

        instance.create_records_from_metadata(1)

        assert connect_mock.call_count == 15


class TestPreviewCreateQueryFromMetadata:
    def test_prints_data_from_file(self, mocker):
        instance = demo.Demo()
        instance.search_cache = {}
        print_mock = mocker.patch("scripts.utils.logger.console.warning")
        connect_mock = mocker.patch(
            "scripts.utils.connect_api.execute",
            return_value={"find": {"count": 0}, "add": {"id": 1}},
        )

        instance.preview_create_query_from_metadata(1)

        assert print_mock.call_count == 8
        assert connect_mock.call_count == 6
