# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC # Deploy tasks
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Study: deployment.yml
# MAGIC
# MAGIC Look at `orgs/acme/domains/transport/projects/taxinyc/flows/prep/revenue/deployment.yml`.
# MAGIC It defines the job which will run the pipeline.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Task: Run dev deploy
# MAGIC
# MAGIC 1. Go to the notebook orgs/acme/domains/transport/projects/taxinyc/flows/prep/revenue/deploy
# MAGIC 2. Connect to serverless compute.
# MAGIC 3. Run the cells up to and including deploying and running the dev job.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Task: Look for the job under Job Runs
# MAGIC
# MAGIC Job Runs are on the side menu

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Task: Run the job by pressing the run button in the UI

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Task: What is the difference between a job and a job run?

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC The job is the plan. The job run is the execution of the plan.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Task: How was the job name composed?
# MAGIC
# MAGIC Name: transport_taxinyc_test_revenue_mortengade_main_514d1f89
# MAGIC
# MAGIC It seems like everything is being handled by your custom functions. They can read my username and the commit id. The environment is specified in the function: autojob(env="test"). 
# MAGIC
# MAGIC The path to the job (something like 'databricks-dataops-course-mrg/orgs/acme/domains/transport/projects/taxinyc/flows/prep/revenue') is used to infer the domain (transport), the project (taxinyc) and the subject (revenue)
