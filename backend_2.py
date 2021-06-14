# Graph database - neo4j

from check import *
#from pandas import *
#from calculateQ import *

graph = Graph("http://localhost:7474", auth=("neo4j", "database_1"))
#graph.delete_all()

def insert(sample_type, sample_ID, loc, status, Q, unit, custodian, time):

    node_sample = Node('Sample', type=repr(sample_type), id=repr(sample_ID),
                       Qvar=float(Q), Qvar_unit=repr(unit),Qinit=None, Qinit_unit=None,
                       Qnow=None, Qnow_unit=None,status =repr(status))

    checker = Check(sample_ID, loc, custodian)

    if checker.samples() and len(checker.samples()) >= 1:

        node_pre_sample = checker.last_sample().first()
        node_1st_sample = checker.first_sample()
        update_Qinit = node_1st_sample['Qinit']
        update_Qinit_unit = node_1st_sample['Qinit_unit']
        node_sample.update({'Qinit': float(update_Qinit), 'Qinit_unit': update_Qinit_unit})

        # If use calculateQ.py to do the calculation, then:
        '''cal = Calculator(sample_ID)
        preQ = cal.quantity_up_to_now()
        currQ = preQ + float(Q)
        node_sample.update({'Qnow': currQ, 'Qnow_unit': repr(unit)})'''

        # Use the checker.py to do the calculation
        # Notice: for the designated sample id, the result from the quantity calculator in check.py is calculated
        # from the quantity variations of the sample in all the previous records, excluding the quantity variation
        # in the current record. (i.e. it is the final quantity of the sample until this moment.)
        preQ = checker.quantity_calculator()
        currQ = preQ + float(Q)
        node_sample.update({'Qnow': float(currQ), 'Qnow_unit': repr(unit)})

        properties1={'at': repr(time)}
        rel_child_of = Relationship(node_pre_sample, 'QUANTITY_CHANGE', node_sample, **properties1)
        s0 = node_pre_sample | node_sample | rel_child_of
        graph.create(s0)

    else:
        node_sample.update({'Qinit': float(Q), 'Qinit_unit': repr(unit)})
        node_sample.update({'Qnow': float(Q), 'Qnow_unit': repr(unit)})

    if checker.freezers():
        node_freezer = checker.freezers().first()
    else:
        node_freezer = Node('Freezer', id=repr(loc))

    if checker.persons():
        node_custodian = checker.persons().first()
    else:
        node_custodian = Node('Person', name=repr(custodian))

    rel_in = Relationship(node_sample,'IN',node_freezer)
    s1 = node_sample | node_freezer | rel_in
    graph.create(s1)

    properties2={'at': repr(time)}
    rel_record = Relationship(node_custodian,'OPERATE',node_sample, **properties2)
    s2 = node_custodian | node_sample | rel_record
    graph.create(s2)

