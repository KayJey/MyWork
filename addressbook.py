import pyodbc


#fill in the appropriate driver name and server name
#here tablle name is "crash"
#columns names are "name" and "num"
conn=pyodbc.connect(
	"Driver={};"
	"Server=<;"
	"Database=contacts;"
	"Trusted_Connection=yes;"
)
def main():
	again = 'yes'
	print("ADDRES BOOK")
	while(again == 'yes'):
		opt = input(" what do u wana do ? \n a.Search a contact  \n b.List all contacts  \n enter a or b  \t ")
		if opt == 'a' :
			update(conn)
			
		elif opt == 'b':
			read(conn)
		again = input(" do u wana continue ? reply with 'yes' or 'no'  \t:")



def read(conn):
	print("read")
	cursor=conn.cursor()
	cursor.execute("select * from crash ;")
	print("NAME\t\tNUM")
	row = cursor.fetchall()
	for r in row :
		print(f"{r[0]}\t{r[1]}")
def update(conn):
	cursor=conn.cursor()
	l = 0
	search = input("Search by 1. NAME  2.NUM   \n enter 1 or 2  \t" )
	if search == '1':
		find = input('enter the NAME in lowercase \t')
		cursor.execute("select name , num from crash where name = ? \t ;" , (find))
		print("NAME\t\tNUM")
		row = cursor.fetchall()
		for r in row :
			print(f"{r[0]}\t{r[1]}")
	elif search == '2':
		find = input('enter the num ')
		cursor.execute("select name , num from crash where num = \t ? ;" , (find))
		print("NAME\t\tNUM")
		row = cursor.fetchall()
		for r in row :
			print(f"{r[0]}\t{r[1]}")
	

main()
conn.close()