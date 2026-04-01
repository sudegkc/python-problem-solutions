def readFile(fileName):
    data=dict()
    most_ordered_num=0
    most_ordered_item=""
    item_totals=dict()
    try:
        with open(fileName,"r") as inf:
            for line in inf:
                parts=line.strip().split()
                name=parts[0].capitalize()
                item=parts[1]
                try:
                    quantity=int(parts[2])
                except ValueError:
                    continue

                if name not in data:
                    data[name]={
                        "item":{},
                        "quantity":0
                    }
                
                if item not in data[name]["item"]:
                    data[name]["item"][item]=quantity
                else:
                    data[name]["item"][item]+=quantity

                data[name]["quantity"] +=quantity
                
                if item not in item_totals:
                    item_totals[item]=quantity
                else:
                    item_totals[item]+=quantity

                for item in item_totals:
                    if item_totals[item] > most_ordered_num:
                        most_ordered_num=item_totals[item]
                        most_ordered_item=item
    
    except OSError:
        exit("error opening the file.")
    return data, most_ordered_num,most_ordered_item

def main():

    data, most_ordered_val, most_ordered_item =readFile("orders.log")
    print("CUSTOMERS: ")
    for name in data:
        print(f"{name}:  ITEMS = {len(data[name]["item"])} TOTAL = {data[name]["quantity"]}")

    print(f"MOST ORDERED ITEM: {most_ordered_item} ({most_ordered_val})")

main()