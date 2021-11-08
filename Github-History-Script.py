import pandas as pd

pulls = pulls_one.append(pulls_two,ignore_index=True)
pulls['date'] = pd.to_datetime(pulls['date'],utc=True)
data = pulls.merge(pull_files,on='pid')
data['month'] = data['date'].dt.month
data['year'] = data['date'].dt.year
counts = data.groupby(['month','year'])['pid'].count()
counts.plot(kind='bar', figsize = (12,4))

%matplotlib inline
by_user = data.groupby('user').agg({'pid':'count'})
by_user.hist()
by_user

last_10 = pulls.sort_values(by='date').tail(10)
joined_pr = pull_files.merge(last_10,on='pid')
files = set(joined_pr['file'])
files

file_pr = data[data['file']==file]
author_counts = file_pr.groupby('user').count()
author_counts.nlargest(3,'file')

file_pr = pull_files[pull_files['file']==file]
joined_pr = pulls.merge(file_pr, on='pid')
users_last_10 = set(joined_pr.nlargest(10, 'date')['user'])
file_pr = pull_files[pull_files['file']==file]
joined_pr = pulls.merge(file_pr, on='pid')
users_last_10 = set(joined_pr.nlargest(10, 'date')['user'])
users_last_10

authors = ['xeno-by', 'soc']
by_author = pulls[pulls['user'].isin(authors)]
counts = by_author.groupby([by_author['user'], by_author['date'].dt.year]).agg({'pid': 'count'}).reset_index()
counts_wide = counts.pivot_table(index='date', columns='user', values='pid', fill_value=0)
counts_wide.plot(kind='bar')

by_author = data[data['user'].isin(authors)]
by_file = by_author[by_author['file']==file]
grouped = by_file.groupby(['user', by_file['date'].dt.year]).count()['pid'].reset_index()
by_file_wide = grouped.pivot_table(index='date',columns='user',values='pid',fill_value=0)
by_file_wide.plot(kind='bar')

