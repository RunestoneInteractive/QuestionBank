.. codelens:: Invoice2
  :author: bmiller
  :difficulty: 3.0
  :basecourse: StudentCSP
  :chapter: CSPNameNumbers
  :subchapter: invoice
  :topics: CSPNameNumbers/invoice
  :from_source: T

  quantity = 2
  unitPrice = 7.56
  total1 = quantity * unitPrice
  quantity = 4
  unitPrice = 4.71
  total2 = quantity * unitPrice
  invoiceTotal = total1 + total2
  print(invoiceTotal)