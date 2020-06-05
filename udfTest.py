from pyspark.sql import Window
from pyspark.sql.types import *
from pyspark.sql.functions import *

empsalary_data = [
    ("sales",     1,  "Alice",  5000, ["game",  "ski"]),
    ("personnel", 2,  "Olivia", 3900, ["game",  "ski"]),
    ("sales",     3,  "Ella",   4800, ["skate", "ski"]),
    ("sales",     4,  "Ebba",   4800, ["game",  "ski"]),
    ("personnel", 5,  "Lilly",  3500, ["climb", "ski"]),
    ("develop",   7,  "Astrid", 4200, ["game",  "ski"]),
    ("develop",   8,  "Saga",   6000, ["kajak", "ski"]),
    ("develop",   9,  "Freja",  4500, ["game",  "kajak"]),
    ("develop",   10, "Wilma",  5200, ["game",  "ski"]),
    ("develop",   11, "Maja",   5200, ["game",  "farming"])]

empsalary=spark.createDataFrame(empsalary_data,schema=["depName", "empNo", "name", "salary", "hobby"])

def test_game(games):
    if(games.__contains__('game')):
        return 1
    else:
        return 0

testg=udf(lambda x : test_game(x))

spark.udf.register("testg",testg)

df2=empsalary.withColumn('test_game',when(testg(col("hobby")).cast("Int")==1,"g").otherwise("n"))




