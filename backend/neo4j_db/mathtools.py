from py2neo import *
from py2neo.matching import *

'''
  tools.py：
  This file contains three tools used in backend.py in order to improve the functionality: 
  1. existenceChecker: check if the node we want to search already exists in the database. 
  2. sampleFinder: find the first and the final node associated with the sample ID.
  3. quantityCalculator: add up all previous quantity variations for the sample. 
'''

NEO4j_URL= "http://localhost:7474"
NEO4j_USERNAME = "neo4j"
NEO4j_PASSWORD = "database_1"
graph = Graph(NEO4j_URL, auth=(NEO4j_USERNAME, NEO4j_PASSWORD))

class existenceChecker(object):
    def __init__(self, sample, freezer, person):
        self.sample = sample
        self.freezer = freezer
        self.person = person

    def check_existing_freezers(self):
        nodes = NodeMatcher(graph)
        existing_freezer = nodes.match("Freezer", id=repr(self.freezer))
        if existing_freezer:
            return existing_freezer
        else:
            return False

    def check_existing_persons(self):
        nodes = NodeMatcher(graph)
        existing_person = nodes.match("Person", name=repr(self.person))
        if existing_person:
            return existing_person
        else:
            return False

    def check_existing_samples(self):
        nodes = NodeMatcher(graph)
        existing_samples = nodes.match("Sample", id=repr(self.sample)).all()
        if existing_samples:
            return existing_samples
        else:
            return False

class sampleFinder(object):
    def __init__(self, sampleID):
        self.sampleID = sampleID

    def find_last_sample(self):
        nodes = NodeMatcher(graph)
        existing_samples = nodes.match("Sample", id=repr(self.sampleID)).all()
        num = len(existing_samples)
        last_sample = nodes.match("Sample", id=repr(self.sampleID)).skip(num-1)
        return last_sample.first()

    def find_first_sample(self):
        nodes = NodeMatcher(graph)
        first_sample = nodes.match("Sample", id=repr(self.sampleID)).first()
        return first_sample

class quantityCalculator(object):
    def __init__(self,sampleID):
        self.sampleID = sampleID

    def calculate_quantity_variations(self):
        nodes = NodeMatcher(graph)
        all_past_samples = nodes.match("Sample", id=repr(self.sampleID)).all()
        current_value = 0
        for nodes in all_past_samples:
            past_quantity_variation = float(dict(nodes)['Qvar'])
            current_value = current_value + past_quantity_variation

        return float(current_value)

