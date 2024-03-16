import json
import report
import pytest


# for testing if data in the file dictionary or not
def test_report_json():
    report.generate_report()

    with open("report.json") as file:
        print("[ Fixture ]: ...return report data")
        dt = json.load(file)
    
        assert type(dt) == dict


# for testing if the timestamp and status in the dictionary
def test_report_fields():
    report.generate_report()

    with open("report.json") as file:
        print("[ Fixture ]: ...return report data")
        dt = json.load(file)
    
        assert "timestamp" in dt
        assert "status" in dt