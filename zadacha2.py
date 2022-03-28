sex = ['Male', 'Female']

sum_tips = tips.groupby("sex")['tip'].apply(lambda x: x.sum())
_ = plt.bar(sex, sum_tips, color = 'black', )
plt.title('Tips per gender')
_ = plt.xlabel('gender')
_ = plt.ylabel('sum of tips')
