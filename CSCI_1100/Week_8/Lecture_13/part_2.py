

input_file = input("Enter the scores file: ")
print(input_file)
output_file = input("Enter the output file: ")
print(output_file)

# input_file = "scores.txt"
# output_file = "result.txt"
scores_collection = []
for line in open(input_file):
	m = line.strip().split()
	scores_collection.append(int(m[0]))

scores_collection = sorted(scores_collection)
# print(scores_collection)
output_file = open(output_file,"w")

for i in range(len(scores_collection)):
	output_file.write("{}:{:4d}\n".format(i,scores_collection[i]))



