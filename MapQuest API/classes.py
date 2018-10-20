## Mina Bedwany  ID - 69543570

### Classes


class STEPS:
    def print_thing(result:dict):
        print('DIRECTIONS')
        for item in result['route']['legs']:
            for i in item['maneuvers']:
                print(i['narrative'])
        print()


class TOTALDISTANCE:
    def print_thing(result:dict):
        for item in result['route']['legs']:
            print('TOTAL DISTANCE:', int(item['distance']//1), 'miles')
            print()



class TOTALTIME:
    def print_thing(result:dict):
        for item in result['route']['legs']:
            print('TOTAL TIME:', item['time']//60, 'minutes')
            print()



class LATLONG:
    def print_thing(result:dict):
        print('LATLONGS')
        for item in result['route']['locations']:
            if item['latLng']['lat']>0 and item['latLng']['lng']>0:
                print('{:.2f}{} {:.2f}{}'.format(item['latLng']['lat'],'N', item['latLng']['lng'], 'E'))
            elif item['latLng']['lat']<0 and item['latLng']['lng']<0:
                print('{:.2f}{} {:.2f}{}'.format(item['latLng']['lat']*-1,'S', item['latLng']['lng']*-1, 'W'))
            elif item['latLng']['lat']<0 and item['latLng']['lng']>0:
                print('{:.2f}{} {:.2f}{}'.format(item['latLng']['lat']*-1,'S', item['latLng']['lng'], 'E'))    
            elif item['latLng']['lat']>0 and item['latLng']['lng']<0:
                print('{:.2f}{} {:.2f}{}'.format(item['latLng']['lat'],'N', item['latLng']['lng']*-1, 'W'))
        print()



class ELEVATION:
    def print_thing(result:dict):
        print('ELEVATIONS')
        for item in result['elevationProfile']:
            print(item['height'])
        print()


