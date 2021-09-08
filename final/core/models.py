from django.db import models
# Create your models here.


class Shape(models.Model):
    class Meta:
        abstract = True


class Triangle(Shape):
    baseLength = models.PositiveIntegerField(blank=False, null=False)
    height = models.PositiveIntegerField(blank=False, null=False)
    sideA = models.PositiveIntegerField(blank=False, null=False)
    sideB = models.PositiveIntegerField(blank=False, null=False)
    sideC = models.PositiveIntegerField(blank=False, null=False)

    @property
    def area(self):
        return self.baseLength * self.height / 2

    @property
    def perimeter(self):
        return self.sideA + self.sideB + self.sideC


class four_side(Shape):
    sideLeft = models.PositiveIntegerField(blank=False, null=False)
    sideRight = models.PositiveIntegerField(blank=False, null=False)
    sideTop = models.PositiveIntegerField(blank=False, null=False)
    sideBottom = models.PositiveIntegerField(blank=False, null=False)

    class Meta:
        abstract = True

    @property
    def area(self):
        pass

    @property
    def perimeter(self):
        return self.sideLeft + self.sideTop + self.sideRight + self.sideBottom


class Rectangle(four_side):
    @property
    def area(self):
        return self.sideLeft * self.sideTop


class Square(four_side):
    @property
    def area(self):
        return self.sideLeft * self.sideTop


class Diamond(four_side):
    diagonalLength_1 = models.PositiveIntegerField(blank=False, null=False)
    diagonalLength_2 = models.PositiveIntegerField(blank=False, null=False)

    @property
    def area(self):
        return self.diagonalLength_1 * self.diagonalLength_2 / 2
