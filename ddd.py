character = {
    'name': '기사',
    'level':'12',
    'items':{
        'sword':'불꽃의 검',
        'armor':'풀풀레이트'
    },
    'skill':['베기1','베기2','베기3']
}
for key in character:
    if type(character[key]) is dict:
        for k in character[key]:
            print('{}:{}'.format(k,character[key][k]))
    elif type(character[key]) is list:
        for i in character[key]:
            print('{}:{}'.format(key,i))
    else:
         print('{}:{}'.format(key,character[key]))