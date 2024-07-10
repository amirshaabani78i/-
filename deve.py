menu_koli = input()
h = menu_koli.replace(' ', ',')
m = h.split(',')
dic_aval = dict(zip(m[0::2], map(float, m[1::2])))

from collections import defaultdict
l1=[]
l2=[]
while True:
    f=input()
    if f.lower()=="end":
        break

    p=f.split(",")
    for z in p:
        o=z.split(" ")
        l1.extend((o[0::2]))
        l2.extend(map(float,o[1::2]))
        
dic_dovom = defaultdict(float)

for key,value in zip(l1,l2):
      dic_dovom[key] += value

for e in dic_aval.keys():
    if e in dic_dovom.keys():
        print(e ,round(dic_aval[e]*dic_dovom[e],2) )
    else:
        print(e,float(0*1))


li class="nav-item"><a href="privacy-policy.html" class="nav-link">سیاست حفظ حریم خصوصی</a></li>
<li class="nav-item"><a href="terms-conditions.html" class="nav-link">شرایط و ضوابط</a></li>
<li class="nav-item"><a href="404.html" class="nav-link">خطا</a></li>
<li class="nav-item"><a href="contact-us.html" class="nav-link">با ما تماس بگیرید</a></li>
</ul>
</li>
<li class="nav-item">
<a href="#" class="nav-link dropdown-toggle">خدمات</a><ul class="dropdown-menu">
<li class="nav-item"><a href="services.html" class="nav-link">خدمات</a></li>
<li class="nav-item"><a href="service-details.html" class="nav-link">جزئیات خدمات</a></li>
</ul>
</li>
<li class="nav-item">
<a href="#" class="nav-link dropdown-toggle">مطالعه موردی</a><ul class="dropdown-menu">
<li class="nav-item"><a href="case-study.html" class="nav-link">مطالعه موردی</a></li>
<li class="nav-item"><a href="cases-study-details.html" class="nav-link">جزئیات مطالعه موردی</a></li>
</ul>
</li>
<li class="nav-item">
<a href="#" class="nav-link dropdown-toggle active">خرید کنید</a><ul class="dropdown-menu">
<li class="nav-item"><a href="products.html" class="nav-link">محصولات</a></li>
<li class="nav-item"><a href="cart.html" class="nav-link">سبد خرید</a></li>
<li class="nav-item"><a href="checkout.html" class="nav-link active">وارسی</a></li>
<li class="nav-item"><a href="product-details.html" class="nav-link">جزئیات محصول</a></li>
</ul>
</li>
<li class="nav-item">
<a href="#" class="nav-link dropdown-toggle">وبلاگ</a><ul class="dropdown-menu">
<li class="nav-item"><a href="blog.html" class="nav-link">وبلاگ</a></li>
<li class="nav-item"><a href="single-blog.html" class="nav-link">صفحه وبلاگ واحد</a></li>
</ul>
</li>
</ul>
<div class="nav-right-options d-flex align-items-center">
<div class="language position-relative z-1">
<select class="form-select" aria-label="Default select example"><option selected>انگلیسی</option>
<option value="1">عربی</option>
<option value="2">چین</option></select><i class="fa-light fa-globe"></i>
</div>
<ul class="social-link ps-0 mb-0 list-unstyled">
<li><a href="https://facebook.com/" target="_blank"><i class="fa-brands fa-facebook-f"></i></a></li>
<li><a href="https://twitter.com/" target="_blank"><i class="fa-brands fa-twitter"></i></a></li>
<li><a href="https://instagram.com/" target="_blank"><i class="fa-brands fa-instagram"></i></a></li>
<li><a href="https://linkedin.com/" target="_blank"><i class="fa-brands fa-linkedin-in"></i></a></li>
</ul>
</div>
</div></nav></div></div>
<div class="mobile-nav"><div class="container"><div class="mobile-menu"><div class="logo"><a href="index.html"><img src="assets/images/white-logo.svg" alt="logo"></a></div></div></div></div>
</div>
<div class="page-banner-area bg-black bg-img" data-background="./assets/images/banner-bg-shape.png"><div class="container mw-1680"><div class="page-banner-content">
<h2>checkout</h2>
<ul class="ps-0 mb-0 list-unstyled justify-content-center page-breadcrumb d-flex flex-wrap gap-4">
<li><a href="index.html">صفحه اصلی</a></li>
<li><span class="active">checkout</span></li>
</ul>
</div></div></div>
<div class="checkout-area pt-100 pb-75"><div class="container"><div class="row">
<div class="col-lg-7 col-xxl-8"><div class="checkout-form">
<h3>جزئیات صورتحساب</h3>
<form>
<h4>اطلاعات تماس</h4>
<div class="row">
<div class="col-lg-12"><div class="form-group mb-4"><input type="email" class="form-control" placeholder="آدرس ایمیل"></div></div>
<div class="col-lg-12"><div class="form-group mb-4"><div class="form-check">
<input class="form-check-input" type="checkbox" value="" id="flexCheckDefault1"><label class="form-check-label" for="flexCheckDefault1">اخبار و پیشنهادات را برای من ایمیل کنید</label>
</div></div></div>
<div class="col-lg-12"><h4>آدرس حمل و نقل</h4></div>
<div class="col-lg-6"><div class="form-group mb-4"><input type="text" class="form-control" placeholder="نام کوچک"></div></div>
<div class="col-lg-6"><div class="form-group mb-4"><input type="text" class="form-control" placeholder="نام خانوادگی"></div></div>
<div class="col-lg-12"><div class="form-group mb-4"><input type="text" class="form-control" placeholder="کشور / منطقه"></div></div>
<div class="col-lg-12"><div class="form-group mb-4"><input type="text" class="form-control" placeholder="آدرس خیابان"></div></div>
<div class="col-lg-12"><div class="form-group mb-4"><input type="text" class="form-control" placeholder="آپارتمان، سوئیت، واحد و غیره (اختیاری)"></div></div>
<div class="col-lg-12"><div class="form-group mb-4"><input type="text" class="form-control" placeholder="شهر / شهر"></div></div>
<div class="col-lg-12"><div class="form-group mb-4"><input type="text" class="form-control" placeholder="کشور (اختیاری)"></div></div>
<div class="col-lg-12"><div class="form-group mb-4"><input type="text" class="form-control" placeholder="کد پستی"></div></div>
<div class="col-lg-12"><div class="form-group mb-4"><input type="text" class="form-control" placeholder="تلفن"></div></div>
<div class="col-lg-12"><div class="form-group mb-4"><div class="d-flex gap-4">
<div class="form-check">
<input class="form-check-in