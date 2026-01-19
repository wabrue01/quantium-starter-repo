#!/bin/bash

#activate the virtual environment
source venv/Scripts/activate

#run the test suite
pytest
TEST_EXIT_CODE=$?

#deactivate the virtual environment
deactivate

#exit with the test result status
if [ $TEST_EXIT_CODE -eq 0 ]; then
    exit 0
else
    exit 1
fi