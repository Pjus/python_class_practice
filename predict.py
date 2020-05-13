import packages.class_parkjunsung as cla
import pickle

pre1 = cla.predict1()

pre2 = cla.predict2()

pre3 = cla.predict3()

pre4 = cla.predict4()

pickle.dump(pre1, open('./pre1.pkl', 'wb'))
pickle.dump(pre2, open('./pre2.pkl', 'wb'))
pickle.dump(pre3, open('./pre3.pkl', 'wb'))
pickle.dump(pre4, open('./pre4.pkl', 'wb'))


emp_pkl1 = pickle.load(open('./pre1.pkl', 'rb'))
emp_pkl2 = pickle.load(open('./pre2.pkl', 'rb'))
emp_pkl3 = pickle.load(open('./pre3.pkl', 'rb'))
emp_pkl4 = pickle.load(open('./pre4.pkl', 'rb'))

emp_pkl1.getPredict(7)
emp_pkl2.getPredict(7)
emp_pkl3.getPredict(7, 9)
emp_pkl4.getPredict(7, 9)