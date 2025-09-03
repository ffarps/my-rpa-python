from Check_in_flow import check_in_flow
from modular01 import simplebot


def define_type_of_flow(type_of_flow):
    if type_of_flow == "checkin":
        check_in_flow()
        # simplebot()
