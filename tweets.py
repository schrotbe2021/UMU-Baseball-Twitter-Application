import twitter


api = twitter.Api(consumer_key='Kt4rgFjVqsEjUZ7hI2gogLgf3',
                      consumer_secret='XnFrW7acLminsGdPTgiGxpsnSqDdhSu311LDcc0YsTsWTc1hHw',
                      access_token_key='804787884893028356-INqdvH8AbSmHe24CMYN1x7d2neHlJDC',
                      access_token_secret='tMTzoop6zTHg0sEXPMeDSUylXxKELZWMvYjE6i06CoHiz')



def SayPioBoof():
    status = api.PostUpdate("pio boof")