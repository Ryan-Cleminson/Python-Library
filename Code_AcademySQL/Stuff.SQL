
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