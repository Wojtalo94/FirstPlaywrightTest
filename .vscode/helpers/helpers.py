from datetime import date
from dateutil.relativedelta import relativedelta


def refresh_and_wait(page):
    page.reload()
    page.wait_for_load_state("networkidle")


def date_months_back(months_back: int) -> str:
    target_date = date.today() - relativedelta(months=months_back)
    return target_date.strftime('%d/%m/%Y')


def date_months_forward(months_forward: int) -> str:
    target_date = date.today() + relativedelta(months=months_forward)
    return target_date.strftime('%d/%m/%Y')


def normalize_string(s: str) -> str:
    s = s.strip()
    s = re.sub(r"\s*-\s*", "-", s)
    s = re.sub(r"\s+", " ", s)
    return s
