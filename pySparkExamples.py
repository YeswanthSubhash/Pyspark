from pyspark.sql import Window
from pyspark.sql.types import *
from pyspark.sql.functions import *

spark = SparkSession.builder.appName('abc').getOrCreate()
#df=spark.read.csv('file:///C://Users//Midhun//Documents//PythonScripts//employee.csv',header=True)

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
empsalary.show()

overCategory=Window.partitionBy('depName')
df=empsalary.withColumn("total_salary_in_dep", sum('salary').over(overCategory))\
            .withColumn("salaries",collect_list('salary').over(overCategory))\
            .withColumn("avg_salary",avg('salary').over(overCategory))

overCategory=Window.partitionBy('depName').orderBy('salary'.desc)
df = empsalary.withColumn("salaries", collect_list('salary').over(overCategory))\
              .withColumn("rank", rank().over(overCategory))\
              .withColumn("dense_rank", dense_rank().over(overCategory))\
              .withColumn("row_number", row_number().over(overCategory))\
              .withColumn("ntile", ntile(3).over(overCategory))\
              .withColumn("percent_rank", percent_rank(). over(overCategory))

df2=empsalary.withColumn('dense_rank',rank().over(overCategory))
