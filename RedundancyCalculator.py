import sys
from gooey import Gooey, GooeyParser
from dateutil import parser as p
import codecs
import re
from datetime import datetime

if sys.stdout.encoding != 'UTF-8':
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
if sys.stderr.encoding != 'UTF-8':
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

@Gooey(
    program_name="Redundancy Calculator",
    menu=[{
        'name': 'Help',
        'items': [{
            'type': 'AboutDialog',
            'menuTitle': 'About',
            'name': 'Redundancy Calculator Help.',
            'version': '2.0',
            'developer': 'James Poland'

        }, {
            'type': 'MessageDialog',
            'menuTitle': 'Information',
            'caption': 'Calculation Explainer',
            'message': 'Wages are capped at €600 per week as per Scheme'
        }, {
            'type': 'Link',
            'menuTitle': 'Calculations Derived from:',
            'url': 'https://www.gov.ie/en/publication/4be20-redundancy-calculation-examples/#example-1-redundancy-payments-scheme-calculation'
        }]
    }
    ]
)
def main():

    parser = GooeyParser(description="Calculate your Redundancy Package -By James Poland")
    today = datetime.today().strftime('%Y-%m-%d')
    g = parser.add_argument_group("EnterDetails Below to Calculate Redundancy Package.  Values are Estimated Only")
        # parsers = argparse.ArgumentParser(description='Calculate your Redundancy Package -By James Poland.')
        #parsers._optionals.title = "Add Your Details Here"
        #parsers.add_argument(
        #    "-s",
        #    "--startdate",
        #    help="The Start Date - format YYYY-MM-DD",
        #    required=True
        #    #type=valid_date
        #)
    g.add_argument('startdate', help='Enter date your term started, please use the calendar!', widget="DateChooser", default=today)
    g.add_argument('enddate', help='Enter date your term ends, please use the calendar!', widget="DateChooser", default=today )
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
    if "/" in str(end_date):
        end_date = datetime.strptime(end_date, '%d/%m/%Y').strftime('%Y-%m-%d')
    if "/" in str(start_date):
        start_date = datetime.strptime(start_date, '%d/%m/%Y').strftime('%Y-%m-%d')
                #wages = int(args['YearlySalary'])
    diff = (end_date - start_date)
    years = diff.days / 365.00
    weeksearned = ((diff.days/365.0)*2)+1
    # difference_in_days = abs((end_date - start_date).days)
    if years < 2:
        print("I'm sorry but you have worked less than minimum time for package")
        print("\r For more information please visit: \r https://www.citizensinformation.ie/en/employment/unemployment_and_redundancy/redundancy/redundancy_payments.html#:~:text=For%20example%2C%20statutory%20redundancy%20only,not%20through%20a%20statutory%20entitlement.")
    else:
        print("You have accrued " + str(round(years, 2)) + " years worth of service")
        if wagesclean/52 < 600 and years >=2:
            weekly = wagesclean/52
            redundo = round(weekly * weeksearned,2)
            print("You are entitled to €"+str(redundo) + " in redundancy" )
            print("\r For more information please visit: \r https://www.gov.ie/en/publication/4be20-redundancy-calculation-examples/#example-1-redundancy-payments-scheme-calculation")
        if wagesclean/52 > 600 and years >=2:
            weekly = 600
            redundo = round(weekly * weeksearned,2)
            print("\rGross weekly wage capped at €600 under scheme\r")
            print("You are entitled to €"+str(redundo) + " in redundancy" )
            print("\r For more information please visit: \r https://www.gov.ie/en/publication/4be20-redundancy-calculation-examples/#example-3-gross-weekly-wage-capped-at-600")

main()














