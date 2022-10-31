import random
import pandas as pd



def regulisi_cs115(podaci):

    vrednost = podaci['cs_115_ocena']
    
    if( 8<= podaci['cs_101_ocena'] <=10):
        vrednost=vrednost+1

        print('jeste cs101 izmedju 8 i 10', vrednost)

    if(13<=podaci['cs_115_izostanci']<=15):
        vrednost=vrednost-2
    elif(5<=podaci['cs_115_izostanci']<=12):
        vrednost=vrednost-1
    
    if(9<= podaci['ma_101_ocena'] <=10 ):
        vrednost=vrednost+1

    print(podaci)

    if(vrednost<=5):
        vrednost=5
        podaci['cs_115_polozen']=0

    if(vrednost>10):vrednost=10

    

    podaci['cs_115_ocena'] = vrednost

    print(podaci)

    return podaci

def generisi_red():

    generisani_podaci = dict()

    generisani_podaci['cs_101_ocena']= random.randint(5,10)
    generisani_podaci['it_101_ocena']= random.randint(5,10)
    generisani_podaci['ma_101_ocena']= random.randint(5,10)
    generisani_podaci['cs_115_izostanci'] = random.randint(0,15)
    generisani_podaci['cs_115_ocena'] = random.randint(5,10)

    
    if(generisani_podaci['cs_115_ocena']>5):
        generisani_podaci['cs_115_polozen'] = 1
    else:
        generisani_podaci['cs_115_polozen'] = 0


    generisani_podaci = regulisi_cs115(generisani_podaci)

    return generisani_podaci






def generisi_df(broj_redova):

    lista = []

    for i in range(0,broj_redova):
        red = generisi_red()
        lista.append(red)

    df = pd.DataFrame(lista)
    print(df)

    return df


def sacuvaj_kao_csv(df):
    df.to_csv('generisani_podaci.csv', index=False, encoding='utf-8')

df = generisi_df(800)

sacuvaj_kao_csv(df)
