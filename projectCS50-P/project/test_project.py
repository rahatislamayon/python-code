import os
import pytest
from project import log_session, get_total_minutes, get_daily_minutes
from datetime import date


TEST_FILE = "study_log.csv"


def setup_function():
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)


def test_log_session():
    log_session("Math", 60)
    assert get_total_minutes() == 60


def test_get_total_minutes():
    log_session("Physics", 30)
    log_session("Chemistry", 45)
    assert get_total_minutes() == 75


def test_get_daily_minutes():
    today = date.today().isoformat()
    log_session("CS", 50)
    assert get_daily_minutes(today) == 50


def test_invalid_minutes():
    with pytest.raises(ValueError):
        log_session("Biology", -10)
check50 cs50/problems/2022/python/seasons

