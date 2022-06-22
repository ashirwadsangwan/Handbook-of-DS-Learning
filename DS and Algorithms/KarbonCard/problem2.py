'''
Want to query an API endpoint to receive data about apartment listings from a rental website

- num_bedrooms==1 : '1-bedroom' apartment
- num_bedrooms==0: 'studio' apartment

- Only two kind of apartments available

Problem: 
    - Wrong tagging of apartments : studio <> 1-bedroom
    - Why? : Issue with one of the data fields, description -- Parsing Issue


'''
import pandas as pd

def num_bedroom_bugfix(json_data):
    df = pd.DataFrame(json_data)
    for j, desc in enumerate(df.description):
        desc = desc.lower()
        desc = desc.split()
        

        
        for i, word in enumerate(desc):
            if word=='art' or word=='yoga' or word=='dance':

                desc.remove(desc[i+1])          
                
        if 'studio' in desc:

            if df.num_bedrooms[j]!=0:
                df['num_bedrooms'][j]=0

        elif '1-bedroom' in desc:
            if df.num_bedrooms[j]!=1:
                df['num_bedrooms'][j]=0
    return df


## TEST

if __name__ == '__main__':
    json_data =([
                
                {'id': '1',
                'agent': 'Radulf Katlego',
                'unit': '#3',
                'description': 'This luxurious studio apartment is in the heart of downtown.',
                'num_bedrooms': 1},
                {'id': '2',
                'agent': "Kelemen Konrad&quot",
                'unit': '#36',
                'description': 'We have a 1-bedroom available on the third floor.',
                'num_bedrooms': 1},
                {'id': '3',
                'agent': 'Tonn Jett',
                'unit': '#12',
                'description': 'Beautiful 1-bedroom apartment with nearby yoga studio.',
                'num_bedrooms': 1},
                {'id': '4',
                'agent': 'Fishel Salman',
                'unit': '#13',
                'description': 'Beautiful studio with a nearby art studio.',
                'num_bedrooms': 1}
            ])
    print(num_bedroom_bugfix(json_data))
    