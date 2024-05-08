


lower_bound = 1
upper_bound = 9

values = []
events = []


def parse_data():
    with open("data.csv", "r") as f:
        data = f.readlines()
        for line in data:
            time, value = line.split(',')
            values.append(int(value))
            if int(value) < lower_bound or int(value) > upper_bound:
                events.append(int(time))
                
def write_data():
    with open("output.csv", "w") as f:
        current = 0
        for i in events:
            if i != current:
                average = sum(values[current:i]) / len(values[current:i]) if len(values[current:i]) > 0 else 1
                f.write(f"[{current} -> {i - 1}], {average}\n")
                f.write(f"{i}, {values[i]}\n")
                current = i
           
def main():
    parse_data()
    write_data()
    
if __name__ == "__main__":
    main()
