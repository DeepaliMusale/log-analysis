# ############# FIRST QUERY #############
import psycopg2
DBNAME = "news"

def get_data():
	db = psycopg2.connect(database=DBNAME)
	c = db.cursor()
	
	#query1 = "select title, count(*) as views from articles, log where substring(log.path, 10)=articles.slug group by title order by views desc limit 3"
	query1 = "select * from num_of_views limit 3 "
	c.execute(query1)
	data = c.fetchall()
	db.close()
	return data
results = get_data()
print('1). What are the most popular articles of all time? \n')
for rows in range(0,3):
	print('\t %s - %d views \n' % (results[rows][0], results[rows][1]))

########### SECOND QUERY #################
def popular_author():
 	db = psycopg2.connect(database=DBNAME)
	c = db.cursor()
	query2 = "select name, views from popular_authors order by views desc limit 5;"
 	c.execute(query2)
 	data2 = c.fetchall()
 	db.close()
 	return data2
result2 = popular_author()
print('\n 2). Who are the most popular article authors of all time? \n')
for rows in range(0,5):
	print('\t %s - %d views \n' % (result2[rows][0], result2[rows][1]))


########### THIRD QUERY #################
def errors():
 	db = psycopg2.connect(database=DBNAME)
 	c = db.cursor()
	query3 = "select * from percentage order by percent desc limit 1;"
 	c.execute(query3)
 	data3 = c.fetchall()
 	db.close()
 	return data3
result3 = errors()
print('\n 3). On which days did more than 1% of requests lead to errors? \n')
for rows in range(0,1):
 	print('\t %s - %g percent \n' % (result3[rows][0], result3[rows][1]))


