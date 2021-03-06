ALTER TABLE movies10 ADD lexemesStarring tsvector;

UPDATE movies10 SET lexemesStarring=to_tsvector(Starring);

SELECT url FROM movies10 WHERE lexemesStarring @@ to_tsquery(‘Gyllenhaal’);


UPDATE movies10 SET rank = ts_rank(lexemesStarring,plainto_tsquery((SELECT Starring FROM movies10 WHERE url='Gyllenhaal')));

CREATE TABLE recommendationsBasedOnStarringField AS SELECT url, rank FROM movies10 WHERE rank <0.99 ORDER BY rank DESC LIMIT 50;

UPDATE movies10 SET rank = ts_rank(lexemesStarring,plainto_tsquery((SELECT Starring FROM movies10 WHERE url=‘zodiac’)));

CREATE TABLE recommendationsBasedOnStarringField2 AS SELECT url, rank FROM movies10 WHERE rank <0.99 ORDER BY rank DESC LIMIT 50;

\copy (SELECT*FROM recommendationsBasedOnStarringField2) to '/home/pi/RSL/top50recommendationsStarring.csv' WITH csv;