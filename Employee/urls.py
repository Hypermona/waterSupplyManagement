from django.urls import path

from Employee.views import home, login, signup, bill_gen, show_bill, display_corporator, payment, all_bill, update_form, \
    profile, update_return, add_complaint,meter

urlpatterns = [
    path('', home.index, name="homepage"),
    path('login', login.Login.as_view(), name="login"),
    path('signup', signup.Signup.as_view(), name="signup"),
    path('billGen', bill_gen.Billgen.as_view(), name="billgen"),
    path('showBill', show_bill.ShowBill.as_view(), name="showbill"),
    path('displayCorp', display_corporator.DisplayCorporator.as_view(), name="displaycorp"),
    path('payment', payment.Payment.as_view(), name="payment"),
    path('allBill', all_bill.ShowBill.as_view(), name="allbills"),
    path('updateForm', update_form.UpdateForm.as_view(), name="updateform"),
    path('profile', profile.Profile.as_view(), name="profile"),
    path('updateReturn', update_return.UpdateReturn.as_view(), name="updatereturn"),
    path('addComplaint', add_complaint.AddComplaint.as_view(), name="addcomplaint"),
    path('meter', meter.MeterUp.as_view(), name="meter"),
    path('logout', login.logout, name="logout"),
]
