import csv                
with open('userReviews.csv', encoding='utf-8-sig') as reviews:
  reader = csv.DictReader(reviews, delimiter= ';')
  data = list(reader)
  next(reader, None)


# Assigning variable zodiac_scores to list()
# When value in movieName is "Zodiac",append the values of column "Metascore_w"

zodiac_scores = list()
for row in data:
  if row['movieName'] == 'zodiac':
      zodiac_scores.append(int(row['Metascore_w']))

print('The scores given to the movie Zodiac are: ' + str(zodiac_scores) + '.')


# Calculating my personal score for movie Zodiac
# My personal scores per variable
entertainment_score = 8.5
engaging_score = 9
cinematography_score = 7
acting_score = 9
plot_score = 8.5

# Final score is the average of the above scores
personal_movie_score = int(entertainment_score + engaging_score + cinematography_score + acting_score + plot_score) / 5

print('My personal score for the movia Zodiac depends on a few factors. For entertainment, the score will be '+ str(entertainment_score) + ', for engagement, I give the score ' + str(engaging_score) + ', the cinematography-score will be ' + str(cinematography_score) + ' the acting score gets a ' + str(acting_score) + ' and finally the plot score gets a ' + str(plot_score) + '. My end-score (average scores) will be ' + str(personal_movie_score) + '.')

# Create empty lists so we can fill it with values from userReviews.csv
# First I wanted to do reviewer = list(), but I've learned that "reviewer = []" is better, since its always a list-literal.

reviewer = []
moviename = []
given_score = []
reviewers_list = []
name_favourite_movie = 'zodiac'


# Give zero values to variables, so I can calculate from zero
user_count = 0
sum_zodiac = 0
average = 0
   


# Going through every user and showing their given score and by going through every user, the sum of the whole
# For every user that watched Zodiac, add the score to the previous sum and add 1 to count everytime the loop
# makes a loop. This, so the average will be calculated correctly (sum scores/amount of scores)


for row in data:
  if row['movieName'] == 'zodiac':
    sum_zodiac += float(row['Metascore_w'])
    user_count = user_count + 1
    reviewers_list.append(row['Author'])
   
    print('User: ' + str(reviewers_list[-1]) + '\n' + 'Given score: ' + (row['Metascore_w']) + '\n' + 'The total score zodiac: ' + str(sum_zodiac) + '\n' + 'Amount of scores: ' + str(user_count) + '\n')


# Calculating average score
# Average is summing all values and deviding it by amount of numbers
# Endvalue will be printed with one decimal


average_score_zodiac = round((sum_zodiac / user_count), 1)


print('The average score for the movie Zodiac is ' + str(average_score_zodiac) + '.' + '\n')


# My personal scores per variable
entertainment_score = 8.5
engaging_score = 9
cinematography_score = 7
acting_score = 9
plot_score = 8.5
personal_movie_score = int(entertainment_score + engaging_score + cinematography_score + acting_score + plot_score) / 5

print('My personal score for the movia Zodiac depends on a few factors. For entertainment, the score will be '+ str(entertainment_score) + ', for engagement, I give the score ' + str(engaging_score) + ', the cinematography-score will be ' + str(cinematography_score) + ', the acting score gets a ' + str(acting_score) + ' and finally the plot score gets a ' + str(plot_score) + '. My end-score (average scores) will be ' + str(personal_movie_score) + '.' + '\n')


# Calculate the difference between personal score and average score Zodiac
difference_score = round((average_score_zodiac - personal_movie_score), 2)

if difference_score > 0:
    print('The average score is higher than my personal score, the difference is ' + str(difference_score) + '.' + '\n')
elif difference_score == 0:
   print('The average score is ' + str(average_score_zodiac) + ' and my personal score is ' + int(personal_movie_score) + ', this means the scores are the same.' + '\n')
else:
    print('The average score is lower than my personal score, the difference is ' +str(difference_score) + '.' + '\n')


# Create list authors_review_zodiac and append the names to list when it movieName == Zodiac
authors_review_zodiac = list()
for row in data:
    if row['movieName'] == 'zodiac':
        authors_review_zodiac.append(row['Author'])
print('The name of the authors that put a review on Zodiac are: ' + str(authors_review_zodiac) + '.' + '\n')


# Create list with watched movies by the reviewers of Zodiac and have a score equal or greater than "zodiac_scores"
watched_movies = list()
for row in data:
    if row['Author'] in authors_review_zodiac and (int(row['Metascore_w']))>= average_score_zodiac:
        watched_movies.append(row['movieName'])

print('Movies watched by the users that reviewed Zodiac are: ' + str(watched_movies) + '.' + '\n')


# List of the reviewer's movielist that watched "Zodiac" as well

# Creating a list to put the final values in
with open('userReviews.csv', 'r', encoding= 'utf-8-sig') as userreviews:
  detail_list = []
  end_list = []
  reader = csv.reader(userreviews, delimiter=';')
 
# If revieuwer has watched "Zodiac" and his score is higher than average score, print his name, his given score and the movie that belongs to this score
  for row in reader:
        if(row[2]) in reviewers_list and float(row[1]) > float(average):
            print('Reviewer: ' + row[2] + '\n' + "The movie: " + str(row[0]) + '\n' + 'Given score: ' + str(row[1]) )
            detail_list.extend([row[0], row[1], row[2]])
            end_list.extend([detail_list])
            print('List of details:' + str(detail_list) + '\n')
            detail_list = []