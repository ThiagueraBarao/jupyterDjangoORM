# List of Package functions

def QueryToJson(query,ParseJsonFlag = True):
    '''
    Returns JSON response from query requested.

            Parameters:
                    query (obj): Django ORM query. 
                    Examples: 
                        1. Model.objects.all()
                        2. Model.objects.filter(email='mail@mailprovider.com'))
                        3. Model.objects.filter(valor__gt=100))

                    ParseJsonFlag (Boolean): Bolean to mark Json parse option or not
                    
            Returns:
                    JSON response (str): Python String with JSON query response
    '''
    
    #Import Libraries
    import json
    from django.core import serializers
    
    #Serialize
    query_json = serializers.serialize('json', query)
    
    #Parse Json Flag
    if ParseJsonFlag == True:
        
        #Parse Json
        query_json_parse = json.loads(query_json)
        
        #Return
        return query_json_parse
    
    else:

        #Return
        return query_json

def ModelToPandasDf(query,interestField='fields',pkField='pk',idRename='ID'):
    '''
    Returns pandas dataframe from query requested.

            Parameters:
                    query (obj): Django ORM query. 
                        Examples: 
                            1. Model.objects.all()
                            2. Model.objects.filter(email='mail@mailprovider.com'))
                            3. Model.objects.filter(valor__gt=100))
                    interestField: Django response fields label
                    pkField (str): Django ID Label
                    idRename (str): DataFrame Index Label


            Returns:
                    Pandas DataFrame (obj): Pandas Dataframe response from query response
    '''
    
    #Import Libraries
    import pandas as pd
    import json
    
    # Django ORM Query Request
    queryToJson = QueryToJson(query)
    
    #Transform in first pandas dataframe
    queryToJsonPdDf = pd.DataFrame.from_records(queryToJson)
    
    #Get interest field
    queryToJsonPdDfInterestField = queryToJsonPdDf[interestField]
    
    #Transform to Fields DataFrame
    df = pd.DataFrame.from_records(queryToJsonPdDfInterestField)
    
    #Insert Index
    df[idRename] = queryToJsonPdDf[pkField]
    
    #Df Set Index
    df.set_index(idRename,inplace=True)
    
    #Return
    return df