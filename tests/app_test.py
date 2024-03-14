import pytest
from datetime import datetime
import datatest
import pandas


class TestApp:
    def __str_to_date(self, datetime_str):
        return datetime.strptime(datetime_str, "%Y/%m/%d %H:%M:%S %p %Z")

    @pytest.fixture()
    def data_table(self):
        return pandas.read_csv("data/ai_at_made_tech_survey.csv")

    @pytest.mark.mandatory
    def test_timestamp_column_exists(self, data_table):
        datatest.validate.superset(data_table.columns, {"Timestamp"})

    @pytest.mark.mandatory
    def test_timestamp_column_type_is_date(self, data_table):
        timestamp_column = data_table["Timestamp"]
        timestamp_column_dates = map(self.__str_to_date, timestamp_column)

        datatest.validate(timestamp_column_dates, datetime)
