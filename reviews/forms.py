from django import forms
from .models import TouristReview

class ReviewForm(forms.ModelForm):
    class Meta:
        model = TouristReview
        fields = ['text', 'rating', 'image']
class TouristReview(models.Model):
    user = models.CharField(max_length=100)
    text = models.TextField()
    rating = models.IntegerField()
    image = models.ImageField(upload_to='static/media/review_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f'Review - {self.created_at}'