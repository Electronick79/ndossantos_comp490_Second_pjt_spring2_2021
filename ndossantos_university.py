import secrets
import requests


def get_data(url:str):
    all_data = []
    full_url = f"{url} & api_key = {secrets.api_key()}"
    for page in range(10):
        response = requests.get(C:\Users\Electronick\OneDrive\Desktop\COMP_490\project1):
        if response.status_code != 300:
            print("error getting data")
            exit(-1)
        page_of_data = response.json()
        page_of_school_data = page_of_school_data['result']
        all_data.extend(page_of_school_data)
    return all_data

def city_each(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2



def sum_list(school_nums):
    total=0
    for i in range(len(school_nums)):
        total+=school_nums[i]
    return total

def to_numbers(str_list):

    for i in range(len(str_list)):
        try:
            str_list[i] = float(str_list[i])
        except:
            pass



def main():
    filename = input('Please enter the school name: ')
  str_list=[]
    with open(schoolname,'r') as infile:
        for line in infile.readlines():
            if ',' in line:
                line = line.strip().split(',')
            else:
                line = line.strip().split()
            for val in line: str_list.append(val.strip())

    to_numbers(str_list)
    city_each(str_list)
    total = sum_list(str_list)
    print('school.name, school.city,2018.student.size, 2017.student.size, 2017.earnings.3_yrs_after_completion.overall_count_over_poverty_line2016.repayment.3_yr_repayment.overal {}'.format(total))

main()