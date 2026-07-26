# Solo Dev Notion Template

Productivity system for freelance developers and indie hackers.

## Database: Projects
- Status (Select: Planning, In Progress, Done, On Hold)
- Client (Relation → Clients)
- Deadline (Date)
- Priority (Select: P0, P1, P2, P3)
- Hours Logged (Number)
- Revenue (Number)
- Tags (Multi-select)

## Database: Tasks
- Status (Select: To Do, In Progress, Review, Done)
- Project (Relation → Projects)
- Assignee (People)
- Due Date (Date)
- Type (Select: Bug, Feature, Refactor, Docs)
- Estimated Hours (Number)

## Database: Clients
- Company (Title)
- Email (Email)
- Contract Type (Select: Hourly, Fixed)
- Rate (Number)
- Projects (Relation → Projects)

## Database: Meetings
- Date (Date)
- Type (Select: Standup, Client Call, Retrospective, Planning)
- Notes (Text)
- Action Items (Relation → Tasks)

## Views
- Weekly Dashboard: filtered view of tasks due this week
- Revenue Tracker: filtered projects with completed status
- Client Pipeline: grouped by client, filtered by active projects

## Setup Instructions
1. Duplicate this template in Notion
2. Replace placeholder data with your projects
3. Customize tags for your tech stack
4. Add the Calendar view for deadlines
5. Link your task database to the dashboard