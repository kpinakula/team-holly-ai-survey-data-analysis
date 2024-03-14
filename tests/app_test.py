import pytest
from datetime import datetime
import datatest
import pandas


class TestApp:
    def __str_to_date(self, datetime_str):
        return datetime.strptime(datetime_str, "%Y/%m/%d %H:%M:%S %p %Z")

    @pytest.fixture()
    def survey_responses(self):
        return pandas.read_csv("data/ai_at_made_tech_survey.csv")

    @pytest.mark.mandatory
    def test_timestamp_column_exists(self, survey_responses):
        datatest.validate.superset(survey_responses.columns, {"Timestamp"})

    @pytest.mark.mandatory
    def test_timestamp_column_type_is_date(self, survey_responses):
        timestamp_column = survey_responses["Timestamp"]
        timestamp_column_dates = map(self.__str_to_date, timestamp_column)

        datatest.validate(timestamp_column_dates, datetime)
