import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    
    race_count = pd.Series(df["race"].value_counts())

    # What is the average age of men?
    average_age_men = df.loc[(df["sex"] == "Male"), "age"].mean().round(decimals=1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(len(df.loc[df["education"] == "Bachelors"]) / len(df.education)  * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    earnings_high = df["salary"].isin([">50K"])
    higher_education = df["education"].isin(["Bachelors", "Masters","Doctorate"])

    # values = ["Bachelors", "Masters", "Doctorate"]
    no_educated = df.loc[(df["education"] != "Bachelors") & (df["education"] != "Masters") & (df["education"] != "Doctorate")]
    lower_education = df.loc[(df["education"] != "Bachelors") & (df["education"] != "Masters") & (df["education"] != "Doctorate") & (df["salary"] == ">50K")].shape[0]

    # percentage with salary >50K
    higher_education_rich = round(df[higher_education & earnings_high].shape[0] / df[higher_education].shape[0] * 100, 1)
  
    lower_education_rich = round(lower_education / len(no_educated) * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df["hours-per-week"].min()
    
    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    working_min = df.loc[df["hours-per-week"] == min_work_hours]
    num_min_workers = (df.loc[(df["hours-per-week"] == min_work_hours) & (df["salary"] == ">50K")]).shape[0]

    rich_percentage =  round(num_min_workers / len(working_min) * 100)

    # What country has the highest percentage of people that earn >50K?
    highest_country = df.loc[(df["salary"] == ">50K"), "native-country"].value_counts()
    map_key = df.groupby(df["native-country"]).size().to_dict()
    highest_country1 = pd.DataFrame(highest_country)
  
    highest_country1["total"] = highest_country1.index.map(map_key)
    highest_country1["percentage"] = (highest_country1["native-country"]).astype(float) / (highest_country1.total).astype(float)
  
    highest_earning_country = highest_country1["percentage"].idxmax()
    highest_earning_country_percentage =  round(highest_country1["percentage"].max() * 100, 1 )

    # Identify the most popular occupation for those who earn >50K in India.
    occupation = df.loc[(df["salary"] == ">50K") & (df["native-country"] == "India"), "occupation"].value_counts()
    occupation1 = pd.DataFrame(occupation)
    top_IN_occupation = occupation1.index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
