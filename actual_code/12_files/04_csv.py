import csv

with open("sample.csv", mode="a") as file:  # log file ... be in append
    writer = csv.writer(file)
    writer.writerow(["Wicked", 2024])
    writer.writerow(["Matrix", 1998])
    writer.writerow(["Forest Gump", 1990])

with open("sample1.csv", mode="w") as file:  # outputting a report
    fieldnames = ["title", "release_year"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"title": "Wick$ed", "release_year": 2024, "rating": 4})
    writer.writerow({"title":"Mat$rix", "release_year":1998})
    writer.writerow({"title":"Fores$t Gump", "release_year":1990})

with open("sample.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        print(f"{row[0]} was made in {row[1]}")

with open("sample1.cleaned.csv", "w") as cleaned:
    with open("sample1.csv") as file:
        reader = csv.DictReader(file)
        writer = csv.DictWriter(cleaned, fieldnames=["title", "release_year"])
        writer.writeheader()
        for row in reader:
            if int(row["release_year"]) < 2000:
                row['title'] = row['title'].replace("$", "")
                writer.writerow(row)