ip_address = '10.0.0.146'
catalog_name = "rest_catalog"
rest_endpoint = f"{ip_address}:8181"
minio_endpoint = f"{ip_address}:9000"
bucket = "lakehouse"
access_key = "5zB1RkdFOd0gk4WbiCpY"
secret_key = "tPf3sA0XOLnHye4IRLRbAcZspsbpGzrfMWj3FXws"
namespace = "ncentral"
table_name = "service_orgs"
classpath = ("/Users/mimischly/Desktop/bluebird/lagoon-ice/store-data/target/scala-2.12/classes:"
             "/Users/mimischly/Desktop/bluebird/lagoon-ice/store-core/target/scala-2.12/classes:"
             "/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/ch/qos/logback/logback-classic/1.5.6/logback-classic-1.5.6.jar:"
             "/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/ch/qos/logback/logback-core/1.5.6/logback-core-1.5.6.jar:"
             "/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/ch/qos/reload4j/reload4j/1.2.22/reload4j-1.2.22.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/co/fs2/fs2-core_2.12/3.10.2/fs2-core_2.12-3.10.2.jar:"
             "/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/co/fs2/fs2-io_2.12/3.10.2/fs2-io_2.12-3.10.2.jar:"
             "/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.12.262/aws-java-sdk-bundle-1.12.262.jar:"
             "/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/com/carrotsearch/thirdparty/simple-xml-safe/2.7.1/simple-xml-safe-2.7.1.jar:"
             "/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/com/clearspring/analytics/stream/2.9.6/stream-2.9.6.jar:"
             "/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/com/comcast/ip4s-core_2.12/3.5.0/ip4s-core_2.12-3.5.0.jar:"
             "/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/com/esotericsoftware/kryo-shaded/4.0.2/kryo-shaded-4.0.2.jar:"
             "/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/com/esotericsoftware/minlog/1.3.0/minlog-1.3.0.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/com/fasterxml/jackson/core/jackson-annotations/2.15.2/jackson-annotations-2.15.2.jar:"
             "/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/com/fasterxml/jackson/core/jackson-core/2.15.2/jackson-core-2.15.2.jar:"
             "/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/com/fasterxml/jackson/core/jackson-databind/2.15.2/jackson-databind-2.15.2.jar:"
             "/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/com/fasterxml/jackson/datatype/jackson-datatype-jsr310/2.15.2/jackson-datatype-jsr310-2.15.2.jar:"
             "/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/com/fasterxml/jackson/module/jackson-module-scala_2.12/2.15.2/jackson-module-scala_2.12-2.15.2.jar:"
             "/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/com/github/luben/zstd-jni/1.5.5-4/zstd-jni-1.5.5-4.jar:"
             "/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/com/github/scopt/scopt_2.12/4.1.0/scopt_2.12-4.1.0.jar:"
             "/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/com/github/wendykierp/JTransforms/3.1/JTransforms-3.1.jar:"
             "/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/com/google/code/findbugs/jsr305/3.0.2/jsr305-3.0.2.jar:"
             "/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/com/google/code/gson/gson/2.10.1/gson-2.10.1.jar:"
             "/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/com/google/crypto/tink/tink/1.9.0/tink-1.9.0.jar:"
             "/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/com/google/errorprone/error_prone_annotations/2.23.0/error_prone_annotations-2.23.0.jar:"
             "/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/com/google/flatbuffers/flatbuffers-java/1.12.0/flatbuffers-java-1.12.0.jar:"
             "/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/com/google/guava/failureaccess/1.0.2/failureaccess-1.0.2.jar:"
             "/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/com/google/guava/guava/33.0.0-jre/guava-33.0.0-jre.jar:"
             "/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/com/google/guava/listenablefuture/9999.0-empty-to-avoid-conflict-with-guava/listenablefuture-9999.0-empty-to-avoid-conflict-with-guava.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/com/google/j2objc/j2objc-annotations/2.8/j2objc-annotations-2.8.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/com/google/protobuf/protobuf-java/3.19.6/protobuf-java-3.19.6.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/com/ibm/icu/icu4j/69.1/icu4j-69.1.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/com/ning/compress-lzf/1.1.2/compress-lzf-1.1.2.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/com/squareup/okhttp3/okhttp/4.12.0/okhttp-4.12.0.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/com/squareup/okio/okio-jvm/3.6.0/okio-jvm-3.6.0.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/com/squareup/okio/okio/3.6.0/okio-3.6.0.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/com/sun/istack/istack-commons-runtime/3.0.8/istack-commons-runtime-3.0.8.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/com/thoughtworks/paranamer/paranamer/2.8/paranamer-2.8.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/com/twitter/chill-java/0.10.0/chill-java-0.10.0.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/com/twitter/chill_2.12/0.10.0/chill_2.12-0.10.0.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/com/univocity/univocity-parsers/2.9.1/univocity-parsers-2.9.1.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/commons-codec/commons-codec/1.16.1/commons-codec-1.16.1.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/commons-collections/commons-collections/3.2.2/commons-collections-3.2.2.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/commons-io/commons-io/2.15.1/commons-io-2.15.1.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/commons-logging/commons-logging/1.1.3/commons-logging-1.1.3.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/dev/ludovic/netlib/arpack/3.0.3/arpack-3.0.3.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/dev/ludovic/netlib/blas/3.0.3/blas-3.0.3.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/dev/ludovic/netlib/lapack/3.0.3/lapack-3.0.3.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/io/airlift/aircompressor/0.25/aircompressor-0.25.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/io/dropwizard/metrics/metrics-core/4.2.19/metrics-core-4.2.19.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/io/dropwizard/metrics/metrics-graphite/4.2.19/metrics-graphite-4.2.19.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/io/dropwizard/metrics/metrics-jmx/4.2.19/metrics-jmx-4.2.19.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/io/dropwizard/metrics/metrics-json/4.2.19/metrics-json-4.2.19.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/io/dropwizard/metrics/metrics-jvm/4.2.19/metrics-jvm-4.2.19.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/io/minio/minio/8.5.10/minio-8.5.10.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/io/netty/netty-all/4.1.96.Final/netty-all-4.1.96.Final.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/io/netty/netty-buffer/4.1.96.Final/netty-buffer-4.1.96.Final.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/io/netty/netty-codec-http2/4.1.96.Final/netty-codec-http2-4.1.96.Final.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/io/netty/netty-codec-http/4.1.96.Final/netty-codec-http-4.1.96.Final.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/io/netty/netty-codec-socks/4.1.96.Final/netty-codec-socks-4.1.96.Final.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/io/netty/netty-codec/4.1.96.Final/netty-codec-4.1.96.Final.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/io/netty/netty-common/4.1.96.Final/netty-common-4.1.96.Final.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/io/netty/netty-handler-proxy/4.1.96.Final/netty-handler-proxy-4.1.96.Final.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/io/netty/netty-handler/4.1.96.Final/netty-handler-4.1.96.Final.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/io/netty/netty-resolver/4.1.96.Final/netty-resolver-4.1.96.Final.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/io/netty/netty-transport-classes-epoll/4.1.96.Final/netty-transport-classes-epoll-4.1.96.Final.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/io/netty/netty-transport-classes-kqueue/4.1.96.Final/netty-transport-classes-kqueue-4.1.96.Final.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/io/netty/netty-transport-native-epoll/4.1.96.Final/netty-transport-native-epoll-4.1.96.Final.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/io/netty/netty-transport-native-epoll/4.1.96.Final/netty-transport-native-epoll-4.1.96.Final-linux-aarch_64.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/io/netty/netty-transport-native-epoll/4.1.96.Final/netty-transport-native-epoll-4.1.96.Final-linux-x86_64.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/io/netty/netty-transport-native-kqueue/4.1.96.Final/netty-transport-native-kqueue-4.1.96.Final-osx-aarch_64.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/io/netty/netty-transport-native-kqueue/4.1.96.Final/netty-transport-native-kqueue-4.1.96.Final-osx-x86_64.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/io/netty/netty-transport-native-unix-common/4.1.96.Final/netty-transport-native-unix-common-4.1.96.Final.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/io/netty/netty-transport/4.1.96.Final/netty-transport-4.1.96.Final.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/jakarta/annotation/jakarta.annotation-api/1.3.5/jakarta.annotation-api-1.3.5.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/jakarta/servlet/jakarta.servlet-api/4.0.3/jakarta.servlet-api-4.0.3.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/jakarta/validation/jakarta.validation-api/2.0.2/jakarta.validation-api-2.0.2.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/jakarta/ws/rs/jakarta.ws.rs-api/2.1.6/jakarta.ws.rs-api-2.1.6.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/jakarta/xml/bind/jakarta.xml.bind-api/2.3.2/jakarta.xml.bind-api-2.3.2.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/javax/activation/activation/1.1.1/activation-1.1.1.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/joda-time/joda-time/2.12.5/joda-time-2.12.5.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/net/razorvine/pickle/1.3/pickle-1.3.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/net/sf/opencsv/opencsv/2.3/opencsv-2.3.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/net/sf/py4j/py4j/0.10.9.7/py4j-0.10.9.7.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/net/sourceforge/f2j/arpack_combined_all/0.1/arpack_combined_all-0.1.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/abego/treelayout/org.abego.treelayout.core/1.0.3/org.abego.treelayout.core-1.0.3.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/antlr/ST4/4.3.1/ST4-4.3.1.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/antlr/antlr-runtime/3.5.2/antlr-runtime-3.5.2.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/antlr/antlr4-runtime/4.9.3/antlr4-runtime-4.9.3.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/antlr/antlr4/4.9.3/antlr4-4.9.3.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/apache/arrow/arrow-format/12.0.1/arrow-format-12.0.1.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/apache/arrow/arrow-memory-core/12.0.1/arrow-memory-core-12.0.1.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/apache/arrow/arrow-memory-netty/12.0.1/arrow-memory-netty-12.0.1.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/apache/arrow/arrow-vector/12.0.1/arrow-vector-12.0.1.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/apache/avro/avro-ipc/1.11.2/avro-ipc-1.11.2.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/apache/avro/avro-mapred/1.11.2/avro-mapred-1.11.2.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/apache/avro/avro/1.11.2/avro-1.11.2.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/apache/commons/commons-collections4/4.4/commons-collections4-4.4.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/apache/commons/commons-compress/1.26.0/commons-compress-1.26.0.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/apache/commons/commons-crypto/1.1.0/commons-crypto-1.1.0.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/apache/commons/commons-lang3/3.14.0/commons-lang3-3.14.0.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/apache/commons/commons-math3/3.6.1/commons-math3-3.6.1.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/apache/commons/commons-text/1.10.0/commons-text-1.10.0.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/apache/curator/curator-client/2.13.0/curator-client-2.13.0.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/apache/curator/curator-framework/2.13.0/curator-framework-2.13.0.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/apache/curator/curator-recipes/2.13.0/curator-recipes-2.13.0.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/apache/datasketches/datasketches-java/3.3.0/datasketches-java-3.3.0.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/apache/datasketches/datasketches-memory/2.1.0/datasketches-memory-2.1.0.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.3.4/hadoop-aws-3.3.4.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/apache/hadoop/hadoop-client-api/3.3.4/hadoop-client-api-3.3.4.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/apache/hadoop/hadoop-client-runtime/3.3.4/hadoop-client-runtime-3.3.4.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/apache/hive/hive-storage-api/2.8.1/hive-storage-api-2.8.1.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/apache/iceberg/iceberg-spark-extensions-3.5_2.12/1.5.2/iceberg-spark-extensions-3.5_2.12-1.5.2.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/apache/iceberg/iceberg-spark-runtime-3.5_2.12/1.5.2/iceberg-spark-runtime-3.5_2.12-1.5.2.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/apache/ivy/ivy/2.5.1/ivy-2.5.1.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/apache/logging/log4j/log4j-1.2-api/2.20.0/log4j-1.2-api-2.20.0.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/apache/logging/log4j/log4j-api/2.20.0/log4j-api-2.20.0.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/apache/logging/log4j/log4j-core/2.20.0/log4j-core-2.20.0.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/apache/logging/log4j/log4j-slf4j2-impl/2.20.0/log4j-slf4j2-impl-2.20.0.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/apache/orc/orc-core/1.9.2/orc-core-1.9.2-shaded-protobuf.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/apache/orc/orc-mapreduce/1.9.2/orc-mapreduce-1.9.2-shaded-protobuf.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/apache/orc/orc-shims/1.9.2/orc-shims-1.9.2.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/apache/parquet/parquet-column/1.13.1/parquet-column-1.13.1.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/apache/parquet/parquet-common/1.13.1/parquet-common-1.13.1.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/apache/parquet/parquet-encoding/1.13.1/parquet-encoding-1.13.1.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/apache/parquet/parquet-format-structures/1.13.1/parquet-format-structures-1.13.1.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/apache/parquet/parquet-hadoop/1.13.1/parquet-hadoop-1.13.1.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/apache/parquet/parquet-jackson/1.13.1/parquet-jackson-1.13.1.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/apache/spark/spark-catalyst_2.12/3.5.1/spark-catalyst_2.12-3.5.1.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/apache/spark/spark-common-utils_2.12/3.5.1/spark-common-utils_2.12-3.5.1.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/apache/spark/spark-core_2.12/3.5.1/spark-core_2.12-3.5.1.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/apache/spark/spark-graphx_2.12/3.5.1/spark-graphx_2.12-3.5.1.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/apache/spark/spark-kvstore_2.12/3.5.1/spark-kvstore_2.12-3.5.1.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/apache/spark/spark-launcher_2.12/3.5.1/spark-launcher_2.12-3.5.1.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/apache/spark/spark-mllib-local_2.12/3.5.1/spark-mllib-local_2.12-3.5.1.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/apache/spark/spark-mllib_2.12/3.5.1/spark-mllib_2.12-3.5.1.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/apache/spark/spark-network-common_2.12/3.5.1/spark-network-common_2.12-3.5.1.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/apache/spark/spark-network-shuffle_2.12/3.5.1/spark-network-shuffle_2.12-3.5.1.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/apache/spark/spark-sketch_2.12/3.5.1/spark-sketch_2.12-3.5.1.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/apache/spark/spark-sql-api_2.12/3.5.1/spark-sql-api_2.12-3.5.1.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/apache/spark/spark-sql_2.12/3.5.1/spark-sql_2.12-3.5.1.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/apache/spark/spark-streaming_2.12/3.5.1/spark-streaming_2.12-3.5.1.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/apache/spark/spark-tags_2.12/3.5.1/spark-tags_2.12-3.5.1.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/apache/spark/spark-unsafe_2.12/3.5.1/spark-unsafe_2.12-3.5.1.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/apache/xbean/xbean-asm9-shaded/4.23/xbean-asm9-shaded-4.23.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/apache/yetus/audience-annotations/0.13.0/audience-annotations-0.13.0.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/apache/zookeeper/zookeeper-jute/3.6.3/zookeeper-jute-3.6.3.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/apache/zookeeper/zookeeper/3.6.3/zookeeper-3.6.3.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/bouncycastle/bcprov-jdk18on/1.78/bcprov-jdk18on-1.78.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/checkerframework/checker-qual/3.37.0/checker-qual-3.37.0.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/codehaus/janino/commons-compiler/3.1.9/commons-compiler-3.1.9.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/codehaus/janino/janino/3.1.9/janino-3.1.9.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/fusesource/leveldbjni/leveldbjni-all/1.8/leveldbjni-all-1.8.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/glassfish/hk2/external/aopalliance-repackaged/2.6.1/aopalliance-repackaged-2.6.1.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/glassfish/hk2/external/jakarta.inject/2.6.1/jakarta.inject-2.6.1.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/glassfish/hk2/hk2-api/2.6.1/hk2-api-2.6.1.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/glassfish/hk2/hk2-locator/2.6.1/hk2-locator-2.6.1.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/glassfish/hk2/hk2-utils/2.6.1/hk2-utils-2.6.1.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/glassfish/hk2/osgi-resource-locator/1.0.3/osgi-resource-locator-1.0.3.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/glassfish/jaxb/jaxb-runtime/2.3.2/jaxb-runtime-2.3.2.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/glassfish/jersey/containers/jersey-container-servlet-core/2.40/jersey-container-servlet-core-2.40.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/glassfish/jersey/containers/jersey-container-servlet/2.40/jersey-container-servlet-2.40.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/glassfish/jersey/core/jersey-client/2.40/jersey-client-2.40.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/glassfish/jersey/core/jersey-common/2.40/jersey-common-2.40.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/glassfish/jersey/core/jersey-server/2.40/jersey-server-2.40.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/glassfish/jersey/inject/jersey-hk2/2.40/jersey-hk2-2.40.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/glassfish/javax.json/1.0.4/javax.json-1.0.4.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/javassist/javassist/3.29.2-GA/javassist-3.29.2-GA.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/jetbrains/kotlin/kotlin-stdlib-common/1.9.10/kotlin-stdlib-common-1.9.10.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/jetbrains/kotlin/kotlin-stdlib-jdk7/1.9.10/kotlin-stdlib-jdk7-1.9.10.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/jetbrains/kotlin/kotlin-stdlib-jdk8/1.9.10/kotlin-stdlib-jdk8-1.9.10.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/jetbrains/kotlin/kotlin-stdlib/1.9.10/kotlin-stdlib-1.9.10.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/jetbrains/annotations/17.0.0/annotations-17.0.0.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/json4s/json4s-ast_2.12/3.7.0-M11/json4s-ast_2.12-3.7.0-M11.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/json4s/json4s-core_2.12/3.7.0-M11/json4s-core_2.12-3.7.0-M11.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/json4s/json4s-jackson_2.12/3.7.0-M11/json4s-jackson_2.12-3.7.0-M11.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/json4s/json4s-scalap_2.12/3.7.0-M11/json4s-scalap_2.12-3.7.0-M11.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/lz4/lz4-java/1.8.0/lz4-java-1.8.0.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/objenesis/objenesis/2.5.1/objenesis-2.5.1.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/roaringbitmap/RoaringBitmap/1.0.1/RoaringBitmap-1.0.1.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/rocksdb/rocksdbjni/8.3.2/rocksdbjni-8.3.2.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/scala-lang/modules/scala-collection-compat_2.12/2.11.0/scala-collection-compat_2.12-2.11.0.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/scala-lang/modules/scala-parser-combinators_2.12/2.3.0/scala-parser-combinators_2.12-2.3.0.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/scala-lang/modules/scala-xml_2.12/2.1.0/scala-xml_2.12-2.1.0.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/scala-lang/scala-library/2.12.19/scala-library-2.12.19.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/scala-lang/scala-reflect/2.12.19/scala-reflect-2.12.19.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/scalanlp/breeze-macros_2.12/2.1.0/breeze-macros_2.12-2.1.0.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/scalanlp/breeze_2.12/2.1.0/breeze_2.12-2.1.0.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/scodec/scodec-bits_2.12/1.1.38/scodec-bits_2.12-1.1.38.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/slf4j/jcl-over-slf4j/2.0.7/jcl-over-slf4j-2.0.7.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/slf4j/jul-to-slf4j/2.0.7/jul-to-slf4j-2.0.7.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/slf4j/log4j-over-slf4j/2.0.13/log4j-over-slf4j-2.0.13.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/slf4j/slf4j-api/2.0.13/slf4j-api-2.0.13.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/slf4j/slf4j-reload4j/2.0.13/slf4j-reload4j-2.0.13.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/threeten/threeten-extra/1.7.1/threeten-extra-1.7.1.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/tukaani/xz/1.9/xz-1.9.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/typelevel/algebra_2.12/2.0.1/algebra_2.12-2.0.1.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/typelevel/cats-core_2.12/2.10.0/cats-core_2.12-2.10.0.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/typelevel/cats-effect-kernel_2.12/3.5.4/cats-effect-kernel_2.12-3.5.4.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/typelevel/cats-effect-std_2.12/3.5.4/cats-effect-std_2.12-3.5.4.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/typelevel/cats-effect_2.12/3.5.4/cats-effect_2.12-3.5.4.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/typelevel/cats-kernel_2.12/2.10.0/cats-kernel_2.12-2.10.0.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/typelevel/literally_2.12/1.1.0/literally_2.12-1.1.0.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/typelevel/spire-macros_2.12/0.17.0/spire-macros_2.12-0.17.0.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/typelevel/spire-platform_2.12/0.17.0/spire-platform_2.12-0.17.0.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/typelevel/spire-util_2.12/0.17.0/spire-util_2.12-0.17.0.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/typelevel/spire_2.12/0.17.0/spire_2.12-0.17.0.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/wildfly/openssl/wildfly-openssl/1.0.7.Final/wildfly-openssl-1.0.7.Final.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/org/xerial/snappy/snappy-java/1.1.10.5/snappy-java-1.1.10.5.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/oro/oro/2.0.8/oro-2.0.8.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/pl/edu/icm/JLargeArrays/1.5/JLargeArrays-1.5.jar:/Users/mimischly/Library/Caches/Coursier/v1/https/repo1.maven.org/maven2/software/amazon/awssdk/bundle/2.23.19/bundle-2.23.19.jar")
