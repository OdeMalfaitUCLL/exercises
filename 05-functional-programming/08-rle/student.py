def rle_encode(data):
    li = iter(data)

    try:
        last_data = next(li)
        count = 1
        for x in li:
            if x == last_data:
                count+=1
            else: 
                yield (last_data,count)
                last_data = x
                count = 1
        yield (last_data,count)
    except StopIteration:
        pass
    

def rle_decode(data):
    print(f"datum = {data}")
    for datum, count in data:
        for _ in range(count):
            yield datum


data = "aabbbc"
new_data=[]
decoded_data=[]
gen_encode = rle_encode(data)
# one =next(gen_encode)
# two =next(gen_encode)
# three =next(gen_encode)
# new_data.append(one)
# new_data.append(two)
# new_data.append(three)
# print(new_data)
gen_decode= rle_decode(gen_encode)
dec_one =next(gen_decode)
dec_two = next(gen_decode)
dec_three = next(gen_decode)
dec_four = next(gen_decode)
dec_five = next(gen_decode)
dec_six = next(gen_decode)
decoded_data.append(dec_one)
decoded_data.append(dec_two)
decoded_data.append(dec_three)
decoded_data.append(dec_four)
decoded_data.append(dec_five)
decoded_data.append(dec_six)
print(decoded_data)



