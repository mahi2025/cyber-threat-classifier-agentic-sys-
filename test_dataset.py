import json

from knowledge_base.attributes import THREAT_ATTRIBUTES
from reasoning.rules import RULES


def load_dataset():

    with open("data/threats.json", "r") as file:
        return json.load(file)


def test_unique_event_ids():

    dataset = load_dataset()

    ids = [event["event_id"] for event in dataset]

    assert len(ids) == len(set(ids))


def test_required_fields():

    dataset = load_dataset()

    required = {
        "event_id",
        "event_type",
        "description",
        "observed_indicators",
        "expected_label",
        "severity",
        "source"
    }

    for event in dataset:
        assert required.issubset(event.keys())


def test_indicators_are_recognized():

    dataset = load_dataset()

    known_indicators = set()

    for threat in THREAT_ATTRIBUTES.values():
        known_indicators.update(
            threat["indicator_codes"]
        )

    for rule in RULES:
        known_indicators.update(rule["all"])
        known_indicators.update(rule["any"])

    for event in dataset:

        for indicator in event["observed_indicators"]:

            assert indicator in known_indicators, (
                f"Unknown indicator: {indicator}"
            )


def test_expected_labels():

    dataset = load_dataset()

    valid_labels = {
        "Phishing",
        "Malware",
        "Brute Force",
        "Benign",
        "Undetermined"
    }

    for event in dataset:
        assert event["expected_label"] in valid_labels