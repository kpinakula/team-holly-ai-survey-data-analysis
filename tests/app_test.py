import pytest
from datetime import datetime
import datatest
import pandas
import matplotlib.pyplot as pyplot


class TestApp:
    @pytest.fixture()
    def survey_responses(self):
        return pandas.read_csv(
            "data/ai_at_made_tech_survey.csv",
            parse_dates=["Timestamp"],
            date_format="%Y/%m/%d %H:%M:%S %p %Z",
            header=0,
            names=[
                "Timestamp",
                "work_area",
                "ai_tool_use_yes_or_no",
                "ai_tool_use_why_not",
                "ai_tools_frequently_used",
                "ai_tools_effectiveness_rating",
                "ai_tools_productivity_gains",
                "ai_tools_output_trust_rating",
                "ai_tools_challenges_limitations",
                "anything_else",
                "interest_in_sessions",
            ],
        )

    @pytest.mark.mandatory
    def test_timestamp_column_exists(self, survey_responses):
        datatest.validate.superset(survey_responses.columns, {"Timestamp"})

    @pytest.mark.mandatory
    def test_timestamp_column_contains_dates(self, survey_responses):
        submit_dates = survey_responses["Timestamp"]
        parsed_submit_dates = map(pandas.to_datetime, submit_dates)
        datatest.validate(parsed_submit_dates, datetime)

    @pytest.mark.mandatory
    def test_work_area_column_contains_strings(self, survey_responses):
        work_areas = survey_responses["work_area"]
        datatest.validate(work_areas, str)

    @pytest.mark.mandatory
    def x_test_effectiveness_rating_column_can_be_plotted(self, survey_responses):
        effectiveness_ratings = survey_responses["ai_tools_effectiveness_rating"]
        effectiveness_ratings.plot()
        pyplot.show()
        datatest.validate(effectiveness_ratings, int)

    @pytest.mark.mandatory
    def x_test_effectiveness_rating_column_can_be_plotted(self, survey_responses):
        effectiveness_ratings = survey_responses["ai_tools_effectiveness_rating"]
        effectiveness_ratings_bar_chart = (
            survey_responses.groupby(effectiveness_ratings).size().plot.bar()
        )

        effectiveness_ratings_bar_chart.bar_label(
            effectiveness_ratings_bar_chart.containers[0]
        )

        pyplot.xlabel(
            "How would you rate the effectiveness of AI tools in improving your productivity or efficiency?"
        )

        pyplot.show()

        datatest.validate(effectiveness_ratings, int)

    @pytest.mark.mandatory
    def test_number_of_responses_is_as_expected(self, survey_responses):
        effectiveness_ratings = survey_responses["ai_tools_effectiveness_rating"]
        all_responses = effectiveness_ratings.size
        empty_responses = effectiveness_ratings.isnull().sum()
        real_responses = effectiveness_ratings.notnull().sum()
        assert empty_responses == 9
        assert all_responses == 27
        assert real_responses == all_responses - empty_responses
        datatest.validate(real_responses, int)

    @pytest.mark.mandatory
    def test_effectiveness_ratings_column_contains_integers(self, survey_responses):
        effectiveness_ratings = survey_responses["ai_tools_effectiveness_rating"]
        real_responses = effectiveness_ratings.notnull().sum()
        datatest.validate(real_responses, int)
