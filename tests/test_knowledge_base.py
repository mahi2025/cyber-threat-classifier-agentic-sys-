from knowledge_base.loader import load_knowledge_base


def test_knowledge_base_loads():
    kb = load_knowledge_base()
    assert "categories" in kb


def test_threat_count():
    kb = load_knowledge_base()
    assert len(kb["categories"]) == 10


def test_threats_have_required_fields():
    kb = load_knowledge_base()

    for threat in kb["categories"]:
        assert all(
            field in threat
            for field in [
                "id", "name", "group", "description",
                "attributes", "indicators", "related_threats"
            ]
        )


def test_threat_ids_are_unique():
    kb = load_knowledge_base()

    ids = [threat["id"] for threat in kb["categories"]]

    assert len(ids) == len(set(ids))