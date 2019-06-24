#Imports
import pandas as pd 

PATH = '/Users/jesusreyes/Google Drive/fake_news_resources/raw_data/'

if __name__ == '__main__':

    NU = pd.read_json(PATH + 'nacion_unida.json')
    HM = pd.read_csv(PATH + 'heraldo_test.csv')

    print('Nación unida sample size: %s' %(NU.shape[0]))
    print('Heraldo sample size: %s' %(HM.shape[0]))
    print(HM.head())

    