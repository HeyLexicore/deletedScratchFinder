from concurrent.futures import ThreadPoolExecutor, as_completed


def daemon(func, data, drange):
    result = []

    for i in drange:
        try:    
            result.append(func(data[i]))
        finally:
            pass
    return result,drange


def process(data, func, threads):
    if threads == 0:
        threads = len(data)

    oriLen = len(data)

    calcuLen = (int(oriLen/threads)+1)*threads

    step = int(oriLen/threads)

    with ThreadPoolExecutor(max_workers=threads) as executor:

        futures = []
        for i in range(0,int(calcuLen/step)):
            #print(i)
            front = i*step
            back = i*step+step
            if i*step+step > oriLen:
                futures.append(executor.submit(daemon, func, data, range(front, oriLen)))
            else:
                futures.append(executor.submit(daemon, func, data, range(front, back)))
        #print(len(futures))
        for future in as_completed(futures):

            info, drange = future.result()
            #print(info,drange)
            for d,i in zip(info,drange):

                data[i] = d
    return data
