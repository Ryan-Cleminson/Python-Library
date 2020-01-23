
/****************************/
/*  Adds Rows to table   */
/****************************/
INSERT INTO TableName(id, name, age)
VALUES (1, 'NAME1',22);

INSERT INTO TableName(id, name, age)
VALUES (2, 'NAME2',22);

INSERT INTO TableName(id, name, age)
VALUES (3, 'NAME3',22);

INSERT INTO TableName(id, name, age)
VALUES (4, 'NAME4',22);

/****************************/
/*  Adds Columns to table   */
/****************************/
ALTER TABLE TableName
ADD COLUMN twitter_handle TEXT;
SELECT * FROM TableName;

/****************************/
/*  Adds Columns to table   */
/****************************/
UPDATE TableName
SET twitter_handle = '@taylorswift13'
WHERE id = 4;
SELECT * FROM TableName;

/*********************************************************/
/*  Deletes specific elements that contain a NULL Field  */
/*********************************************************/
DELETE FROM TableName
WHERE twitter_handle IS NULL;
SELECT * FROM TableName;

/*****************************************************************************/
/*  Creates new table named awards with entities id, recipient, award_name   */
/*****************************************************************************/
CREATE TABLE awards(
    id INTEGER PRIMARY KEY,
    recipient TEXT NOT NULL,
    award_name TEXT DEFAULT 'Grammy'
);

/*********************/
/*  Rename Columns   */
/*********************/
SELECT imdb_rating AS 'IMDb'
FROM movies;

/***********************************************************/
/*  DISTINCT -> Displays years in movies without duplicates*/
/***********************************************************/

SELECT DISTINCT year
FROM movies;

/***********************************************************/
/*  Displays the movies that were made after 2014          */
/***********************************************************/
SELECT *
FROM movies
WHERE year > 2014

/***********************************************************************************************************************/
/*  Displays all movies where the name is similar to that of the 'quote' where the "_" acts as any individual character*/
/***********************************************************************************************************************/
SELECT *
FROM movies
WHERE name LIKE 'Se_en';

/*****************************************************************************************************/
/*  "%" matches zero or more characters in the patern ---> A% will find all movies that start with A */
/*****************************************************************************************************/
SELECT * 
FROM movies
WHERE name LIKE '%man%';

/******************************************************************************/
/*  Shows results of movies between 1970 and 1979 and have a high imdb rating */
/******************************************************************************/
SELECT *
FROM movies
WHERE year BETWEEN 1970 AND 1979
  AND imdb_rating > 8;

/*************************************************************/
/*  Shows results of movies with genres of romance or comedy */
/*************************************************************/
SELECT *
FROM movies
WHERE genre = 'romance' or genre = 'comedy';

/*************************************************************/
/*  Shows results of movies in an alphabetical order */
/*************************************************************/

SELECT name, year
FROM movies
ORDER BY name;

/***************************************************************/
/*  Shows results of best rated movies rated highest to lowest */
/***************************************************************/
SELECT name, year, imdb_rating
FROM movies
ORDER BY imdb_rating DESC;


/***************************************************************/
/*  Shows top 3 rated movies */
/***************************************************************/
Select * 
FROM movies
ORDER BY imdb_rating DESC
LIMIT 3;