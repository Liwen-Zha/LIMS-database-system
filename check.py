# check.py is used to check:
# 1. If there is already such freezer record in the database
# 2. If there is already such person record in the database
# 3. If there is any record about the sample in the database

from py2neo import *
from py2neo.matching import *

graph = Graph("http://localhost:7474", auth=("neo4j", "database_1"))

class Check(object):
    def __init__(self, sample, freezer, person):
        self.sample = sample
        self.freezer = freezer
        self.person = person

    def freezers(self):
        nodes = NodeMatcher(graph)
        existing_freezer = nodes.match("Freezer", id=repr(self.freezer))
        if existing_freezer:
            return existing_freezer
        else:
            return False

    def persons(self):
        nodes = NodeMatcher(graph)
        existing_person = nodes.match("Person", name=repr(self.person))
        if existing_person:
            return existing_person
        else:
            return False

    def samples(self):
        nodes = NodeMatcher(graph)
        existing_samples = nodes.match("Sample", id=repr(self.sample)).all()
        if existing_samples:
            #print(existing_samples)
            return existing_samples
        else:
            return False

    def last_sample(self):
        if self.samples():
            num = len(self.samples())
            #print(num)
            nodes = NodeMatcher(graph)
            last_sample = nodes.match("Sample", id=repr(self.sample)).skip(num-1)
            #print(last_sample)
            return last_sample
        else:
            return False

    def first_sample(self):
        if self.samples():
            nodes = NodeMatcher(graph)
            first_sample = nodes.match("Sample", id=repr(self.sample)).first()
            #print(first_sample)
            return first_sample
        else:
            return False

    def quantity_calculator(self):
        if self.samples():
            all_past_samples = self.samples()
            current_value = 0
            for nodes in all_past_samples:
                bufferQ = dict(nodes)['Qvar']
                '''if dict(nodes)['Qvar_unit'].lower() == 'ml':
                    numQ = float(eval(bufferQ))
                if dict(nodes)['Qvar_unit'].lower() == 'l':
                    numQ = 1000*float(eval(bufferQ))'''
                numQ = float(eval(bufferQ))
                current_value = current_value + numQ

            return current_value

        else:
            return False
