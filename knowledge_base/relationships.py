
def build_relationships(kb):

    relationships = []

    threats_by_id = {
        threat["id"]: threat
        for threat in kb["categories"]
    }

    for threat in kb["categories"]:
        for related_id in threat["related_threats"]:

            related_threat = threats_by_id.get(related_id)

            if related_threat:
                relationships.append({
                    "subject": threat["name"],
                    "relation": "related_to",
                    "object": related_threat["name"]
                })

    return relationships
