from requests import Session as sess

def get_page(address:str) -> str:
    # s = sess()
    with sess() as s:
        # address = 'https://repetitors.info'
        resp = s.get(address, timeout=2)
        return resp.text

def get_numbers(page:str) -> list:
    