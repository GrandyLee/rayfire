import pickle

pickle_file = open('my_list.pkl', 'rb')
my_list2 = pickle.load(pickle_file)
print(my_list2)
