def square_each(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2


def sum_list(nums):
    total=0
    for i in range(len(nums)):
        total+=nums[i]
    return total

def to_numbers(str_list):

    for i in range(len(str_list)):
        try:
            str_list[i] = float(str_list[i])
        except:
            pass



def main():
    filename = input('Please enter the file name: ')
  str_list=[]
    with open(filename,'r') as infile:
        for line in infile.readlines():
            if ',' in line:
                line = line.strip().split(',')
            else:
                line = line.strip().split()
            for val in line: str_list.append(val.strip())

    to_numbers(str_list)
    square_each(str_list)
    total = sum_list(str_list)
    print('The sum of the squares of the numbers in the file is {}'.format(total))

main()