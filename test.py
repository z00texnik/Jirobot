from atlassian import Jira

jira = Jira(
    url='https://aptekarunew.atlassian.net/',
    username='katren.apteka.ru.jira@gmail.com',
    password="dJ57bvyQDzEaO6GCZTYk4C0E",
    cloud=True)

JQL = 'project = ARN AND status = Done AND fixVersion = null'

data = jira.jql(JQL)
print(data)

a = jira.csv(JQL)
print(a)