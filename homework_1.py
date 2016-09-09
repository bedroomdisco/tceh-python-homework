while True:

# yes/no questions:

    q1 = input ('is everything an object in python (yes/no): ')
    q2 = input ('is 1 treated as a true value (yes/no): ')
    array_yn = [q1,q2] #array for yes/no questions
    index_yn = 0
    for i in array_yn:
        if i == 'yes':
            array_yn[index_yn] = 1
        elif i == 'Yes':
            array_yn[index_yn] = 1
        else:
            array_yn[index_yn] =0
        index_yn = index_yn + 1 #index for yes/no questions
    q1 = array_yn[0]
    q2 = array_yn[1] 


# String-type calculations:

    q3 = input ('123+456 as a string:')
    if q3 == '123456':
         q3 = 1
    else:
         q3 = 0


# Math:

    q4 = input ('4 // 3:')
    q4 = int(q4)
    

# Boolean calculations: 

    q5 = input ('True or False (executed as bool):')
    if q5 == 'True':
        q5 = 1
    elif q5 == 'true':
        q5 = 1
    else:
        q5 = 0
    

    
    array = [q1,q2,q3,q4,q5]
    index = 1
    correct = 0
    for i in array:
        if i == 1:
            print ('answer%.d is correct' % index)
            correct = correct + 1
        else:
            print ('answer%.d is incorrect' % index)
        index = index+1
    print ('number of correct answers:', correct)
    break    
