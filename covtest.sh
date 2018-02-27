#!/bin/bash

echo ""
echo "Checking for linting errors"
flake8 --select E,W --max-line-length=140 --ignore E722 jarviscli/
echo "lint errors checked"
echo ""
cd jarviscli/
rm *.branch
echo "" > parse_date@textParser.py.branch
echo "" > main@weather_pinpoint.py.branch
echo "" > score@cricket.py.branch
echo "" > main@translate.py.branch
echo "" > parse_number@textParser.py.branch
echo "" > request_news@news.py.branch
echo "" > organise@file_organise.py.branch
echo "" > precmd@Jarvis.py.branch
echo "" > reminder_handler@reminder.py.branch
echo "" > get_opt@news.py.branch
echo "" > tests/test_manual/__init__.py
echo "checking for unit test"
python -m unittest discover
rm tests/test_manual/__init__.py
echo "unit tests checked"
echo ""