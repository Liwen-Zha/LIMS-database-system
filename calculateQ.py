from check_existing import *

graph = Graph("http://localhost:7474", auth=("neo4j", "database_1"))

class Calculator(object):
    def __init__(self, id):
        self.id = id

    def quantity_up_to_now(self):
        all_past_samples = Check(self.id,'','').samples()
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
