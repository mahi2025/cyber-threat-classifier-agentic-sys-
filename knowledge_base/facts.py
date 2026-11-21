def build_facts(kb):

    facts = []
    fact_number = 1

    for threat in kb["categories"]:
        name = threat["name"]

        facts.append({
            "id": f"F{fact_number:03}",
            "statement": f"{name} belongs to {threat['group']}.",
            "subject": name,
            "predicate": "belongs_to",
            "object": threat["group"]
        })
        fact_number += 1

        for key, value in threat["attributes"].items():
            facts.append({
                "id": f"F{fact_number:03}",
                "statement": f"{name} has {key}: {value}.",
                "subject": name,
                "predicate": f"has_{key}",
                "object": value
            })
            fact_number += 1

        for indicator in threat["indicators"]:
            facts.append({
                "id": f"F{fact_number:03}",
                "statement": f"{name} may show {indicator}.",
                "subject": name,
                "predicate": "has_indicator",
                "object": indicator
            })
            fact_number += 1

    return facts
