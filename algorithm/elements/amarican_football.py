def num_pos(score, l = []):
   
    if score == 0:
        #print('score: {}, {}'.format(score, num_methods))
        #num_methods += 1 
        print(l)
        return True
    if score < 0 or score == 1:
        #print('score: {}, {}'.format(score, num_methods))
        return False
    
    num_methods=0
    #l = []
    for number in [2, 3, 7]:
        #print('score: {}, number: {} num_methods: {}'.format(score, number, num_methods))
        if len(l) == 0:
            l.append(score)
        l.append(score-number)
        num_methods += num_pos(score-number, l=l)        
        
    return num_methods

if __name__ == '__main__':
    print(num_pos(7))
    #print(num_methods)