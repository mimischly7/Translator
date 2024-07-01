## AWS Region problem
```
Traceback (most recent call last):
  File "/Users/mimischly/Desktop/bluebird/jun03/Translation/translate.py", line 60, in <module>
    print(customers.show(10))
          ^^^^^^^^^^^^^^^^^^
  File "/Users/mimischly/Desktop/bluebird/jun03/Translation/.venv/lib/python3.11/site-packages/pyspark/sql/dataframe.py", line 945, in show
    print(self._show_string(n, truncate, vertical))
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/mimischly/Desktop/bluebird/jun03/Translation/.venv/lib/python3.11/site-packages/pyspark/sql/dataframe.py", line 963, in _show_string
    return self._jdf.showString(n, 20, vertical)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/mimischly/Desktop/bluebird/jun03/Translation/.venv/lib/python3.11/site-packages/py4j/java_gateway.py", line 1322, in __call__
    return_value = get_return_value(
                   ^^^^^^^^^^^^^^^^^
  File "/Users/mimischly/Desktop/bluebird/jun03/Translation/.venv/lib/python3.11/site-packages/pyspark/errors/exceptions/captured.py", line 179, in deco
    return f(*a, **kw)
           ^^^^^^^^^^^
  File "/Users/mimischly/Desktop/bluebird/jun03/Translation/.venv/lib/python3.11/site-packages/py4j/protocol.py", line 326, in get_return_value
    raise Py4JJavaError(
py4j.protocol.Py4JJavaError: An error occurred while calling o77.showString.
: software.amazon.awssdk.core.exception.SdkClientException: Unable to load region from any of the providers in the chain software.amazon.awssdk.regions.providers.DefaultAwsRegionProviderChain@4c6cf8d6: [software.amazon.awssdk.regions.providers.SystemSettingsRegionProvider@3da0e335: Unable to load region from system settings. Region must be specified either via environment variable (AWS_REGION) or  system property (aws.region)., software.amazon.awssdk.regions.providers.AwsProfileRegionProvider@26fdb98b: No region provided in profile: default, software.amazon.awssdk.regions.providers.InstanceProfileRegionProvider@860f712: Unable to contact EC2 metadata service.]
	at software.amazon.awssdk.core.exception.SdkClientException$BuilderImpl.build(SdkClientException.java:111)
	at software.amazon.awssdk.regions.providers.AwsRegionProviderChain.getRegion(AwsRegionProviderChain.java:70)
	at software.amazon.awssdk.awscore.client.builder.AwsDefaultClientBuilder.resolveRegion(AwsDefaultClientBuilder.java:293)
	at software.amazon.awssdk.utils.AttributeMap$DerivedValue.primeCache(AttributeMap.java:600)
	at software.amazon.awssdk.utils.AttributeMap$DerivedValue.get(AttributeMap.java:589)
	at software.amazon.awssdk.utils.AttributeMap$Builder.resolveValue(AttributeMap.java:396)
	at software.amazon.awssdk.utils.AttributeMap$Builder.internalGet(AttributeMap.java:389)
	at software.amazon.awssdk.utils.AttributeMap$Builder.access$1300(AttributeMap.java:201)
	at software.amazon.awssdk.utils.AttributeMap$Builder$1.get(AttributeMap.java:399)
	at software.amazon.awssdk.awscore.client.builder.AwsDefaultClientBuilder.resolveSigningRegion(AwsDefaultClientBuilder.java:260)
	at software.amazon.awssdk.utils.AttributeMap$DerivedValue.primeCache(AttributeMap.java:600)
	at software.amazon.awssdk.utils.AttributeMap$DerivedValue.get(AttributeMap.java:589)
	at software.amazon.awssdk.utils.AttributeMap$Builder.resolveValue(AttributeMap.java:396)
	at java.base/java.util.ArrayList.forEach(ArrayList.java:1596)
	at software.amazon.awssdk.utils.AttributeMap$Builder.build(AttributeMap.java:362)
```

**Fix**: Set an environment variable `AWS_REGION`, i.e. `os.env['AWS_REGION'] = "us-east-1"`

**Observations**:
- I am able to run 
    ```
    customers = spark.sql(f"SELECT * FROM {namespace}.customers")
    print(customers)
    print(type(customers))
  ```
  without an error, and it actually shows the columns of the table, so
    it must be connected to MinIO!
- Any string you put will work, because the aws client is not actually using it
    minio is hosted on my local machine!





UDAF:
- [ ] https://stackoverflow.com/questions/46187630/how-to-write-pyspark-udaf-on-multiple-columns
- [ ] SOS: https://danvatterott.com/blog/2018/09/06/python-aggregate-udfs-in-pyspark/
- [ ] SOS: https://florianwilhelm.info/2017/10/efficient_udfs_with_pyspark/

# Learning
- An RDD (resilient distributed dataset) is the low-kevelndata structure
    of Spark and a Spark dataframe is build on top of it.
- " in PySpark you should avoid all kind of Python UDFs - like RDD functions or data frame UDFs - as much as possible! Whenever there is a built-in DataFrame method available, this will be much faster than its RDD counterpart."
- asd



# TODO
- [ ] summary of statistics on top of customer page
- [ ] use take to retrieve results n at a time to store to qdrant/elastic
- [ ] create functionality to store to elastic as keyword
- [ ] create the functionality to store to qdrant as vectors
  - **this will require chunking a company file into multiple files**





# TODO:
  - [ ] Work
    - [ ] Implement `Ingestor` for `qdrant`
    - [ ] Make sure airflow works up to store-data
    - [ ] Run the DAG with full data, and then run the translator (before running translato remove indices/collections)
    - [ ] package into a wheel to be used in the lagoon project -- remember that everything that now comes out of a `.env` file
          or a `config.py` file will now have to becomne parameters of a function to be passed in the airflow process (from xcom
          info for example)
  - [ ] Liu
    - [ ] Wrap up PR for button
    - [ ]
  - [ ] Personal


  - [ ] https://www.youtube.com/watch?v=2KLC2yxxR1g&ab_channel=NaturalLanguageProcessingpresentations