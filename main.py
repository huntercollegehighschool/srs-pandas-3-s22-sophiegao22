# 1. Import pandas
import pandas as pd

# 2. Read the "metacritic2.csv" file, and save the data in a dataframe variable. Print the data
metacritic = pd.read_csv('metacritic2.csv', index_col = 0)
print(metacritic)
print("\n")

# 3. Create a new dataframe with only Mario Games. Save that in a new dataframe variable and print that data (this will involve Boolean indexing)
mario = metacritic[metacritic.index.str.contains('mario', case = False)]
print(mario)
print("\n")


# 4. Sort the Mario data by release year in descending order. (a .sort_values() function exists)
mariosorted = mario.sort_values(by = ["Release Year"], ascending = False)
print(mariosorted)
print("\n")

# 5. Last time we used a loop to find individual data on different platforms, years, etc. There is a .groupby() function that exists as well. Let's start by grouping by Release Year. Run the following code:
# <var> = <dataframe>.groupby("Release Year").count()
# What does it seems like count presents?
mariogroupedrelyear = mario.groupby("Release Year").count()
print(mariogroupedrelyear)
print("\n")

# 6. Use groupby again, but this time on Platform. Afterwards, run .count(), .mean(), and .median(). Which platform looks like it has the best games?
mariogroupedplatform = mario.groupby("Platform").count()
print(mariogroupedplatform)
print("\n")

print("count:")
countplatformmario = mariogroupedplatform.count()
print(countplatformmario)
print("mean:")
meanplatformmario = mariogroupedplatform.mean()
print(meanplatformmario)
print("median:")
medianplatformmario = mariogroupedplatform.median()
print(medianplatformmario)


# 7. Create a new dataframe from the HunterAMC.csv file.
amc = pd.read_csv('HunterAMC.csv', sep = "\t")
print(amc)

# 8. In that csv, contest 0 is the AMC 10, and contest 2 is the AMC 12. Create two separate dataframes containing data from the two different contests.
amc10 = amc[amc["contest"].between(-1, 1)]
print(amc10)
amc12 = amc[amc["contest"].between(1, 3)]
print(amc12)

# 9. Find the average scores for each contest.
amc10scores = amc10["TotalScore"]

meanamc10 = amc10scores.mean()
print("mean for amc10:")
print(meanamc10)

amc12scores = amc12["TotalScore"]
meanamc12 = amc12scores.mean()
print("mean for amc12:")
print(meanamc12)
print("\n")
# 10. For each column, count how often each answer choice was selected.
answerchoices = amc[amc.columns[[6,7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]]]
for column in answerchoices:
  print(column)
  print(answerchoices[column].value_counts())
  print("\n")