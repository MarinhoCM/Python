import unittest

from main import FindDomain

class TestFindDomain(unittest.TestCase):
    def test_get_domain(self) -> None:
        domain1 = FindDomain("8.8.8.8")
        domain2 = FindDomain("8.8.4.4")
        
        self.assertEquals(domain1.get_domain(), "dns.google")
        self.assertEquals(domain2.get_domain(), "dns.google")
        
if __name__ == "__main__":
    unittest.main()
