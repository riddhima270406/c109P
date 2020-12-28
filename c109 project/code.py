import pandas as pd
import statistics
import csv

df = pd.read_csv("data.csv")

gender_list = df['Gender'].to_list()
race_list = df["Race/Ethnicity"].to_list()
parentedu_list = df["Parental level of Education"].to_list()
course_list = df["Test Preparation Course"].to_list()
lunch_list = df["Lunch"].to_list()
math_list = df['Math Score'].to_list()
reading_list = df["Reading Score"].to_list()
writing_list = df["Writing Score"].to_list()

math_mean = statistics.mean(math_list)
reading_mean = statistics.mean(reading_list)
writing_mean = statistics.mean(writing_list)

math_median = statistics.median(math_list)
reading_median = statistics.median(reading_list)
writing_median = statistics.median(writing_list)

math_mode = statistics.mode(math_list)
reading_mode = statistics.mode(reading_list)
writing_mode = statistics.mode(writing_list)

print("Mean of MATHS SCORE is {}")
print("Mode of MATHS SCORE is {}")
print("Median of MATHS SCORE is {}")

print("Mean of WRITING SCORE is {}")
print("Mode of WRITING SCORE is {}")
print("Median of WRITING SCORE is {}")

print("Mean of READING SCORE is {}")
print("Mode of READING SCORE is {}")
print("Median of READING SCORE is {}")
  
math_std_deviation = statistics.stdev(math_list)
reading_std_deviation = statistics.stdev(reading_list)
writing_std_deviation = statistics.stdev(writing_list)

math_first_std_deviation_start, math_first_std_deviation_end = math_mean-math_std_deviation, math_mean+math_std_deviation
math_second_std_deviation_start, math_second_std_deviation_end = math_mean-(2*math_std_deviation), math_mean+(2*math_std_deviation)
math_third_std_deviation_start, math_third_std_deviation_end = math_mean-(3*math_std_deviation), math_mean+(3*math_std_deviation)

reading_first_std_deviation_start, reading_first_std_deviation_end = reading_mean-reading_std_deviation, reading_mean+reading_std_deviation
reading_second_std_deviation_start, reading_second_std_deviation_end = reading_mean-(2*reading_std_deviation), reading_mean+(2*reading_std_deviation)
reading_third_std_deviation_start, reading_third_std_deviation_end = reading_mean-(3*reading_std_deviation), reading_mean+(3*reading_std_deviation)

writing_first_std_deviation_start, writing_first_std_deviation_end = writing_mean-writing_std_deviation, writing_mean+writing_std_deviation
writing_second_std_deviation_start, writing_second_std_deviation_end = writing_mean-(2*writing_std_deviation), writing_mean+(2*writing_std_deviation)
writing_third_std_deviation_start, writing_third_std_deviation_end = writing_mean-(3*writing_std_deviation), writing_mean+(3*writing_std_deviation)

math_list_of_data_1_std_deviation = [result for result in math_list if result > math_first_std_deviation_start and result < math_first_std_deviation_end]
math_list_of_data_2_std_deviation = [result for result in math_list if result > math_second_std_deviation_start and result < math_second_std_deviation_end]
math_list_of_data_3_std_deviation = [result for result in math_list if result > math_third_std_deviation_start and result < math_third_std_deviation_end]

reading_list_of_data_1_std_deviation = [result for result in reading_list if result > reading_first_std_deviation_start and result < reading_first_std_deviation_end]
reading_list_of_data_2_std_deviation = [result for result in reading_list if result > reading_second_std_deviation_start and result < reading_second_std_deviation_end]
reading_list_of_data_3_std_deviation = [result for result in reading_list if result > reading_third_std_deviation_start and result < reading_third_std_deviation_end]

writing_list_of_data_1_std_deviation = [result for result in writing_list if result > writing_first_std_deviation_start and result < writing_first_std_deviation_end]
writing_list_of_data_2_std_deviation = [result for result in writing_list if result > writing_second_std_deviation_start and result < writing_second_std_deviation_end]
writing_list_of_data_3_std_deviation = [result for result in writing_list if result > writing_third_std_deviation_start and result < writing_third_std_deviation_end]

print("{}% of data for MATH SCORE lies within 1 standard deviation".format(len(math_list_of_data_1_std_deviation)*100.0/len(math_list)))
print("{}% of data for MATH SCORE lies within 2 standard deviation".format(len(math_list_of_data_2_std_deviation)*100.0/len(math_list)))
print("{}% of data for MATH SCORE lies within 3 standard deviation".format(len(math_list_of_data_3_std_deviation)*100.0/len(math_list)))

print("{}% of data for READING SCORE lies within 1 standard deviation".format(len(reading_list_of_data_1_std_deviation)*100.0/len(reading_list)))
print("{}% of data for READING SCORE lies within 2 standard deviation".format(len(reading_list_of_data_2_std_deviation)*100.0/len(reading_list)))
print("{}% of data for READING SCORE lies within 3 standard deviation".format(len(reading_list_of_data_3_std_deviation)*100.0/len(reading_list)))

print("{}% of data for WRITING SCORE lies within 1 standard deviation".format(len(writing_list_of_data_1_std_deviation)*100.0/len(writing_list)))
print("{}% of data for WRITING SCORE lies within 2 standard deviation".format(len(writing_list_of_data_2_std_deviation)*100.0/len(writing_list)))
print("{}% of data for WRITING SCORE lies within 3 standard deviation".format(len(writing_list_of_data_3_std_deviation)*100.0/len(writing_list)))