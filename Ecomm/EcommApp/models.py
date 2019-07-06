from django.db import models

class category(models.Model):
  # CategoryId = models.IntegerField()
  CategoryName = models.CharField(max_length=255)
  Discription = models.CharField(max_length=1000)
  Picture = models.CharField(max_length=500)
  Active = models.BooleanField()
  Created = models.DateTimeField()


class customers(models.Model):
    # CustomersId = models.IntegerField()
    Email = models.CharField(max_length=255)
    Password = models.CharField(max_length=255)
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    PhoneNo = models.IntegerField()
    DOB = models.CharField(max_length=100)
    Address = models.CharField(max_length=500)
    Country = models.CharField(max_length=100)
    State = models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    PinCode = models.IntegerField()
    Gender = models.CharField(max_length=100)
    ProfileImg = models.CharField(max_length=100)
    created = models.DateTimeField()

class products(models.Model):
    # ProductId = models.IntegerField(primary_key=True)
    SKU = models.CharField(max_length=100)
    ProductName = models.CharField(max_length=100)
    ProductDes = models.CharField(max_length=1000)
    SupplierId = models.IntegerField()
    categoryId = models.ForeignKey(category, on_delete=models.CASCADE)
    QuantityPerUnit = models.IntegerField()
    UnitPrice = models.IntegerField()
    MSRP = models.IntegerField()
    AvilSize = models.CharField(max_length=100)
    AvilColor = models.CharField(max_length=100)
    Size = models.IntegerField()
    Colour = models.CharField(max_length=100)
    UnitWeight = models.IntegerField()
    UnitInStock = models.IntegerField()
    UnitOnOrder = models.IntegerField()
    ProductAvil = models.BooleanField()
    DiscountAvil = models.BooleanField()
    picture = models.CharField(max_length=500)
    Ranking = models.IntegerField()
    Note = models.CharField(max_length=1000)
    Discount = models.IntegerField()
    created = models.DateTimeField()


class orderdetails(models.Model):
    # OrderId = models.IntegerField(primary_key=True)
    productId = models.ForeignKey(products, on_delete=models.CASCADE)
    OrderNumber = models.IntegerField()
    Price = models.IntegerField()
    Qantity = models.IntegerField()
    Total = models.IntegerField()
    Discount = models.IntegerField()
    Size = models.CharField(max_length=100)
    Colour = models.CharField(max_length=100)
    Fullfilled = models.CharField(max_length=100)
    ShipDate = models.CharField(max_length=100)
    OrderDetailId = models.CharField(max_length=100)
    created = models.DateTimeField()

class payment(models.Model):
    # PaymentId = models.IntegerField(primary_key=True)
    PaymentType = models.CharField(max_length=100)
    Allowed = models.CharField(max_length=100)
    created = models.DateTimeField()


class shippers(models.Model):
    # ShipperId = models.IntegerField(primary_key=True)
    CompanyName = models.CharField(max_length=100)
    PhoneNo = models.IntegerField()
    created = models.DateTimeField()


class orders(models.Model):
    # OrderId = models.IntegerField(primary_key=True)
    customerId = models.ForeignKey(customers, on_delete=models.CASCADE)
    OrderNumber = models.IntegerField()
    paymentId = models.ForeignKey(payment, on_delete=models.CASCADE)
    OrderDate = models.CharField(max_length=100)
    ShipDate = models.CharField(max_length=100)
    RequiredDate = models.CharField(max_length=100)
    ShipperId = models.IntegerField()
    Freight = models.CharField(max_length=100)
    TimeStamp = models.CharField(max_length=100)
    TransactionsStatus = models.BooleanField()
    ErrorMsg = models.CharField(max_length=500)
    Fullfilled = models.CharField(max_length=100)
    Deleted = models.BooleanField()
    Paid = models.BooleanField()
    PaymentDate = models.CharField(max_length=100)
    created = models.DateTimeField()


class cart(models.Model):
    customerId = models.ForeignKey(customers, on_delete=models.CASCADE)
    productId = models.ForeignKey(products, on_delete=models.CASCADE)
    cart = models.BooleanField()
    wshishlist = models.BooleanField()







