
from knowledge_base.loader import load_knowledge_base
from knowledge_base.attributes import build_threat_attributes
from knowledge_base.facts import build_facts
from knowledge_base.relationships import build_relationships


kb = load_knowledge_base()

attributes = build_threat_attributes(kb)
facts = build_facts(kb)
relationships = build_relationships(kb)

print("Total threats:", len(attributes))
print("Total facts:", len(facts))
print("Total relationships:", len(relationships))

print("\nThreat attributes:")
for name, data in attributes.items():
    print(data["id"], "-", name)

print("\nRelationships:")
for relationship in relationships:
    print(
        relationship["subject"],
        relationship["relation"],
        relationship["object"]
    )
