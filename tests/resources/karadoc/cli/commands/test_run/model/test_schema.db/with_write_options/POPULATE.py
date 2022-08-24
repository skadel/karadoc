from karadoc.common import Job

job = Job()

job.output_options = {"compression": "gzip"}

job.output_format = "json"


def run():
    return job.spark.sql("select 'a' as a")
