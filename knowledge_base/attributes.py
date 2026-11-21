
def build_threat_attributes(kb):
    threat_attributes = {}

    for threat in kb["categories"]:
        threat_attributes[threat["name"]] = {
            "id": threat["id"],
            "category": threat["group"],
            "attributes": threat["attributes"],
            "indicators": threat["indicators"],
            "indicator_codes": threat["indicators"],
            "targets": [
                threat["attributes"]["target"]
            ] if "target" in threat["attributes"] else []
        }

    return threat_attributes
