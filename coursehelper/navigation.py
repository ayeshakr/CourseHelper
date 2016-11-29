import re
import yaml
import datetime
import sqlite3

from database import get_db, query_db
from sqlite3 import IntegrityError, Row

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def regexCheck(searchQuery):
	return re.match(r'^[a-zA-Z]{4}\s?[0-9]{3}([a-zA-Z]\d)?$', searchQuery)

def formatQuery(searchQuery):
	query = (searchQuery.upper()).replace(" ", "")
	qLength = len(query)

	if qLength > 7:
		query = query[:-(qLength - 7)]

	return query

def getCourseInfo(courseID):
	print "TEST"
	courseInfo = {}

	if regexCheck(courseID):
		query = formatQuery(courseID)
		print "Searching for : " + query

		db = get_db()
		db.row_factory = Row

		result = query_db('SELECT * FROM courses WHERE courseid = (?)', (query, ) , one=True)
		
		if not result is None:
			courseInfo = yaml.safe_load(result['description'])

	return courseInfo

def getCoursePosts(courseID):
	coursePosts = []

	if regexCheck(courseID):
		query = formatQuery(courseID)
		print "Asking for posts for course: " + query 
		
		db = get_db()
		db.row_factory = dict_factory

		result = query_db('SELECT * FROM posts WHERE courseid = (?)', (query, ) , one=False)

		print "Received: " + str(result)

		if not result is None:
			for desc in result:
				print "checking : " + str(desc)
				coursePosts.append(desc)

	return coursePosts

def checkValidPost(post):
	error = None

	if len(post) < 2:
		error = "Error! Post must contain at least 3 characters"

	return error

def addPostAttempt(request, session):
	post = request.form['post']
	courseid = request.form['courseid']
	print "Wants to add Post: " + post + " to Course : " + courseid

	error = checkValidPost(post)

	if not error is None:
		print error
		return error

	username = session['username']
	timestamp = datetime.datetime.now().strftime("%H:%M %Y-%m-%d")
	db = get_db()

	try:
		db.execute('INSERT INTO posts (userid, courseid, post, tstamp) VALUES (?, ?, ?, ?)', [username, courseid, post, timestamp])
		db.commit()
    #if not, redirect user to registration page
	except IntegrityError:
		db.rollback()
		error = "Invalid Entry!"
		print error
		return error

	return error