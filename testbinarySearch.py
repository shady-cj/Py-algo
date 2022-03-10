import getpass

def binary_search_rotation(lo, hi, condition):
    while lo <= hi:
        mid = (lo+hi) // 2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        elif result == 'right':
            lo = mid + 1
    return -1

def count_rotations_generic(nums):
    hi = len(nums)-1
    lo = 0
    def condition(mid):
        nonlocal hi
        nonlocal lo
        # print(mid)
        # print(nums)
        
        # print("in here")
        if mid > 0 and nums[mid] < nums[mid-1]:
            return "found"
        elif mid > 0 and nums[mid] >= nums[mid-1]:
            if nums[mid] < nums[hi]:
                hi = mid - 1
                return "left"
            else:
                lo = mid +1 
                return "right"
        else:
            hi = mid - 1
            return "left"

    return binary_search_rotation(0,len(nums)-1,condition)


def evaluate_test_case(test_function, tests):
    num = 0
    passed = 0
    failed = 0
    for test in tests:
        print(test['input']['nums'])
        
        if test['output'] == test_function(test['input']['nums']):
            print(f'##### Test Case {num} #####')
            print('STATUS: PASSED')
            
            passed +=1
        else:
            print(f'##### Test Case {num} #####')
            print('STATUS: FAILED')
            failed += 1
        print("Expected Output: ",test['output'])
        print("Output: ",test_function(test['input']['nums']),"\n \n \n")
        num += 1
    
    return f'*******Test Result*******\n Total:{num}\n Passed:{passed}\n Failed:{failed}'




test0 = {
    'input': {
        'nums': [19, 25, 29, 3, 5, 6, 7, 9, 11, 14]
    },
    'output': 3
}

# A list of size 8 rotated 5 times.
test1 = {
    'input': {
        'nums': [4,5,6,7,8,1,2,3]
    },
    'output': 5
}
# A list that wasn't rotated at all.
test2 = {
    'input': {
        'nums': [10,12,45,50,100,550,1234,2000]
    },
    'output': -1
}

# A list that was rotated just once.
test3 = {
    'input': {
        'nums': [2000, 20,45,64,355,503,708]
    },
    'output': 1
}

# A list that was rotated n-1 times, where n is the size of the list.
test4 = {
    'input': {
        'nums': [20,42,52,56,345,635,823,5634,6452,4]
    },
    'output': 9
}
# A list that was rotated n times, where n is the size of the list
test5 = {
    'input': {
        'nums': [23,42,43,45,62,66,72,76,86,132]
    },
    'output': -1
}
# An empty list.
test6 = {
    'input': {
        'nums': []
    },
    'output': -1
}
# A list containing just one element.
test7 = {
    'input': {
        'nums': [4]
    },
    'output': -1
}

test8={
     'input': {
        'nums': [14,20,4,5,6,6,6,7,7,8,10]
    },
    'output': 2
}
test9 = {
     'input': {
        'nums': [14,20,4,5,6,6,7,7,8,10]
    },
    'output': 2
}

test10 = {
     'input': {
        'nums': [20,20,20,1,2,5,7,13,19]
    },
    'output': 3
}

test11 = {
     'input': {
        'nums': [20,20]
    },
    'output': -1
}

test12 = {
     'input': {
        'nums': [40,51,1,3,6,9,14,18,20,20]
    },
    'output': 2
}


tests = [test0, test1, test2,test3, test4, test5, test6, test7, test8,test9, test10,test11, test12]

if __name__ == '__main__':
    print('Initiating program')
    password = getpass.getpass(prompt="Enter Your Password \n")

    if password == 'ceejay':
        print("Access Granted")
        print(evaluate_test_case(count_rotations_generic, tests))
    else:
        print('Wrong Credentials')