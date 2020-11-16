import twint

c = twint.Config()
c.Search = 'APC'

c.Since = '2019-01-19'
c.Until = '2019-02-19'
c.Store_csv = True
#c.Output = 'data.csv'
c.Store_object = True
c.Limit = 10
twint.run.Search(c)

c_object = twint.output.tweets_list
print(c_object)