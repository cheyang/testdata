import tensorflow as tf
import sys

def run(file_name):
	filename_queue = tf.train.string_input_producer([
    	file_name,
	])

	reader = tf.TextLineReader()
	key, value = reader.read(filename_queue)

	# Default values, in case of empty columns. Also specifies the type of the
	# decoded result.
	record_defaults = [[1], [1], [1], [1], [1], [1], [1], [1], [1], [1]]
	col1, col2, col3, col4, col5, col5, col6, col7, col8, col9 = tf.decode_csv(
    	value, record_defaults=record_defaults)
	features = tf.stack([col1, col2, col3, col4, col5, col6, col7, col8, col9])

	with tf.Session() as sess:
  		# Start populating the filename queue.
  	   coord = tf.train.Coordinator()
  	   threads = tf.train.start_queue_runners(coord=coord)

  	   for i in range(1200):
    	   # Retrieve a single instance:
    	     example, label = sess.run([features, col9])
    	     print(example)
    	     print(label)

  	   coord.request_stop()
  	   coord.join(threads)

if __name__ == "__main__":
  if len(sys.argv) <= 1:
  	raise Exception("Please input the hdfs url, like hdfs://192.168.1.97:9000/irs_train.csv")
  file_name = sys.argv[1]
  run(file_name)
  
