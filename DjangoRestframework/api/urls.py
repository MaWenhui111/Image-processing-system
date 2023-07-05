from django.urls import path
from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()  
router.register('ImageSet', views.ImageSet) 

urlpatterns = [
    path('resize/', views.resize.as_view(), name='resize'),
    path('rotate/', views.rotate.as_view(), name='rotate'),
    path('reversal/', views.reversal.as_view(), name='reversal'),
    path('translate/', views.translate.as_view(), name='translate'),
    path('crop/', views.crop.as_view(), name='crop'),
    path('gray/', views.gray.as_view(), name='gray'),
    path('logChange/', views.logChange.as_view(), name='logChange'),
    path('reverseChange/', views.reverseChange.as_view(), name='reverseChange'),
    path('gammaChange/', views.gammaChange.as_view(), name='gammaChange'),
    path('histogramToBalance/', views.histogramToBalance.as_view(), name='histogramToBalance'),
    path('linearChange/', views.linearChange.as_view(), name='linearChange'),
    path('contrast/', views.contrast.as_view(), name='contrast'),
    path('addSaltPepper/', views.addSaltPepper.as_view(), name='addSaltPepper'),
    path('addGaussian/', views.addGaussian.as_view(), name='addGaussian'),
    path('addrandom_mean/', views.addrandom_mean.as_view(), name='addrandom_mean'),
    path('filter/', views.filter.as_view(), name='filter'),
    path('Medianblur/', views.Medianblur.as_view(), name='Medianblur'),
    path('bilateralblur/', views.bilateralblur.as_view(), name='bilateralblur'),
    path('sharpenOne/', views.sharpenOne.as_view(), name='sharpenOne'),
    path('sharpenTwo/', views.sharpenTwo.as_view(), name='sharpenTwo'),
    path('Seg/', views.Seg.as_view(), name='Seg'),
    path('colorSeg/', views.colorSeg.as_view(), name='colorSeg'),
    path('rgbToHSI/', views.rgbToHSI.as_view(), name='rgbToHSI'),
    path('edge1/', views.edge1.as_view(), name='edge1'),
    path('edge2/', views.edge2.as_view(), name='edge2'),
    path('edgeColor/', views.edgeColor.as_view(), name='edgeColor'),
    path('AreaGrow/', views.AreaGrow.as_view(), name='AreaGrow'),
    path('bcsadjust/', views.bcsadjust.as_view(), name='bcsadjust'),
    path('hsvadjust/', views.hsvadjust.as_view(), name='hsvadjust'),
    path('addBorder/', views.addBorder.as_view(), name='addBorder'),
    path('Haze/', views.Haze.as_view(), name='Haze'),
    path('Featuredes/', views.Featuredes.as_view(), name='Featuredes'),
    path('motion/', views.motion.as_view(), name='motion'),
    path('wiener/', views.wiener.as_view(), name='wiener'),
    path('selfMedian/', views.selfMedian.as_view(), name='selfMedian'),
    path('selfMean/', views.selfMean.as_view(), name='selfMean'),
    path('fft/', views.fft.as_view(), name='fft'),
    path('lowFilter/', views.lowFilter.as_view(), name='lowFilter'),
    path('highFilter/', views.highFilter.as_view(), name='highFilter'),
    path('partition/', views.partition.as_view(), name='partition'),
    path('getHistArray/', views.getHistArray.as_view(), name='getHistArray'),
    path('new_/',views.new_.as_view(),name='new_'),
    path('', views.index.as_view(), name='index'),
]


urlpatterns += router.urls  
