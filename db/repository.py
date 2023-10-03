from .repo import SqliteRepository
from ..model.model import CompanyInfo


class Repo:
    def __init__(self):
        self.company_repo = SqliteRepository[CompanyInfo]("db.sqlite3")

    def get_contact_pages_for_company(self, name: str) -> list[str]:
        companies = self.company_repo.get_all(where={"name":name})
        if len(companies) == 0:
            return []
        company_info = companies[0]
        contact_pages = company_info.contacts.split(",")
        result_addresses = []
        for cp in contact_pages:
            result_addresses.append(company_info.address + "/" + cp)
        return result_addresses

