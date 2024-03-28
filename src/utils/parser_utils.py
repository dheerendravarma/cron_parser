from typing import List


def get_minute_component(expr: str) -> List:
    expr_length = len(expr)
    if expr_length == 1:
        if expr.isnumeric():
            return [int(expr)]
        if expr == '*':
            return list(range(60))
    if "/" in expr:
        expr_components = expr.split("/")
        range_value = expr_components[1]
        start_value = expr_components[0]
        if start_value == '*':
            return list(range(0,60,range_value))
        else:
            return list(range(start_value, 60, range_value))
    elif "-" in expr:
        expr_components = expr.split("-")
        start_value = expr_components[0]
        end_value = expr_components[0]
        return list(start_value, end_value+1)

def get_hour_component(expr: str) -> List:
    pass

def get_dom_component(expr: str) -> List:
    pass

def get_month_component(expr: str) -> List:
    pass

def get_dow_component(expr: str) -> List:
    pass
