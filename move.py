import pandas as pd # pandas is used to read csv files
import MySQLdb # MySQLdb is used to connect Python with MySQL
db = MySQLdb.connect("localhost", "root", "babai30.2008", "basic")
# MySQLdb.connect(database server IP, username, password, database name)
list1 = pd.read_csv(
    "C:\Users\Saikat\Desktop\Bosch" + \
    "IRIS.csv").dropna()
quandl_stock_w_fundamental_list[:5]
