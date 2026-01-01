def groceryList():

    item_list={}
    try:
        while True:
            item=input().upper()
            item_list[item]=item_list.get(item,0)+1

    except EOFError:
        item_list=dict(sorted(item_list.items()))
        return item_list


def main():
    item_list=groceryList()
    for key,value in item_list.items():
        print(f"{value} {key}")

if __name__=="__main__":
    main()

