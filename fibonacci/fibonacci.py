# iteration
def fibonacci(num):
    preVal = 0
    val    = 1
    fiboList = [preVal, val]
    for n in range(1,num):
        tmp = val+preVal
        fiboList.append(tmp)

        # update preVal
        preVal = val
        val    = tmp
    
    return fiboList

# recursive time
result = None
def fiboRecurive(num, idx, preVal, val): 
    '''
    [初始資料][當下資料+呼叫recursive回傳的資料]...[當下資料+呼叫recursive回傳"最後"的資料]
    ^^^^^^^^ ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
       (1)                (2)                                  (3)

    Recursive的設計可分為:
    - (1)初始: 定義好初始資料的狀態+next過程
    - (2)過程: 當下的資料+next過程
    - (3)最後: 傳回最後一個資料, 與上一個過程拼接, 一路傳回去
    以下針對這幾個來設計程式
    '''
    # (1)初始
    if idx==0:
        return [preVal, val]+ fiboRecurive(num,idx+1,preVal=val, val=preVal+val)
    # (3)最後
    elif idx == num:
        return [val] #<--把最後一個
    # (2)過程
    else:
        return [val] + fiboRecurive(num,idx+1,preVal=val, val=preVal+val)
    #          ^^^^^   ^^^^^^^^^^^^
    #          (1)          (2)
    # 設計理念: [val]: val原本是當下的值, 在呼叫fiboRecurive的當下, val就會變成preVal, 
    # 與(2)fiboRecurive的結果做組合, 成為新的[preVal,val]
    

from time import time

# test 10 num
num=10

# test fibo iteration
print('=== test fibo iteration ===')
tStart = time()
result = fibonacci(num)
tEnd = time()
print('result={}, time={}'.format(result,(tEnd-tStart)))



# test fibo recursive
print('=== test fibo recursive ===')
tStart = time()
result = fiboRecurive(num,0,preVal=0, val=1)
tEnd = time()
print('result={}, time={}'.format(result,(tEnd-tStart)))


