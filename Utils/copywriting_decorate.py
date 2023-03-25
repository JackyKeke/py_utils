def add_dividing_line(add_dividing_str):
    return f"{add_dividing_str}\n\n   ************ \n\n"


def add_new_line(add_new_line_str):
    return f"{add_new_line_str}\n\n "


def add_bold_line(add_bold_line_str):
    return f"**{add_bold_line_str}** "


def gen_form_columns(list):
    d = "| "
    for item in list:
        d += f" {item} |"
    d += "\n\n"
    return d


def add_form_indicator(num):
    d = "| "
    for i in range(num):
        d += " :---: |"
    d += "\n\n"
    return d

# def add_new_l_line(add_new_l_line_str):
#     return f" {add_new_l_line_str} |"
