import module

module.auth()

JQL = 'project = ARN AND status = Done AND fixVersion = null'
a = module.auth.Jira.jql(JQL)