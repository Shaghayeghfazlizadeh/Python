mylist = [1, 3,  2, 8, 4, 8, 5, 8, 6, 7, 8]
element_to_remove = 8
count_removed = 0

while element_to_remove in mylist:
    mylist.remove(element_to_remove)
    count_removed += 1

print("لیست بعد از حذف:", mylist)
print("تعداد عنصر های حذفی :", count_removed)
