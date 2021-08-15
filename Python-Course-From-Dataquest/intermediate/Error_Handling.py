## 2. Sets ##


gender = []
for item in legislators:
    gender.append(item[3])

gender = set(gender)
print(gender)

## 3. Exploring the Dataset ##


party = []
for item in legislators:
    party.append(item[6])

party = set(party)
print(party)

print(legislators)

## 4. Missing Values ##


for row in legislators:
    if row[3] == "":
        row[3] = "M"

## 5. Parsing Birth Years ##


birth_years = []
for row in legislators:
    birthday = row[2]
    parts = birthday.split("-")
    birth_years.append(parts[0])

## 6. Try/except Blocks ##


try:
    float("hello")
except Exception:
    print("Error converting to float.")

## 7. Exception Instances ##


try:
    int('')
except Exception as exc:
    print(type(exc))
    print(str(exc))

## 8. The Pass Keyword ##

converted_years = []
for year in birth_years:
    try:
        int_year = int(year)
        converted_years.append(int_year)
    except Exception:
        pass

## 9. Convert Birth Years to Integers ##


for row in legislators:
    birthday = row[2]
    birth_year = birthday.split("-")[0]
    try:
        birth_year = int(birth_year)
    except Exception:
        birth_year = 0
    row.append(birth_year)

## 10. Fill in Years Without a Value ##


last_value = 1
for row in legislators:
    if row[7] == 0:
        row[7] = last_value
    last_value = row[7]
