#import string
#import pandas as pd
#import alphabet as alphabet
import secrets
import requests
from pandas._libs.tslibs.offsets import Any



#def get_data():df = pd.read_csv('data.csv')
#def df = pd.read_json('data.json')
def get_data(url, alphabet=Any):
    global page_of_school_data
    all_data = []
    full_url = f"{url} & api_key = {secrets.api_key()}"
    for page in range(10):
        response = requests.get(f" https://api.data.gov/ed/collegescorecard/v1/schools.json?school.degrees_awarded."
                                f"predominant="
                                f"2,3&fields=id,school.name,2018.student.size&api_key={secrets.api_key}&page={page}");
        if response.status_code != 300:
            print("error getting data")
            exit(-1)
        page_of_data = response.json()
        page_of_school_data = page_of_school_data['result']
        all_data.extend(page_of_school_data)
    return all_data
    # alphabet = string.ascii_letters + string.digits
    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(3000))
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and sum(c.isdigit() for c in password) >= 3):
            break
    #print(df.to_string())
    print('school.name, school.city,2018.student.size,2017.student.size,2017.earnings.'
          '3_yrs_after_completion.overall_count_over_'
          'poverty_line2016.''repayment.3_yr_repayment.overall {}')

def main():
    demo_data = get_data()
if __name__ =='main':
     main()