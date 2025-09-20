import statistics as st

# Mean
student_score = [30, 50, 40, 25, 45, 35]
mean = st.mean(student_score)
print(mean) 

# harmornic mean
print('=============================' *2)
print('Harmonic Mean')
h_mean = st.harmonic_mean(student_score)
print(h_mean)

# median
print('=============================' *2)
print('Median')
medi = st.median(student_score)
print(medi)

# mode
print('=============================' *2)
print('Mode')
mod = st.mode(student_score)
print(mod)

# standard deviation
print('=============================' *2)
print('Standard Deviation')
std = st.stdev(student_score)
print(std)

# variance
print('=============================' *2)
print('Variance')
var = st.variance(student_score)
print(var)

"""Suppose you travel to a place at  60km/h and return at 40km/h.
calculate the average speed
          n
  ------------------
  i/x1 + 1/x2 ...... 1/xn

(60+40)/2=50.
Instead, the harmonic mean is:
Arithmetic Mean
You recorded the daily temperature (in °C) for a week: [30, 32, 31, 29, 35, 33, 30].
Find the average temperature using statistics.mean().

Median
The salaries (in $1000s) of employees are: [45, 50, 47, 60, 55, 53, 48].
Find the median salary using statistics.median().

Median Low & Median High
Exam scores: [65, 70, 75, 80, 85, 90].
Find the median_low and median_high scores.

Mode
In a survey, shoe sizes of customers were recorded as: [42, 41, 42, 40, 43, 42, 41].
Find the most common shoe size using statistics.mode().

Multimode
Votes for favorite fruits: ["apple", "banana", "apple", "orange", "banana", "banana", "apple", "orange"].
Find all the modes using statistics.multimode().

📌 Variability / Spread (Variance, Standard Deviation, etc.)

Variance
Marks of students in a test: [65, 70, 75, 80, 85].
Find the variance using statistics.variance().

Standard Deviation
Heights (in cm) of students: [160, 165, 170, 175, 180].
Calculate the standard deviation using statistics.stdev().

Population Variance & Std Dev
The weights (kg) of all 6 workers in a small company are: [55, 60, 65, 70, 75, 80].
Find the population variance and population standard deviation using statistics.pvariance() and statistics.pstdev().

📌 Special Means (Geometric, Harmonic, etc.)

Geometric Mean
Monthly growth multipliers for a stock are [1.02, 1.05, 0.98, 1.03].
Find the average growth rate using statistics.geometric_mean().

Harmonic Mean
A car travels at 60 km/h for one trip and 40 km/h on the return.
Find the average speed using statistics.harmonic_mean().

📌 Quantiles & Other Stats

Quantiles
Exam scores: [30, 40, 50, 60, 70, 80, 90, 100].
Find the quartiles (25%, 50%, 75%) using statistics.quantiles().

Fmean (Fast Mean)
Data: [1.1, 2.3, 3.7, 4.6, 5.5].
Find the arithmetic mean using statistics.fmean() (faster version of mean()).

Multimode for Survey Data
Favorite programming languages of developers: ["Python", "JavaScript", "Python", "C++", "JavaScript", "Python"].
Find the most common languages using statistics.multimode().

📌 Real-Life Data Mix

Comparing Mean, Median, Mode
House prices in a small town (in $1000s): [150, 155, 160, 165, 170, 1000].
Find mean, median, and mode, and discuss which best represents the data (since there’s an outlier).

Variance & Std Dev for Daily Sales
Daily sales (in $): [200, 220, 210, 205, 230, 240, 1000].
Find the variance and standard deviation.
Explain whether the data is consistent or has high variability."""

print('=============================' *2)
print("""
    Suppose you travel to a place at  60km/h and return at 40km/h.
    calculate the average speed
""")
speed = [60, 40]
average_speed = st.harmonic_mean(speed)
print(f'Average Speed: {average_speed}')

print('=============================' *2)
print("""You recorded the daily temperature (in °C) for a week: [30, 32, 31, 29, 35, 33, 30].
Find the average temperature using statistics.mean().
      """)

daily_temperature = [30, 32, 31, 29, 35, 33, 30]
avg_daiy_temp = st.mean(daily_temperature)
print(avg_daiy_temp)

print('=============================' *2)
print("""Favorite programming languages of developers: ["Python", "JavaScript", "Python", "C++", "JavaScript", "Python"].
Find the most common languages using statistics.multimode().
""")
fav_prog_lang = ["Python", "JavaScript", "Python", "C++", "JavaScript", "Python"]
common_lang = st.multimode(fav_prog_lang)
print(common_lang)

print('=============================' *2)
print("""Exam scores: [30, 40, 50, 60, 70, 80, 90, 100].
Find the quartiles (25%, 50%, 75%) using statistics.quantiles().
""")
exam_scores = [30, 40, 50, 60, 70, 80, 90, 100]
quantile_25th = st.quantiles(exam_scores, n=25)
print(quantile_25th)