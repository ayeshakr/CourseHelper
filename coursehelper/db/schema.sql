DROP TABLE IF EXISTS users;
CREATE TABLE users (
	username TEXT PRIMARY KEY,
	email TEXT NOT NULL,
	password TEXT NOT NULL
);
DROP TABLE IF EXISTS courses;
CREATE TABLE courses (
	courseid TEXT PRIMARY KEY,
	description TEXT
);
DROP TABLE IF EXISTS reviews;
CREATE TABLE reviews (
	rid TEXT PRIMARY KEY,
	tstamp TEXT NOT NULL,
	courseid TEXT NOT NULL,
	userid TEXT NOT NULL,
	review TEXT NOT NULL,
	stars INTEGER
);
DROP TABLE IF EXISTS coursefollowers;
CREATE TABLE coursefollowers (
	userid TEXT NOT NULL,
	courseid TEXT NOT NULL,
	PRIMARY KEY(userid, courseid)
);
DROP TABLE IF EXISTS posts;
CREATE TABLE posts (
	postid INTEGER PRIMARY KEY AUTOINCREMENT,
	userid TEXT NOT NULL,
	courseid TEXT NOT NULL,
	parentid TEXT,
	post TEXT NOT NULL,
	tstamp TEXT NOT NULL
)

