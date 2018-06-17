def getListYears():
    listYears = [{'label': i, 'value': i} for i in     [2009,2010,2011,2012,2013,2014,2015]]
    return listYears
    
def getListColumns():
    listColumns = [{'label': i, 'value': i} for i in ['longitude', 'latitude',
       'Number of Vehicles', 'Accident Date', 'Time (24hr)', '1st Road Class',
       'Road Surface', 'Lighting Conditions', 'Weather Conditions',
       'Casualty Class', 'Casualty Severity', 'Sex of Casualty',
       'Age of Casualty', 'Type of Vehicle']]
    return listColumns