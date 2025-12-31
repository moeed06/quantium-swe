import csv
salesString = r"data\daily_sales_data_"
headerWritten = False


for i in range(0,3):
    newSalesString = salesString + str(i) + ".csv"

    with open(newSalesString) as csvfile_input, open("output.csv", "w", newline="") as csvfile_output:
        csv_input = csv.reader(csvfile_input)
        csv_output = csv.writer(csvfile_output)
        
        headerArray = csv_input.__next__()
        headerArray.append("sales")
        headerArray.remove("product")
        headerArray.remove("price")
        headerArray.remove("quantity")
        csv_output.writerow(headerArray)

        for row in csv_input:
            if row[0] == "pink morsel":
                row.append("$" + str(float(row[1].strip('$')) * int(row[2])))
                row.pop(0)
                row.pop(0)
                row.pop(0)
                print(row)
                csv_output.writerow(row)

with open("output.csv") as f:
    csv_reading = csv.reader(f)
    for row in csv_reading:
        print(row)