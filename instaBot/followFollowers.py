"""
    instabot example
    Workflow:
        Follow user's followers by username.
"""

import argparse
import os
import sys

sys.path.append(os.path.join(sys.path[0], "../"))
from instabot import Bot  # noqa: E402

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument("-u", type=str, help="ingeniero_gualteros")
parser.add_argument("-p", type=str, help="*******")
parser.add_argument("-proxy", type=str, help="proxy")
parser.add_argument("users", type=str, nargs="+", help="fcbarcelona")
args = parser.parse_args()

bot = Bot(
    filter_users=True,
    filter_private_users=False,
    filter_previously_followed=True,
    filter_business_accounts=True,
    filter_verified_accounts=True,
)
bot.login(username=args.u, password=args.p, proxy=args.proxy)

for username in args.users:
    bot.follow_followers(args.user_id)