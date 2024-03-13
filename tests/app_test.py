import pytest
import datatest
import pandas

class TestApp:

    @pytest.fixture()
    def data_table(self):
        return pandas.read_csv("data/ai_at_made_tech_survey.csv")

    @pytest.mark.mandatory
    def test_timestamp_column_exists(self, data_table):
        datatest.validate.superset(
            data_table.columns,
            {'Timestamp'}
        )
