import sys
newList = sys.argv
newList.pop(0)

for index, item in enumerate(newList, start=1):
    string_to_print = f"{index}.{item}"
    print(string_to_print)