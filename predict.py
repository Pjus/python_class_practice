import myClass.class_parkjunsung as cla
import pickle

# pre1 = cla.predict1()
# pre1.getPredict(3)

# pre2 = cla.predict2()
# pre2.getPredict(3)

# pre3 = cla.predict3()
# pre3.getPredict(3, 5)

# pre4 = cla.predict4()

# emp1 = pre1.getPredict(3)
# emp2 = pre2.getPredict(3)
# emp3 = pre3.getPredict(3, 5)

# pickle.dump(pre1, open('./pre1.pkl', 'wb'))
# pickle.dump(pre2, open('./pre2.pkl', 'wb'))
# pickle.dump(pre3, open('./pre3.pkl', 'wb'))

emp_pkl1 = pickle.load(open('./pre1.pkl', 'rb'))
emp_pkl2 = pickle.load(open('./pre2.pkl', 'rb'))
emp_pkl3 = pickle.load(open('./pre3.pkl', 'rb'))

emp_pkl1.getPredict(3)
emp_pkl2.getPredict(3)
emp_pkl3.getPredict(3, 5)