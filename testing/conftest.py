

# import html
import pytest


@pytest.fixture(scope="module")#scope= class, module 
def setup():
   pass

def pytest_html_report_title(report):
    report.title = "My very own title"

# every thing u check in the documentation of this pytest 
#  "https://docs.pytest.org/en/6.2.x/fixture.html#scope-sharing-fixtures-across-classes-modules-packages-or-session"

# from xml  import html

# def pytest_html_result_summary(prefix,summary,postfix):
#     prefix.extend([html.p("adhfjklhdsfkhvkdhfgh")])
#     postfix.extend([html.p("fjdhjhfhhjhjhjhhhhhhhh")])
    