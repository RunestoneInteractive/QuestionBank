.. activecode:: structured_addr_1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcspy
    :chapter: Inheritance
    :subchapter: 07-CaseStudy
    :topics: Inheritance/07-CaseStudy
    :from_source: T

    class StructuredAddress:
        def __init__(self, country, recipient, street, city, state, postalCode):
            self.country = country
            self.recipient = recipient
            self.street = street
            self.city = city
            self.state = state
            self.postalCode = postalCode

        def display(self):
            print(self.recipient)
            print(self.street)
            print(self.city + ", " + self.state + "  " + self.postalCode)
            print(self.country)

    addr = StructuredAddress('USA', 'Abe Jones', '103 Anywhere Ln',
                   'Greenville', 'SC', '29609')
    addr.display()