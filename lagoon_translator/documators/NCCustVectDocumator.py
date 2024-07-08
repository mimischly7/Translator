from pyspark.sql import DataFrame, SparkSession
from pyspark.sql.functions import udf, collect_list
from pyspark.sql.types import StructType, StringType, ArrayType, Row
from jinja2 import Template
from pprint import pprint
from typing import List

from lagoon_translator.Document import Document
from lagoon_translator.utils import recursive_dictify
from lagoon_translator.templates.ncentral_template import jinja_template
from lagoon_translator.documators.Documator import Documator

class NCCustVectDocumator(Documator):
    def __init__(self):
        super(NCCustVectDocumator, self).__init__(self.__class__.__name__, template)
    
    def documentify(self, row: Row, template: str) -> List[Document]:
        ### 1: convert the map-like object to a string
        content = recursive_dictify(row)['cust_struct']
        jinja_temp = Template(template)
        data = {"data": content, "metadata": {"num_devices": len(content["dev_structs"])}}
        formatted_text = template.render(cust_struct=data["data"], meta=data["metadata"])
        pprint(f"formatted_text: {formatted_text}")
        data_for_doc = {
            "content" : formatted_text[:1500],
            "payload" : {"summary" : f"NCentral information for customer {content['customer_id']}"},
            "collection" : "customers"
        }
        ### 2: use the formatted string (and other info) to produce a Document object
        doc = Document(content = data_for_doc["content"], payload = data_for_doc["payload"], collection = data_for_doc["collection"])
        return [doc]