
def solution(string_data):
    data=string_data.split('@')
    price_dict={}
    volume_dict={}
    for i, item in enumerate(data):
        if i%3==0:
            code=item
            if not price_dict.get(code):
                price_dict[code]=[]
            if not volume_dict.get(code):
                volume_dict[code]=[]
        elif i%3==1:
            price_dict[code].append(eval(item))
        else:
            volume_dict[code].append(int(item))

    result=[]

    print(price_dict)

    for code in price_dict:
        min_price=min(price_dict[code])
        max_price=max(price_dict[code])
        new_price=price_dict[code][-1]
        
        total_value=0
        for price, volume in zip(price_dict[code], volume_dict[code]):
            total_value+=price*volume
        
        average_price=total_value/sum(volume_dict[code])

        result.append(code)
        result.append(str(min_price))
        result.append(str(max_price))
        result.append(str(new_price))
        result.append(f'{average_price:.2f}')
    return '@'.join(result)

if __name__ == "__main__":
    string_data='600006@24@1000@000001@26.3@2000@600006@25@1000'
    print(solution(string_data))
