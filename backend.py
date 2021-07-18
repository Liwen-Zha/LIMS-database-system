from tools import *
import re
import time

'''
  backend.py:
  This file is the core module of the system, including different functions required for the LIMS.
  It will be used in the Flask framework to complete the backend design.
'''

NEO4j_URL= "http://localhost:7474"
NEO4j_USERNAME = "neo4j"
NEO4j_PASSWORD = "database_1"
graph = Graph(NEO4j_URL, auth=(NEO4j_USERNAME, NEO4j_PASSWORD))

def insert(sample_type, sample_ID, loc, status, Q, unit, custodian, time):
    '''
    Log the sample transaction into the database.

    keyword arguments:
    sample_type -- the type of the sample (e.g., blood, DNA, RNA)
    sample_ID -- the identification number of the sample (e.g., blo0001)
    loc -- the physical location (i.e., the freezer) of the sample (e.g., f1)
    status -- the status of the sample, including available, in use and booked.
    Q -- the quantity variation of the sample (e.g., 10, -5, +2.1)
    unit -- the unit of Q (e.g., ml, tube, plate)
    custodian -- the custodian of the sample transaction （e.g., peter, linda)
    time -- the occurrence time of the sample transaction
    '''
    node_sample = Node('Sample', type=repr(sample_type), id=repr(sample_ID),
                       Qvar=float(Q), Qvar_unit=repr(unit),Qinit=None, Qinit_unit=None,
                       Qnow=None, Qnow_unit=None,status =repr(status))

    check_existence = existenceChecker(sample_ID, loc, custodian)

    if check_existence.check_existing_samples() and len(check_existence.check_existing_samples()) >= 1:

        find_samples = sampleFinder(sample_ID)

        node_pre_sample = find_samples.find_last_sample()
        node_1st_sample = find_samples.find_first_sample()
        update_Qinit = node_1st_sample['Qinit']
        update_Qinit_unit = node_1st_sample['Qinit_unit']
        node_sample.update({'Qinit': float(update_Qinit), 'Qinit_unit': update_Qinit_unit})

        # Use the class quantityCalculator() in tools.py to calculate the current quantity of the sample.
        # Notice: for each sample id, the result of quantityCalculator() is the sum of all previous quantity variations
        # of the sample, which means it excludes the quantity variation of the current sample transaction.
        calculate_quantity = quantityCalculator(sample_ID)
        previous_quantity = calculate_quantity.calculate_quantity_variations()
        current_quantity = previous_quantity + float(Q)
        node_sample.update({'Qnow': float(current_quantity), 'Qnow_unit': repr(unit)})

        properties1={'at': repr(time)}
        rel_child_of = Relationship(node_pre_sample, 'QUANTITY_CHANGE', node_sample, **properties1)
        s0 = node_pre_sample | node_sample | rel_child_of
        graph.create(s0)

    else:
        node_sample.update({'Qinit': float(Q), 'Qinit_unit': repr(unit)})
        node_sample.update({'Qnow': float(Q), 'Qnow_unit': repr(unit)})

    if check_existence.check_existing_freezers():
        node_freezer = check_existence.check_existing_freezers().first()
    else:
        node_freezer = Node('Freezer', id=repr(loc))

    if check_existence.check_existing_persons():
        node_custodian = check_existence.check_existing_persons().first()
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
    '''
    Search the sample transaction in the database.

    keyword arguments:
    sample_type -- the type of the sample (e.g., blood, DNA, RNA)
    sample_ID -- the identification number of the sample (e.g., blo0001)
    loc -- the physical location (i.e., the freezer) of the sample (e.g., f1)
    status -- the status of the sample, including available, in use and booked.
    Q -- the quantity variation of the sample (e.g., 10, -5, +2.1)
    unit -- the unit of Q (e.g., ml, tube, plate)
    custodian -- the custodian of the sample transaction （e.g., peter, linda)
    time -- the occurrence time of the sample transaction
    '''
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

    show_search = list()
    r_sample = list()
    r_loc = list()
    r_people = list()

    for each in search_samples:
        each_node = list(each.values())[0]
        records = graph.run("MATCH (p: Person)-[r1:OPERATE]-> (n:Sample)-[r2:IN]->(f:Freezer) "
                            "WHERE id(n) = $s RETURN r1,r2", s=each_node.identity).data()

        r_who = list(records[0].values())[0]
        who = r_who.start_node['name']
        who_time = list(r_who.values())[0]

        r_where = list(records[0].values())[1]
        where = r_where.end_node['id']

        print(who + ' operate ' + str(each_node) + ' in freezer: ' + where + ' at ' + who_time)
        r_sample.append(who + ' operate ' + str(each_node) + ' in freezer: ' + where + ' at ' + who_time)

    for each in search_loc:
        each_loc = list(each.values())[0]
        loc_records = graph.run("MATCH (p: Person)-[r1:OPERATE]-> (n:Sample)-[r2:IN]->(f:Freezer) "
                                "WHERE id(f) = $s RETURN n", s=each_loc.identity).data()

        for each in loc_records:
            each_node = list(each.values())[0]

            records = graph.run("MATCH (p: Person)-[r1:OPERATE]-> (n:Sample)-[r2:IN]->(f:Freezer) "
                                "WHERE id(n) = $s AND id(f) = $m RETURN r1,r2,n",
                                s=each_node.identity, m=each_loc.identity ).data()

            r_who = list(records[0].values())[0]
            who = r_who.start_node['name']
            who_time = list(r_who.values())[0]
            r_where = list(records[0].values())[1]
            where = r_where.end_node['id']

            print(who + ' operate ' + str(each_node) + ' in freezer: ' + where + ' at ' + who_time)
            r_loc.append(who + ' operate ' + str(each_node) + ' in freezer: ' + where + ' at ' + who_time)

    for each in search_people:
        each_people = list(each.values())[0]
        people_records = graph.run("MATCH (p: Person)-[r1:OPERATE]-> (n:Sample)-[r2:IN]->(f:Freezer) "
                                   "WHERE id(p) = $s RETURN n", s=each_people.identity).data()

        for each in people_records:
            each_node = list(each.values())[0]
            records = graph.run("MATCH (p: Person)-[r1:OPERATE]-> (n:Sample)-[r2:IN]->(f:Freezer) "
                                "WHERE id(n) = $s AND id(p) = $u RETURN r1,r2",
                                s=each_node.identity, u=each_people.identity).data()

            r_who = list(records[0].values())[0]
            who = r_who.start_node['name']
            who_time = list(r_who.values())[0]
            r_where = list(records[0].values())[1]
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

