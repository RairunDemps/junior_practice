first_list = ["hi", "hello", "doni", "rafaelo",
              "leo", "mike", "hamsta"]
print(first_list)

sorted_first_list = sorted(first_list)
print(sorted_first_list)

first_list.sort(reverse=True)
print(first_list)

second_list = [item.replace("h", "n") for item in first_list if "h" in item]
print(second_list)

range_test = [str(i) for i in range(-10, 0, 2)]
print(range_test)

xrange_test = [str(i) for i in range(-10, 0, 2)]
print(xrange_test)

def special_replace(x):
    return x.replace("a", "e")

map_list = map(special_replace, first_list)
print(list(map_list))

xrange_sum_test = [i for i in range(-10, 0, 5)]
print(sum(xrange_sum_test, start=0))

enumerate_test = [x for x in enumerate(first_list)]
print(enumerate_test)

zip_list = list(zip(first_list, [i for i in range(0, len(first_list))]))
print(zip_list)
