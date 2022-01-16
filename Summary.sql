SELECT url FROM movies10 WHERE lexemesSummary @@ to_tsquery(‘zodiac’);
               
UPDATE movies10 SET rank=ts_rank(lexemesSummary,plainto_tsquery((SELECT Summary FROM movies10 WHERE url=‘zodiac’)));

\copy (SELECT * FROM recommendationsBasedOnSummaryField2) to '/home/pi/RSL/top50recommendations.csv' WITH csv;