def search(sample_type, sample_ID, loc, status, Q, unit, custodian):
    '''nodes = NodeMatcher(graph)
    search_samples = nodes.match("Sample", type=repr(sample_type)).all()
    print(search_samples)
    return(list(search_samples))'''

    # .evaluate() returns first matched node in node type
    # .data() returns all matched nodes in list of dictionaries

    # get all searched sample nodes
    '''if sample_type or sample_ID or status:
        if sample_type and sample_ID:
            nodes= graph.run("MATCH (a) WHERE a.type=$x1 AND a.id=$x2 RETURN a",
                     x1=repr(sample_type), x2=repr(sample_ID)).data()
        else:
            nodes= graph.run("MATCH (a) WHERE a.type=$x1 OR a.id=$x2 RETURN a",
                     x1=repr(sample_type), x2=repr(sample_ID)).data()
    
    else:
        alert["enter_sample"] = 0'''

    global search_samples
    global search_loc
    global search_people
    if sample_type:
        nodes1 = graph.run("MATCH (a) WHERE a.type=$x RETURN a", x=repr(sample_type)).data()
        search_samples = nodes1
        if nodes1 and sample_ID:
            nodes2 = []
            for n1 in nodes1:
                if n1['id'] == sample_ID:
                    nodes2.append(n1)
                else:
                    continue
            search_samples = nodes2
            if nodes2 and status:
                nodes3 = []
                for n2 in nodes2:
                    if n2['status'] == status:
                        nodes3.append(n2)
                    else:
                        continue
                search_samples = nodes3
                if nodes3 and Q:
                    nodes4 = []
                    for n3 in nodes3:
                        if n3['Q'] == str(Q):
                            nodes4.append(n3)
                        else:
                            continue
                    search_samples = nodes4
                    if nodes4 and unit:
                        nodes5= []
                        for n4 in nodes4:
                            if n4['unit'] == unit:
                                nodes5.append(n4)
                            else:
                                continue
                        search_samples = nodes5
                        if nodes5:
                            print('Can search samples!')
                        else:
                            print('Cannot search samples with the sample unit')
                    else:
                        print('No sample unit entered or Cannot search samples with the quantity variation')
                else:
                    print('No sample quantity variation entered or Cannot search samples with the status')
            else:
                print('No sample status entered or Cannot search samples with the sample id')
        else:
            print('No sample id enetered or Cannot search samples with the sample type')

    elif sample_ID:
        nodes6 = graph.run("MATCH (a) WHERE a.id=$x RETURN a", x=repr(sample_ID)).data()
        search_samples = nodes6
        if nodes6 and status:
            nodes7 = []
            for n6 in nodes6:
                if n6['status'] == status:
                    nodes7.append(n6)
                else:
                    continue
            search_samples = nodes7
            if nodes7 and Q:
                nodes8 = []
                for n7 in nodes7:
                    if n7['Q'] == str(Q):
                        nodes8.append(n7)
                    else:
                        continue
                search_samples = nodes8
                if nodes8 and unit:
                    nodes9 = []
                    for n8 in nodes8:
                        if n8['unit'] == unit:
                            nodes9.append(n8)
                        else:
                            continue
                    search_samples = nodes9
                    if nodes9:
                        print('Can search samples!')
                    else:
                        print('Cannot search samples with the sample unit')
                else:
                    print('No sample unit entered or Cannot search samples with the quantity variation')
            else:
                print('No sample quantity variation entered or Cannot search samples with the status')
        else:
            print('No sample status entered or Cannot search samples with the sample id')

    elif status:
        nodes10 = graph.run("MATCH (a) WHERE a.status=$x RETURN a", x=repr(status)).data()
        search_samples = nodes10
        if nodes10 and Q:
            nodes11 = []
            for n10 in nodes10:
                if n10['Q'] == str(Q):
                    nodes11.append(n10)
                else:
                    continue
            search_samples = nodes11
            if nodes11 and unit:
                nodes12 = []
                for n11 in nodes11:
                    if n11['unit'] == unit:
                        nodes12.append(n11)
                    else:
                        continue
                search_samples = nodes12
                if nodes12:
                        print('Can search samples!')
                else:
                    print('Cannot search samples with the sample unit')
            else:
                print('No sample unit entered or Cannot search samples with the quantity variation')
        else:
            print('No sample quantity variation entered or Cannot search samples with the status')

    elif Q:
        nodes13 = graph.run("MATCH (a) WHERE a.Qvar=$x RETURN a", x=repr(Q)).data()
        search_samples = nodes13
        if nodes13 and unit:
            nodes14 = []
            for n13 in nodes13:
                if n13['unit'] == unit:
                    nodes14.append(n13)
                else:
                    continue
            search_samples = nodes14
            if nodes14:
                print('Can search samples!')
            else:
                print('Cannot search samples with the sample unit')
        else:
            print('No sample unit entered or Cannot search samples with the quantity variation')
    
    elif unit:
        nodes15 = graph.run("MATCH (a) WHERE a.Qvar_unit=$x RETURN a", x=repr(unit)).data()
        if nodes15:
            print('Can search samples!')
        else:
            print('Cannot search samples with the sample unit')
    
    else:
        search_samples = []
        print('Cannot search samples')

    if search_samples:
        print('Can search samples!')
    else:
        print('Cannot search samples with entered criteria')


    search_loc= graph.run("MATCH (a) WHERE a.id=$x RETURN a", x=repr(loc)).data()
    if search_loc:
        print('Can search freezers!')

    else:
        search_loc = []
        print('Cannot search freezers with the freezer id')

    search_people= graph.run("MATCH (a) WHERE a.name=$x RETURN a", x=repr(custodian)).data()
    if search_people:
        print('Can search custodians!')
    else:
        search_people = []
        print('Cannot search custodians with the custodian id')


    # test
    #print(search_samples)
    #n = list(search_samples[0].values())
    #print(n[0])
    #print(type(n[0]))   # gives the node
    #print(search_loc)
    #print(search_people)

    global show_search, r_sample, r_loc, r_people
    show_search = list()
    r_sample = list()
    r_loc = list()
    r_people = list()

    for each in search_samples:

        each_node = list(each.values())[0] # each_node: class 'py2neo.data.Node'
        # print(list(each_node.items()))
        # print(dict(each_node)) #----use this
        # show_s_type = list(each_node.values())[7]
        # return all the records related to certain sample
        records = graph.run("MATCH (p: Person)-[r1:OPERATE]-> (n:Sample)-[r2:IN]->(f:Freezer) "
                            "WHERE id(n) = $s RETURN r1,r2", s=each_node.identity).data()

        # print(records) # records: list records[0]: dict
        r_who = list(records[0].values())[0] # r_who: class 'py2neo.data.OPERATE'
        # print(r_who)
        who = r_who.start_node['name']  #r_who.start_node['name']: str
        # show_rel = r_who.type('OPERATE').__name__ # return str
        who_time = list(r_who.values())[0] # return str

        r_where = list(records[0].values())[1] # r_where: class 'py2neo.data.IN'
        # print(r_where)
        where = r_where.end_node['id']

        print(who + ' operate ' + str(each_node) + ' in freezer: ' + where + ' at ' + who_time)
        r_sample.append(who + ' operate ' + str(each_node) + ' in freezer: ' + where + ' at ' + who_time)
        '''records2 = graph.run("MATCH (s1:Sample)-[r:QUANTITY_CHANGE]->(s2:Sample) "
                      "WHERE s2.id = $s RETURN r", s=each_node['id']).data()'''

    for each in search_loc:
        each_loc = list(each.values())[0]
        loc_records = graph.run("MATCH (p: Person)-[r1:OPERATE]-> (n:Sample)-[r2:IN]->(f:Freezer) "
                                "WHERE id(f) = $s RETURN n", s=each_loc.identity).data()

        for each in loc_records:
            #print(each)
            each_node = list(each.values())[0] # each_node: class 'py2neo.data.Node'
            # print(each_node.identity)

            records = graph.run("MATCH (p: Person)-[r1:OPERATE]-> (n:Sample)-[r2:IN]->(f:Freezer) "
                                "WHERE id(n) = $s AND id(f) = $m RETURN r1,r2,n",
                                s=each_node.identity, m=each_loc.identity ).data()
            # print(records)
            r_who = list(records[0].values())[0] # r_who: class 'py2neo.data.OPERATE'
            who = r_who.start_node['name']  #r_who.start_node['name']: str
            who_time = list(r_who.values())[0] # return str
            r_where = list(records[0].values())[1] # r_where: class 'py2neo.data.IN'
            where = r_where.end_node['id']

            print(who + ' operate ' + str(each_node) + ' in freezer: ' + where + ' at ' + who_time)
            r_loc.append(who + ' operate ' + str(each_node) + ' in freezer: ' + where + ' at ' + who_time)

    for each in search_people:
        each_people = list(each.values())[0]
        people_records = graph.run("MATCH (p: Person)-[r1:OPERATE]-> (n:Sample)-[r2:IN]->(f:Freezer) "
                                   "WHERE id(p) = $s RETURN n", s=each_people.identity).data()

        for each in people_records:
            each_node = list(each.values())[0] # each_node: class 'py2neo.data.Node'
            records = graph.run("MATCH (p: Person)-[r1:OPERATE]-> (n:Sample)-[r2:IN]->(f:Freezer) "
                                "WHERE id(n) = $s AND id(p) = $u RETURN r1,r2",
                                s=each_node.identity, u=each_people.identity).data()

            r_who = list(records[0].values())[0] # r_who: class 'py2neo.data.OPERATE'
            who = r_who.start_node['name']  #r_who.start_node['name']: str
            who_time = list(r_who.values())[0] # return str
            r_where = list(records[0].values())[1] # r_where: class 'py2neo.data.IN'
            where = r_where.end_node['id']

            print(who + ' operate ' + str(each_node) + ' in freezer: ' + where + ' at ' + who_time)
            r_people.append(who + ' operate ' + str(each_node) + ' in freezer: ' + where + ' at ' + who_time)

    if r_sample and not r_loc and not r_people:
        show_search = r_sample
    elif r_loc and not r_sample and not r_people:
        show_search = r_loc
    elif r_people and not r_loc and not r_sample:
        show_search = r_people
    else:
        non_repeat = list()
        total = [r_sample] + [r_loc] + [r_people]
        for content in total:
            for i in set(content):
                if i in non_repeat:
                    show_search.append(i)
                else:
                    non_repeat.append(i)

    if show_search:
        print('MATCHED RECORDS!')
        return show_search
    else:
        print('NO MATCHED RECORDS!')
        return False

# view all records in the database
# include all relationships and nodes
def view():
    all_samples = graph.run("MATCH (a: Sample) RETURN a").data()
    global view_all
    view_all = list()
    for each in all_samples:

        each_sample = list(each.values())[0] # each_node: class 'py2neo.data.Node'
        records = graph.run("MATCH (p: Person)-[r1:OPERATE]-> (n:Sample)-[r2:IN]->(f:Freezer) "
                            "WHERE id(n) = $s RETURN r1,r2", s=each_sample.identity).data()

        # print(records) # records: list records[0]: dict
        r_who = list(records[0].values())[0] # r_who: class 'py2neo.data.OPERATE'
        # print(r_who)
        who = r_who.start_node['name']  #r_who.start_node['name']: str
        # show_rel = r_who.type('OPERATE').__name__ # return str
        who_time = list(r_who.values())[0] # return str

        r_where = list(records[0].values())[1] # r_where: class 'py2neo.data.IN'
        # print(r_where)
        where = r_where.end_node['id']

        print(who + ' operate ' + str(each_sample) + ' in freezer: ' + where + ' at ' + who_time)
        view_all.append(who + ' operate ' + str(each_sample) + ' in freezer: ' + where + ' at ' + who_time)

    return view_all




