def view_logs():
    '''
    View all sample transactions in the database.
    '''
    all_samples = graph.run("MATCH (a: Sample) RETURN a").data()
    view_all = list()
    for each in all_samples:
        each_sample = list(each.values())[0]
        records = graph.run("MATCH (p: Person)-[r1:OPERATE]-> (n:Sample)-[r2:IN]->(f:Freezer) "
                            "WHERE id(n) = $s RETURN r1,r2", s=each_sample.identity).data()

        r_who = list(records[0].values())[0]
        who = r_who.start_node['name']
        who_time = list(r_who.values())[0]

        r_where = list(records[0].values())[1]
        where = r_where.end_node['id']

        txt = [who,'operate',str(each_sample),' in freezer: ',where,' at ', who_time ]
        view_all.append(txt)

    return view_all

def view_samples():
    '''
    View all samples registered in the database.
    '''
    show_check = list()
    uni_id = list()
    uni_samples = list()
    alone_samples = list()
    alone_id = list()

    final_sample = graph.run("MATCH (s0: Sample)-[r: QUANTITY_CHANGE]-> (s1:Sample) RETURN s1").data()

    init_id = list(final_sample[0].values())[0]['id']
    uni_id.append(init_id)
    uni_samples.append(list(final_sample[0].values())[0])
    for each in final_sample[1:]:
        each_node = list(each.values())[0]
        each_sid = each_node['id']
        if each_sid not in uni_id:
            uni_id.append(each_sid)
            uni_samples.append(each_node)
        else:
            id_index = uni_id.index(each_sid)
            uni_samples[id_index] = each_node

    sample_nodes = graph.run("MATCH (a: Sample) RETURN a").data()
    for each in sample_nodes:
        every_node = list(each.values())[0]
        every_sid = every_node['id']
        if every_sid not in uni_id:
            alone_samples.append(every_node)
            alone_id.append(every_sid)

    all_samples = uni_samples + alone_samples

    for each in all_samples:
        records = graph.run("MATCH (p: Person)-[r1:OPERATE]->(n:Sample)-[r2:IN]->(f:Freezer) WHERE id(n) = $s RETURN r1,r2",
                            s=each.identity).data()

        find_who = list(records[0].values())[0]
        txt_who = find_who.start_node['name']
        find_where = list(records[0].values())[1]
        txt_where = find_where.end_node['id']

        txt = 'Type:{} ID:{} Quantity:{} Unit:{} Location:{} Status:{} latest operated by:{}'.\
            format(each['type'], each['id'], each['Qnow'], each['Qnow_unit'], txt_where, each['status'], txt_who)

        show_check.append(txt)

    return show_check

