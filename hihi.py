i=1
count=0
total=0
def CarParking(start_h,start_m,end_h,end_m):
    start = start_h*60 + start_m
    end = end_h*60 + end_m
    if (end - start)%10 ==0:
        charge =(end-start)/10*500
    else:
        charge =((end-start)//10+1)*500
    return charge



while 1:
    start_h,start_m = input('%s번 차량 주차 시작 시각(시 분):' %str(i)).split()
    end_h,end_m = input('%s번 차량 주차 종료 시각(시 분):' %str(i)).split()
    i+=1
    start_h= int(start_h)
    start_m= int(start_m)
    end_h=int(end_h)
    end_m=int(end_m)

    print('주차요금: %d원' %CarParking(start_h,start_m,end_h,end_m))
    count +=1
    total +=CarParking(start_h,start_m,end_h,end_m)
    
    q =input('더 입력하시겠습니까?(Y/N):')
    if q == 'N': break
    
print('주차차량 %d대의 총 주차 요금은 %d원입니다.' %(count, total)   )