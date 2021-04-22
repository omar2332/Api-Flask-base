import psycopg2
from decouple import config



def get_connection():
	conn = psycopg2.connect(
		    host=config('HOST'),
		    database=config('DB'),
		    user=config('API_USER'),
		    password=config('PASSWORD'))

	cur = conn.cursor()
	return conn,cur

def close_connection(conn):
	if conn is not None:
		conn.close()
		#print('Database connection closed.')
		return True



##################################

def get_result_query(query_string ):
	result_query = None
	try:
		conn,cur= get_connection()
		cur.execute(query_string)	
		result_query = cur.fetchall()
		cur.close()
	except (Exception, psycopg2.DatabaseError) as error:
	    print(error)
	finally:
	    close_connection(conn)


	return(result_query)




