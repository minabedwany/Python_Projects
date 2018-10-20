## Mina Bedwany  ID - 69543570


### main program module

import API
import classes

def Input():
    numlines = int(input())
    input_lines = []
    for i in range(numlines):
        input_lines.append(input())

    return input_lines

print(Input())
def output():
    numlines = int(input())
    output_lines = []
    for i in range(numlines):
        output_lines.append(input())

    return output_lines






#dictionary = {'STEPS': classes.STEPS(), 'TOTALDISTANCE': classes.TOTALDISTANCE, 'TOTALTIME': classes.TOTALTIME(), 'LATLONG': classes.LATLONG, 'ELEVATION': classes.ELEVATION}




def run_things(output: list):
    dictionary = {'STEPS': classes.STEPS, 'TOTALDISTANCE': classes.TOTALDISTANCE, 'TOTALTIME': classes.TOTALTIME, 'LATLONG': classes.LATLONG}
    dictionaryy = {'ELEVATION': classes.ELEVATION}
    try:
        for i in output:
            url = API.build_directions_url(inputs)
            Dict = API.get_result(url)
            urll = API.build_elevation_url(inputs)
            Dictt = API.get_result(urll)

            if i == 'ELEVATION':
                dictionaryy[i].print_thing(Dictt)
            else:
                dictionary[i].print_thing(Dict)
    except:
        print('NO ROUTE FOUND')
    else:
        print('Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors')    
        




if __name__=='__main__':
    inputs = Input()
    outputs = output()
    print()
    run_things(outputs)
    
    

    
