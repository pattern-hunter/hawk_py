from redis import Redis
from rq import Queue
from rq_scheduler import Scheduler
from datetime import datetime
import slackbot

# https://github.com/rq/rq-scheduler

scheduler = Scheduler('hawk', connection=Redis())

# scheduler.cron(
#     "*/10 * * * * *",
#     func=slackbot.daily_cleanup_list,
#     queue_name="hawk"
# )

list_of_job_instances = scheduler.get_jobs(with_times=True)
for obj in list_of_job_instances:
    # scheduler.cancel(obj[0].id)
    print(obj)