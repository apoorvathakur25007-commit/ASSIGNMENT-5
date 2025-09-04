og_list=[]
for i in range(1,11):
    og_list.append(i)
ext_list=og_list[:5]
rev_list=ext_list[::-1]
print(f"Original list: {og_list}")
print(f"Extracted first five elements: {ext_list}")
print(f"Reversed extracted elements: {rev_list}")