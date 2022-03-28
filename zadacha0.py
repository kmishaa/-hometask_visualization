data['year']=data.date.str[6:10]
sum_comments = data.groupby("year")['comments'].apply(lambda x: x.sum())

plt.plot(sum_comments)
sum_comments
