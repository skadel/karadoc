from karadoc.common import Job

job = Job()

job.external_inputs = {"source": {"connection": "dummy"}}

job.output_format = "parquet"


def run():
    pass
