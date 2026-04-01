def read_token(fileName):
    tokens=dict()
    try:
        with open(fileName,"r") as inf:
            inf.readline()
            for line in inf :
                line=line.strip()
                if not line:
                    continue
                parts=line.split(";")
                token=parts[0]
                try:
                    quantity=float(parts[1])
                except ValueError:
                    continue
                tokens[token]=quantity

    except OSError:
        exit("error opening the file.")
    return tokens

def read_token_prices(fileName):
    data=dict()
    try:
        with open(fileName,"r") as inf:
            inf.readline()
            for line in inf:
                line=line.strip()
                if not line:
                    continue
                parts=line.split(";")
                date=parts[0]
                token=parts[1]
                try:
                    price=float(parts[2])
                except ValueError:
                    continue
                if date not in data:
                    data[date]={}
                
                data[date][token]=price
    except OSError:
        exit("error opening the file.")
    return data


def main():
    tokens=read_token("token.csv")
    data=read_token_prices("token_prices.csv")
    
    total_day=len(data)
    print("Number of days: ",total_day)

    print(f"{'Date':<18} Value (USD)")

    max_val=0.0
    max_date=""
    for date in sorted(data.keys()):
        current_tot=0.0

        for token,quantity in tokens.items():
            if token in data[date]:
                price=data[date][token]
                current_tot=price*quantity

        print(f"{date:<18} {current_tot:.2f}")

        if current_tot>max_val:
            max_val=current_tot
            max_date=date
    print("Date of maximum values",max_date,", value: ",max_val)

            


if __name__=="__main__":
    main()