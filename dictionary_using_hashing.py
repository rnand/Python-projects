class IntegerDict(object):

	def __init__(self,num_buckets):
		#Create an empty dictionary
		self.buckets = []
		self.num_buckets = num_buckets
		for i in range(num_buckets):
			self.buckets.append([])
	def add_entry(self,dic_key,dic_val):
		#dic_key is an integer
		hash_bucket=self.buckets[dic_key%self.num_buckets]
		for