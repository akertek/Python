from django.test import TestCase
from .models import Kitap, Yazar
from django.core.management import call_command
from django.db.models import Q 
# Create your tests here.


class StringTestCase(TestCase):
    def test_upper(self):
        self.assertEqual("ABC", "abc".upper())

    def test_lower(self):
        self.assertEqual("abc", "ABC".lower())


class DataTestCase(TestCase):
    """
    python manage.py loaddata kitaplar.yaml

    from django.core.management import call_command
    """

    def setUp(self):
        call_command("loaddata", "yazarlar.yaml")
        call_command("loaddata", "kitaplar.yaml")

    def tearDown(self):
        pass

    def test_kitap_count(self):
        # kitap tablosunda birden fazla kayıt olduğunu test eder.
        kitaplar = Kitap.objects.all()

        self.assertGreater(len(kitaplar), 0)
        self.assertEqual(3, len(kitaplar))

    def test_kitap_contains_str1(self):
        kitaplar = Kitap.objects.filter(
            notlar__icontains="in").order_by("-notlar")
        kac_kitap = Kitap.objects.filter(notlar__icontains="in").exclude(
            notlar__icontains="veri").count()

        for kitap in kitaplar:
            print("*******", kitap, "*******")
        self.assertEqual(1, kac_kitap)

    def test_kitap_contains_str2(self):
        kac_kitap = Kitap.objects.filter(notlar__icontains="in").count()
        self.assertEqual(2, kac_kitap)

    def test_kitap_iendswith(self):
        kac_tane = Kitap.objects.filter(notlar__iendswith=".").count()
        self.assertEqual(3, kac_tane)

    def test_multiple_lookup(self):
        kac_tane = Kitap.objects.filter(
            notlar__icontains="in", adi__icontains="robot").count()
        self.assertEqual(1, kac_tane)

    def test_get1(self):
        count1 = Yazar.objects.all().count()
        Yazar.objects.get(pk=2).delete()
        count2 = Yazar.objects.all().count()

        self.assertEqual(count2 + 1, count1)

        # yazar1 = Yazar.objects.get(tc_kimlik_no = 112)
        # yazar2 = Yazar.objects.get(id = 3)
        # yazar3 = Yazar.objects.get(pk = 2)
        # yazar4 = Yazar.objects.get(pk = 99)    # Does not exist hatası fırlatır.

    def test_or(self):

        yazarlar1 = Yazar.objects.filter(adi__icontains="ac")
        yazarlar2 = Yazar.objects.filter(adi__icontains="oy")

        yazarlar3 = yazarlar1 | yazarlar2

        self.assertEqual(2, yazarlar3.count())

        # from django.db.models import Q 
        sorgu = Q(adi__icontains = "ac") | Q(adi__icontains = "oy")

        yazarlar4 = Yazar.objects.filter(sorgu)
        self.assertEqual(2, yazarlar4.count())

    def test_raw_sql(self):
        sql = r"SELECT * FROM kitaplar_kitap WHERE adi = 'Üç Robot Yasası'"
        data = Kitap.objects.raw(sql)
        self.assertEqual(1, len(data))
 