def check(sample_type, sample_ID, loc, status, custodian):
    '''
    Check: 1. the latest information of certain sample
           2. the contents in certain freezer
           3. the samples managed by certain custodian

    keyword arguments:
    sample_type -- the type of the sample (e.g., blood, DNA, RNA)
    sample_ID -- the identification number of the sample (e.g., blo0001)
    loc -- the physical location (i.e., the freezer) of the sample (e.g., f1)
    status -- the status of the sample, including available, in use and booked.
    custodian -- the custodian of the sample transaction （e.g., peter, linda)
    '''
    this_input = [sample_type, sample_ID, loc, status, custodian]
    while '' in this_input:
        this_input.remove('')

    show_check = view_samples()
    check_result = list()

    for each in show_check:
        this_type = re.findall(r"Type:'(.+)' ID", each)
        this_id = re.findall(r"ID:'(.+)' Quantity", each)
        this_loc = re.findall(r"Location:'(.+)' Status", each)
        this_sta = re.findall(r"Status:'(.+)' latest", each)
        this_who = re.findall(r"latest operated by:'(.+)'", each)
        this_element = [this_type[0], this_id[0], this_loc[0], this_sta[0], this_who[0]]

        if set(this_input) < set(this_element):
            check_result.append(each)
        else:
            continue

    return check_result

def search_improved(sample_type, sample_ID, loc, status, Q, unit, custodian):
    '''
    This function is simpler compared with search(sample_type, sample_ID, loc, status, Q, unit, custodian).
    The method is similar to the design of the check function.
    Firstly, call the view_logs() function, get all the logs in the database;
    Secondly, check if the entered criteria match the keywords of each log;
    Thirdly, store all the matched logs and return them.

    keyword arguments:
    sample_type -- the type of the sample (e.g., blood, DNA, RNA)
    sample_ID -- the identification number of the sample (e.g., blo0001)
    loc -- the physical location (i.e., the freezer) of the sample (e.g., f1)
    status -- the status of the sample, including available, in use and booked.
    Q -- the quantity variation of the sample (e.g., 10, -5, +2.1)
    unit -- the unit of Q (e.g., ml, tube, plate)
    custodian -- the custodian of the sample transaction （e.g., peter, linda)
    '''
    this_search = [sample_type, sample_ID, loc, status, Q, unit, custodian]
    while '' in this_search:
        this_search.remove('')

    search_all = view_logs()
    search_result = list()

    for each in search_all:
        this_sample = each[2]
        this_type = re.findall(r'type: "(.+?)"', this_sample)
        this_id = re.findall(r'id: "([^"]+)", status', this_sample)
        this_loc = each[4]
        this_status = re.findall(r'status: "([^"]+)", type', this_sample)
        this_q = re.findall(r'Qvar: (.+), Qvar_unit', this_sample)
        this_unit = re.findall(r'Qvar_unit: "([^"]+)", id', this_sample)
        this_who = each[0]
        this_all = [this_type[0][1:-1], this_id[0][1:-1], this_loc[1:-1], this_status[0][1:-1],
                    this_q[0][1:-1], this_unit[0][1:-1], this_who[1:-1]]

        if set(this_search) < set(this_all):
            search_result.append(each)
        else:
            continue

    return search_result

def get_time():
    '''
    Get the current time in 'date/month/year - hour:minute:second' format.
    '''
    now_time = time.strftime('%d/%m/%Y - %H:%M:%S',time.localtime(time.time()))
    return now_time

def ttttt():
    print('Yeah')



























