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
		for i in range(len(hash_bucket)):
			if hash_bucket[i][0] == dic_key:
				hash_bucket[i] = (dic_key,dic_val)
				return
		hash_bucket.append((dic_key,dic_val))

	def get_value(self, dic_key):
		hash_bucket = self.buckets[dic_key%self.num_buckets]
		for n in hash_bucket:
			if n[0] == dic_key:
				return n[1]
		return None

	def __str__(self):
		result = '{'
		for b in self.buckets:
			for e in b:
				result = result + str(e[0]) + ':' + str(e[1]) + ','
		return result[:-1] + '}' 