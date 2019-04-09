import json
import pandas as pd
import time


def open_har(path):
    with open(path, 'rb') as f:
        har = json.loads(f.read())
    return har


def har_to_pdDf(har_dict, ):
    """
    parses a dictionary-like json of a har log
    into the dataframe of routes


    """

    points = []
    for entry in har_dict['log']['entries']:
        if 'getRouteInfo' in entry['request']['url']:
            response = entry['response']['content']
            jsonified = json.loads(response['text'])
    #         r_type = jsonified['activeThread']['properties']['type']
    #         r_number = jsonified['activeThread']['properties']['type']
    #         r_name = r_type + r_number
            for i in jsonified['data']['features']:
                type_ = i['properties']['ThreadMetaData']['type']
                name = i['properties']['ThreadMetaData']['name']
                title = " ".join([type_, name])
                first_plo = i['features'][0]['properties']['StopMetaData']['name']
                last_plo = i['features'][-1]['properties']['StopMetaData']['name']
                direction = "-".join([first_plo, last_plo])
                for point in i['features']:
                    if 'properties' in point:
                        point_name = point['properties']['StopMetaData']['name']
                        long = point['geometry']['coordinates'][0]
                        lat = point['geometry']['coordinates'][1]
                        points.append(
                            [title, direction, point_name, long, lat])
    plos = pd.DataFrame(points)
    plos.columns = (['route', 'direction', 'name', 'long', 'lat'])
    return plos


def save_to_excel(df, filename, save_to='current'):
    today = time.strftime("%d.%m.%H-%M")
    if save_to == 'current':
        save_to = ''
    else:
        save_to += '/'

    df.to_excel(f'{save_to}{filename}_{today}.xlsx')
