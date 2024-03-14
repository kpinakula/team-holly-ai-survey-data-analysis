import pytest
from datetime import datetime
import datatest
import pandas


class TestApp:
    @pytest.fixture()
    def survey_responses(self):
        return pandas.read_csv(
            "data/ai_at_made_tech_survey.csv",
            parse_dates=["Timestamp"],
            date_format="%Y/%m/%d %H:%M:%S %p %Z",
        )

    @pytest.mark.mandatory
    def test_timestamp_column_exists(self, survey_responses):
        datatest.validate.superset(survey_responses.columns, {"Timestamp"})

    @pytest.mark.mandatory
    def test_timestamp_column_contains_dates(self, survey_responses):
        submit_dates = survey_responses["Timestamp"]
        parsed_submit_dates = map(pandas.to_datetime, submit_dates)
        datatest.validate(parsed_submit_dates, datetime)
