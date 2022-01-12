import sys
from gooey import Gooey, GooeyParser
from dateutil import parser as p
import codecs
import re

if sys.stdout.encoding != 'UTF-8':
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
if sys.stderr.encoding != 'UTF-8':
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

@Gooey
def main():
        parser = GooeyParser(description="Calculate your Redundancy Package -By James Poland")
        g = parser.add_argument_group("EnterDetails Below to Calculate Redundancy Package")
        # parsers = argparse.ArgumentParser(description='Calculate your Redundancy Package -By James Poland.')
        #parsers._optionals.title = "Add Your Details Here"
        #parsers.add_argument(
        #    "-s",
        #    "--startdate",
        #    help="The Start Date - format YYYY-MM-DD",
        #    required=True
        #    #type=valid_date
        #)
        g.add_argument('startdate', help='Enter date you started', widget="DateChooser")
        g.add_argument('enddate', help='Enter date your term ends', widget="DateChooser")
        g.add_argument('YearlySalary', help='Enter your yearly salary')
       # parsers.add_argument(
       #     "-e",
       #     "--enddate",
       #     help="The End Date - format YYYY-MM-DD",
       #     required=True
       #     #type=valid_date
       # )

        #parsers.add_argument(
        #    "-w",
        #    "--YearlySalary",
        #    help="This is your Yearly Salary",
       #     required=True
#
       # )
        args = vars(parser.parse_args())
        end_date = p.parse(args['enddate'])
        start_date = p.parse(args['startdate'])
        wages = args['YearlySalary']
        wagesclean = int(re.sub("[^\d\.]", "", wages))

        #wages = int(args['YearlySalary'])
        diff = (end_date - start_date)
        years = diff.days / 365.00
        weeksearned = ((diff.days/365.0)*2)+1
        # difference_in_days = abs((end_date - start_date).days)
        if years < 2:
            print("I'm sorry but you have worked less than minimum time for package")
        else:
            print("You have accrued " + str(round(years, 2)) + " years worth of service")
        if wagesclean/52 < 600 and years >=2:
            weekly = wagesclean/52
            redundo = round(weekly * weeksearned,2)
            print("You are entitled to €"+str(redundo) + " in redundancy" )
        if wagesclean/52 > 600 and years >=2:
            weekly = 600
            redundo = round(weekly * weeksearned,2)
            print("You are entitled to €"+str(redundo) + " in redundancy" )

main()














