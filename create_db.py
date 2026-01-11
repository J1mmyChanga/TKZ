from data import db_session
from data.items import Items
from data.colors import Colors
from data.factures import Factures
from data.types import Types
from data.photos import Photos

db_session.global_init('db/tkz.db')
session = db_session.create_session()

s1 = Colors(color='Серый')
session.add(s1)
s2 = Colors(color='Фисташковый')
session.add(s2)
s3 = Colors(color='Красный')
session.add(s3)
s4 = Colors(color='Коричневый')
session.add(s4)
s5 = Colors(color='Графит')
session.add(s5)

s1 = Factures(facture='Гладкая')
session.add(s1)
s2 = Factures(facture='Финская')
session.add(s2)
s3 = Factures(facture='Старый город')
session.add(s3)
s4 = Factures(facture='Скала')
session.add(s4)
s5 = Factures(facture='Мраморная')
session.add(s5)
s6 = Factures(facture='Мраморная с фаской')
session.add(s6)
s7 = Factures(facture='Цокольная')
session.add(s7)
s8 = Factures(facture='Тротуарная гиперпрессованная плитка')
session.add(s8)

s1 = Types(typee='Кирпич')
session.add(s1)
s2 = Types(typee='Плитка')
session.add(s2)

i100 = Items(name='Кирпич гладкий', size='250x120x65', amount_per_meter=52, facture_id=1, typee_id=1,
             weight=4.4, amount=330, color_id=1, price_no_package=43, price_package=45)
i101 = Items(name='Кирпич гладкий', size='250x120x65', amount_per_meter=52, facture_id=1, typee_id=1,
             weight=4.4, amount=330, color_id=2, price_no_package=48, price_package=50)
i102 = Items(name='Кирпич гладкий', size='250x120x65', amount_per_meter=52, facture_id=1, typee_id=1,
             weight=4.4, amount=330, color_id=3, price_no_package=48, price_package=50)
i103 = Items(name='Кирпич гладкий', size='250x120x65', amount_per_meter=52, facture_id=1, typee_id=1,
             weight=4.4, amount=330, color_id=4, price_no_package=48, price_package=50)
i104 = Items(name='Кирпич гладкий', size='250x120x65', amount_per_meter=52, facture_id=1, typee_id=1,
             weight=4.4, amount=330, color_id=5, price_no_package=49, price_package=51)

i105 = Items(name='Кирпич гладкий угловой', size='250x120x65', facture_id=1, typee_id=1,
             weight=4.0, amount=330, color_id=1, price_no_package=43, price_package=45)
i106 = Items(name='Кирпич гладкий угловой', size='250x120x65', facture_id=1, typee_id=1,
             weight=4.0, amount=330, color_id=2, price_no_package=48, price_package=50)
i107 = Items(name='Кирпич гладкий угловой', size='250x120x65', facture_id=1, typee_id=1,
             weight=4.0, amount=330, color_id=3, price_no_package=48, price_package=50)
i108 = Items(name='Кирпич гладкий угловой', size='250x120x65', facture_id=1, typee_id=1,
             weight=4.0, amount=330, color_id=4, price_no_package=48, price_package=50)
i109 = Items(name='Кирпич гладкий угловой', size='250x120x65', facture_id=1, typee_id=1,
             weight=4.0, amount=330, color_id=5, price_no_package=49, price_package=51)

im1 = Photos(item_id=1, filepath='../static/uploads/items/1.png') #Кирпич гладкий
im2 = Photos(item_id=2, filepath='../static/uploads/items/2.png')
im3 = Photos(item_id=3, filepath='../static/uploads/items/3.png')
im4 = Photos(item_id=4, filepath='../static/uploads/items/4.png')
im5 = Photos(item_id=5, filepath='../static/uploads/items/5.png')

im6 = Photos(item_id=6, filepath='../static/uploads/items/6.png') #Кирпич гладкий угловой
im7 = Photos(item_id=7, filepath='../static/uploads/items/7.png')
im8 = Photos(item_id=8, filepath='../static/uploads/items/8.png')
im9 = Photos(item_id=9, filepath='../static/uploads/items/9.png')
im10 = Photos(item_id=10, filepath='../static/uploads/items/10.png')

i110 = Items(name='Кирпич гладкий 2-х угловой', size='250x120x65', facture_id=1, typee_id=1,
             weight=3.7, amount=330, color_id=1, price_no_package=43, price_package=45)
i111 = Items(name='Кирпич гладкий 2-х угловой', size='250x120x65', facture_id=1, typee_id=1,
             weight=3.7, amount=330, color_id=2, price_no_package=48, price_package=50)
i112 = Items(name='Кирпич гладкий 2-х угловой', size='250x120x65', facture_id=1, typee_id=1,
             weight=3.7, amount=330, color_id=3, price_no_package=48, price_package=50)
i113 = Items(name='Кирпич гладкий 2-х угловой', size='250x120x65', facture_id=1, typee_id=1,
             weight=3.7, amount=330, color_id=4, price_no_package=48, price_package=50)
i114 = Items(name='Кирпич гладкий 2-х угловой', size='250x120x65', facture_id=1, typee_id=1,
             weight=3.7, amount=330, color_id=5, price_no_package=49, price_package=51)

i115 = Items(name='Кирпич "финский"', size='250x100x65', amount_per_meter=52, facture_id=2, typee_id=1,
             weight=3.8, amount=330, color_id=1, price_no_package=50, price_package=52)
i116 = Items(name='Кирпич "финский"', size='250x100x65', amount_per_meter=52, facture_id=2, typee_id=1,
             weight=3.8, amount=330, color_id=2, price_no_package=54, price_package=56)
i117 = Items(name='Кирпич "финский"', size='250x100x65', amount_per_meter=52, facture_id=2, typee_id=1,
             weight=3.8, amount=330, color_id=3, price_no_package=54, price_package=56)
i118 = Items(name='Кирпич "финский"', size='250x100x65', amount_per_meter=52, facture_id=2, typee_id=1,
             weight=3.8, amount=330, color_id=4, price_no_package=54, price_package=56)
i119 = Items(name='Кирпич "финский"', size='250x100x65', amount_per_meter=52, facture_id=2, typee_id=1,
             weight=3.8, amount=330, color_id=5, price_no_package=55, price_package=57)

im11 = Photos(item_id=11, filepath='../static/uploads/items/11.png') #Кирпич гладкий 2-х угловой
im12 = Photos(item_id=12, filepath='../static/uploads/items/12.png')
im13 = Photos(item_id=13, filepath='../static/uploads/items/13.png')
im14 = Photos(item_id=14, filepath='../static/uploads/items/14.png')
im15 = Photos(item_id=15, filepath='../static/uploads/items/15.png')

im16 = Photos(item_id=16, filepath='../static/uploads/items/16.png') #Кирпич "финский"
im17 = Photos(item_id=17, filepath='../static/uploads/items/17.png')
im18 = Photos(item_id=18, filepath='../static/uploads/items/18.png')
im19 = Photos(item_id=19, filepath='../static/uploads/items/19.png')
im20 = Photos(item_id=20, filepath='../static/uploads/items/20.png')

i120 = Items(name='Кирпич гладкий тычковой', size='230x120x65', facture_id=2, typee_id=1,
             weight=4.0, amount=330, color_id=1, price_no_package=50, price_package=52)
i121 = Items(name='Кирпич гладкий тычковой', size='230x120x65', facture_id=2, typee_id=1,
             weight=4.0, amount=330, color_id=2, price_no_package=54, price_package=56)
i122 = Items(name='Кирпич гладкий тычковой', size='230x120x65', facture_id=2, typee_id=1,
             weight=4.0, amount=330, color_id=3, price_no_package=54, price_package=56)
i123 = Items(name='Кирпич гладкий тычковой', size='230x120x65', facture_id=2, typee_id=1,
             weight=4.0, amount=330, color_id=4, price_no_package=54, price_package=56)
i124 = Items(name='Кирпич гладкий тычковой', size='230x120x65', facture_id=2, typee_id=1,
             weight=4.0, amount=330, color_id=5, price_no_package=55, price_package=57)

i125 = Items(name='Кирпич "финский" тычковой', size='230x100x65', facture_id=2, typee_id=1,
             weight=3.7, amount=330, color_id=1, price_no_package=54, price_package=56)
i126 = Items(name='Кирпич "финский" тычковой', size='230x100x65', facture_id=2, typee_id=1,
             weight=3.7, amount=330, color_id=2, price_no_package=60, price_package=62)
i127 = Items(name='Кирпич "финский" тычковой', size='230x100x65', facture_id=2, typee_id=1,
             weight=3.7, amount=330, color_id=3, price_no_package=60, price_package=62)
i128 = Items(name='Кирпич "финский" тычковой', size='230x100x65', facture_id=2, typee_id=1,
             weight=3.7, amount=330, color_id=4, price_no_package=60, price_package=62)
i129 = Items(name='Кирпич "финский" тычковой', size='230x100x65', facture_id=2, typee_id=1,
             weight=3.7, amount=330, color_id=5, price_no_package=61, price_package=63)


im21 = Photos(item_id=21, filepath='../static/uploads/items/21.png') #Кирпич гладкий тычковой
im22 = Photos(item_id=22, filepath='../static/uploads/items/22.png')
im23 = Photos(item_id=23, filepath='../static/uploads/items/23.png')
im24 = Photos(item_id=24, filepath='../static/uploads/items/24.png')
im25 = Photos(item_id=25, filepath='../static/uploads/items/25.png')

im26 = Photos(item_id=26, filepath='../static/uploads/items/26.png') #Кирпич "финский" тычковой
im27 = Photos(item_id=27, filepath='../static/uploads/items/27.png')
im28 = Photos(item_id=28, filepath='../static/uploads/items/28.png')
im29 = Photos(item_id=29, filepath='../static/uploads/items/29.png')
im30 = Photos(item_id=30, filepath='../static/uploads/items/30.png')

i130 = Items(name='Кирпич "финский" угловой тычковой', size='230x100x65', facture_id=2, typee_id=1,
             weight=3.5, amount=330, color_id=1, price_no_package=56, price_package=58)
i131 = Items(name='Кирпич "финский" угловой тычковой', size='230x100x65', facture_id=2, typee_id=1,
             weight=3.5, amount=330, color_id=2, price_no_package=62, price_package=64)
i132 = Items(name='Кирпич "финский" угловой тычковой', size='230x100x65', facture_id=2, typee_id=1,
             weight=3.5, amount=330, color_id=3, price_no_package=62, price_package=64)
i133 = Items(name='Кирпич "финский" угловой тычковой', size='230x100x65', facture_id=2, typee_id=1,
             weight=3.5, amount=330, color_id=4, price_no_package=62, price_package=64)
i134 = Items(name='Кирпич "финский" угловой тычковой', size='230x100x65', facture_id=2, typee_id=1,
             weight=3.5, amount=330, color_id=5, price_no_package=63, price_package=65)

i135 = Items(name='Кирпич "финский" 2-х угловой', size='250x100x65', facture_id=2, typee_id=1,
             weight=3.4, amount=330, color_id=1, price_no_package=56, price_package=58)
i136 = Items(name='Кирпич "финский" 2-х угловой', size='250x100x65', facture_id=2, typee_id=1,
             weight=3.4, amount=330, color_id=2, price_no_package=62, price_package=64)
i137 = Items(name='Кирпич "финский" 2-х угловой', size='250x100x65', facture_id=2, typee_id=1,
             weight=3.4, amount=330, color_id=3, price_no_package=62, price_package=64)
i138 = Items(name='Кирпич "финский" 2-х угловой', size='250x100x65', facture_id=2, typee_id=1,
             weight=3.4, amount=330, color_id=4, price_no_package=62, price_package=64)
i139 = Items(name='Кирпич "финский" 2-х угловой', size='250x100x65', facture_id=2, typee_id=1,
             weight=3.4, amount=330, color_id=5, price_no_package=63, price_package=65)

im31 = Photos(item_id=31, filepath='../static/uploads/items/31.png') #Кирпич "финский" угловой тычковой
im32 = Photos(item_id=32, filepath='../static/uploads/items/32.png')
im33 = Photos(item_id=33, filepath='../static/uploads/items/33.png')
im34 = Photos(item_id=34, filepath='../static/uploads/items/34.png')
im35 = Photos(item_id=35, filepath='../static/uploads/items/35.png')

im36 = Photos(item_id=36, filepath='../static/uploads/items/36.png') #Кирпич "финский" 2-х угловой
im37 = Photos(item_id=37, filepath='../static/uploads/items/37.png')
im38 = Photos(item_id=38, filepath='../static/uploads/items/38.png') #не брать
im39 = Photos(item_id=39, filepath='../static/uploads/items/39.png')
im40 = Photos(item_id=30, filepath='../static/uploads/items/40.png')

i140 = Items(name='Кирпич "финский" 40', size='250x40x65', amount_per_meter=52, facture_id=2, typee_id=1,
             weight=3.8, amount=660, color_id=1, price_no_package=32, price_package=33)
i141 = Items(name='Кирпич "финский" 40', size='250x40x65', amount_per_meter=52, facture_id=2, typee_id=1,
             weight=3.8, amount=660, color_id=2, price_no_package=36, price_package=37)
i142 = Items(name='Кирпич "финский" 40', size='250x40x65', amount_per_meter=52, facture_id=2, typee_id=1,
             weight=3.8, amount=660, color_id=3, price_no_package=36, price_package=37)
i143 = Items(name='Кирпич "финский" 40', size='250x40x65', amount_per_meter=52, facture_id=2, typee_id=1,
             weight=3.8, amount=660, color_id=4, price_no_package=36, price_package=37)
i144 = Items(name='Кирпич "финский" 40', size='250x40x65', amount_per_meter=52, facture_id=2, typee_id=1,
             weight=3.8, amount=660, color_id=5, price_no_package=37, price_package=38)

i145 = Items(name='Кирпич "финский" 40 тычковой', size='230x40x65', amount_per_meter=52, facture_id=2, typee_id=1,
             weight=1.9, amount=660, color_id=1, price_no_package=33, price_package=34)
i146 = Items(name='Кирпич "финский" 40 тычковой', size='230x40x65', amount_per_meter=52, facture_id=2, typee_id=1,
             weight=1.9, amount=660, color_id=2, price_no_package=37, price_package=38)
i147 = Items(name='Кирпич "финский" 40 тычковой', size='230x40x65', amount_per_meter=52, facture_id=2, typee_id=1,
             weight=1.9, amount=660, color_id=3, price_no_package=37, price_package=38)
i148 = Items(name='Кирпич "финский" 40 тычковой', size='230x40x65', amount_per_meter=52, facture_id=2, typee_id=1,
             weight=1.9, amount=660, color_id=4, price_no_package=37, price_package=38)
i149 = Items(name='Кирпич "финский" 40 тычковой', size='230x40x65', amount_per_meter=52, facture_id=2, typee_id=1,
             weight=1.9, amount=660, color_id=5, price_no_package=38, price_package=39)

im41 = Photos(item_id=41, filepath='../static/uploads/items/41.png') #Кирпич "финский" 40
im42 = Photos(item_id=42, filepath='../static/uploads/items/42.png')
im43 = Photos(item_id=43, filepath='../static/uploads/items/43.png')
im44 = Photos(item_id=44, filepath='../static/uploads/items/44.png')
im45 = Photos(item_id=45, filepath='../static/uploads/items/45.png')

im46 = Photos(item_id=46, filepath='../static/uploads/items/46.png') #Кирпич "финский" 40 тычковой
im47 = Photos(item_id=47, filepath='../static/uploads/items/47.png')
im48 = Photos(item_id=48, filepath='../static/uploads/items/48.png')
im49 = Photos(item_id=49, filepath='../static/uploads/items/49.png')
im50 = Photos(item_id=50, filepath='../static/uploads/items/50.png')

i150 = Items(name='Кирпич "старый город"', size='250x110x65', amount_per_meter=52, facture_id=3, typee_id=1,
             weight=4.0, amount=330, color_id=1, price_no_package=50, price_package=52)
i151 = Items(name='Кирпич "старый город"', size='250x110x65', amount_per_meter=52, facture_id=3, typee_id=1,
             weight=4.0, amount=330, color_id=2, price_no_package=54, price_package=56)
i152 = Items(name='Кирпич "старый город"', size='250x110x65', amount_per_meter=52, facture_id=3, typee_id=1,
             weight=4.0, amount=330, color_id=3, price_no_package=54, price_package=56)
i153 = Items(name='Кирпич "старый город"', size='250x110x65', amount_per_meter=52, facture_id=3, typee_id=1,
             weight=4.0, amount=330, color_id=4, price_no_package=54, price_package=56)
i154 = Items(name='Кирпич "старый город"', size='250x110x65', amount_per_meter=52, facture_id=3, typee_id=1,
             weight=4.0, amount=330, color_id=5, price_no_package=55, price_package=57)

i155 = Items(name='Кирпич "старый город" тычковой', size='240x110x65', facture_id=3, typee_id=1,
             weight=3.8, amount=330, color_id=1, price_no_package=54, price_package=56)
i156 = Items(name='Кирпич "старый город" тычковой', size='240x110x65', facture_id=3, typee_id=1,
             weight=3.8, amount=330, color_id=2, price_no_package=60, price_package=62)
i157 = Items(name='Кирпич "старый город" тычковой', size='240x110x65', facture_id=3, typee_id=1,
             weight=3.8, amount=330, color_id=3, price_no_package=60, price_package=62)
i158 = Items(name='Кирпич "старый город" тычковой', size='240x110x65', facture_id=3, typee_id=1,
             weight=3.8, amount=330, color_id=4, price_no_package=60, price_package=62)
i159 = Items(name='Кирпич "старый город" тычковой', size='240x110x65', facture_id=3, typee_id=1,
             weight=3.8, amount=330, color_id=5, price_no_package=61, price_package=63)

im51 = Photos(item_id=51, filepath='../static/uploads/items/51.png') #Кирпич "старый город"
im52 = Photos(item_id=52, filepath='../static/uploads/items/52.png')
im53 = Photos(item_id=53, filepath='../static/uploads/items/53.png')
im54 = Photos(item_id=54, filepath='../static/uploads/items/54.png')
im55 = Photos(item_id=55, filepath='../static/uploads/items/55.png')

im56 = Photos(item_id=56, filepath='../static/uploads/items/56.png') #Кирпич "старый город" тычковой
im57 = Photos(item_id=57, filepath='../static/uploads/items/57.png')
im58 = Photos(item_id=58, filepath='../static/uploads/items/58.png')
im59 = Photos(item_id=59, filepath='../static/uploads/items/59.png')
im60 = Photos(item_id=60, filepath='../static/uploads/items/60.png')

i160 = Items(name='Кирпич "старый город" угловой тычковой', size='240x110x65', facture_id=3, typee_id=1,
             weight=3.7, amount=330, color_id=1, price_no_package=56, price_package=58)
i161 = Items(name='Кирпич "старый город" угловой тычковой', size='240x110x65', facture_id=3, typee_id=1,
             weight=3.7, amount=330, color_id=2, price_no_package=62, price_package=64)
i162 = Items(name='Кирпич "старый город" угловой тычковой', size='240x110x65', facture_id=3, typee_id=1,
             weight=3.7, amount=330, color_id=3, price_no_package=62, price_package=64)
i163 = Items(name='Кирпич "старый город" угловой тычковой', size='240x110x65', facture_id=3, typee_id=1,
             weight=3.7, amount=330, color_id=4, price_no_package=62, price_package=64)
i164 = Items(name='Кирпич "старый город" угловой тычковой', size='240x110x65', facture_id=3, typee_id=1,
             weight=3.7, amount=330, color_id=5, price_no_package=63, price_package=65)

i165 = Items(name='Кирпич "старый город" 2-х  угловой', size='230x110x65', amount_per_meter=52, facture_id=3, typee_id=1,
             weight=3.5, amount=330, color_id=1, price_no_package=56, price_package=58)
i166 = Items(name='Кирпич "старый город" 2-х  угловой', size='230x110x65', amount_per_meter=52, facture_id=3, typee_id=1,
             weight=3.5, amount=330, color_id=2, price_no_package=62, price_package=64)
i167 = Items(name='Кирпич "старый город" 2-х  угловой', size='230x110x65', amount_per_meter=52, facture_id=3, typee_id=1,
             weight=3.5, amount=330, color_id=3, price_no_package=62, price_package=64)
i168 = Items(name='Кирпич "старый город" 2-х  угловой', size='230x110x65', amount_per_meter=52, facture_id=3, typee_id=1,
             weight=3.5, amount=330, color_id=4, price_no_package=62, price_package=64)
i169 = Items(name='Кирпич "старый город" 2-х  угловой', size='230x110x65', amount_per_meter=52, facture_id=3, typee_id=1,
             weight=3.5, amount=330, color_id=5, price_no_package=63, price_package=65)

im61 = Photos(item_id=61, filepath='../static/uploads/items/61.png') #Кирпич "старый город" угловой тычковой
im62 = Photos(item_id=62, filepath='../static/uploads/items/62.png')
im63 = Photos(item_id=63, filepath='../static/uploads/items/63.png')
im64 = Photos(item_id=64, filepath='../static/uploads/items/64.png')
im65 = Photos(item_id=65, filepath='../static/uploads/items/65.png')

im66 = Photos(item_id=66, filepath='../static/uploads/items/66.png') #Кирпич "старый город" 2-х  угловой
im67 = Photos(item_id=67, filepath='../static/uploads/items/67.png')
im68 = Photos(item_id=68, filepath='../static/uploads/items/68.png')
im69 = Photos(item_id=69, filepath='../static/uploads/items/69.png')
im70 = Photos(item_id=70, filepath='../static/uploads/items/70.png')

i170 = Items(name='Кирпич "старый город" 50', size='250x50x65', amount_per_meter=52, facture_id=3, typee_id=1,
             weight=2.0, amount=660, color_id=1, price_no_package=32, price_package=33)
i171 = Items(name='Кирпич "старый город" 50', size='250x50x65', amount_per_meter=52, facture_id=3, typee_id=1,
             weight=2.0, amount=660, color_id=2, price_no_package=36, price_package=37)
i172 = Items(name='Кирпич "старый город" 50', size='250x50x65', amount_per_meter=52, facture_id=3, typee_id=1,
             weight=2.0, amount=660, color_id=3, price_no_package=36, price_package=37)
i173 = Items(name='Кирпич "старый город" 50', size='250x50x65', amount_per_meter=52, facture_id=3, typee_id=1,
             weight=2.0, amount=660, color_id=4, price_no_package=36, price_package=37)
i174 = Items(name='Кирпич "старый город" 50', size='250x50x65', amount_per_meter=52, facture_id=3, typee_id=1,
             weight=2.0, amount=660, color_id=5, price_no_package=37, price_package=38)

i175 = Items(name='Плитка "старый город"', size='250x20x65', amount_per_meter=52, facture_id=3, typee_id=2,
             weight=0.9, amount=960, color_id=1, price_no_package=25, price_package=26)
i176 = Items(name='Плитка "старый город"', size='250x20x65', amount_per_meter=52, facture_id=3, typee_id=2,
             weight=0.9, amount=960, color_id=2, price_no_package=28, price_package=29)
i177 = Items(name='Плитка "старый город"', size='250x20x65', amount_per_meter=52, facture_id=3, typee_id=2,
             weight=0.9, amount=960, color_id=3, price_no_package=28, price_package=29)
i178 = Items(name='Плитка "старый город"', size='250x20x65', amount_per_meter=52, facture_id=3, typee_id=2,
             weight=0.9, amount=960, color_id=4, price_no_package=28, price_package=29)
i179 = Items(name='Плитка "старый город"', size='250x20x65', amount_per_meter=52, facture_id=3, typee_id=2,
             weight=0.9, amount=960, color_id=5, price_no_package=29, price_package=30)

im71 = Photos(item_id=71, filepath='../static/uploads/items/71.png') #Кирпич "старый город" 50
im72 = Photos(item_id=72, filepath='../static/uploads/items/72.png')
im73 = Photos(item_id=73, filepath='../static/uploads/items/73.png')
im74 = Photos(item_id=74, filepath='../static/uploads/items/74.png')
im75 = Photos(item_id=75, filepath='../static/uploads/items/75.png')

im76 = Photos(item_id=76, filepath='../static/uploads/items/76.png') #Плитка "старый город"
im77 = Photos(item_id=77, filepath='../static/uploads/items/77.png')
im78 = Photos(item_id=78, filepath='../static/uploads/items/78.png')
im79 = Photos(item_id=79, filepath='../static/uploads/items/79.png')
im80 = Photos(item_id=80, filepath='../static/uploads/items/80.png')

i180 = Items(name='Кирпич 80 "скала"', size='250x80x65', amount_per_meter=52, facture_id=4, typee_id=1,
             weight=3.8, amount=330, color_id=1, price_no_package=52, price_package=54)
i181 = Items(name='Кирпич 80 "скала"', size='250x80x65', amount_per_meter=52, facture_id=4, typee_id=1,
             weight=3.8, amount=330, color_id=2, price_no_package=56, price_package=58)
i182 = Items(name='Кирпич 80 "скала"', size='250x80x65', amount_per_meter=52, facture_id=4, typee_id=1,
             weight=3.8, amount=330, color_id=3, price_no_package=56, price_package=58)
i183 = Items(name='Кирпич 80 "скала"', size='250x80x65', amount_per_meter=52, facture_id=4, typee_id=1,
             weight=3.8, amount=330, color_id=4, price_no_package=56, price_package=58)
i184 = Items(name='Кирпич 80 "скала"', size='250x80x65', amount_per_meter=52, facture_id=4, typee_id=1,
             weight=3.8, amount=330, color_id=5, price_no_package=57, price_package=59)

i185 = Items(name='Кирпич 80 "скала" тычковой', size='230x80x65', amount_per_meter=52, facture_id=4, typee_id=1,
             weight=3.6, amount=330, color_id=1, price_no_package=55, price_package=57)
i186 = Items(name='Кирпич 80 "скала" тычковой', size='230x80x65', amount_per_meter=52, facture_id=4, typee_id=1,
             weight=3.6, amount=330, color_id=2, price_no_package=56, price_package=58)
i187 = Items(name='Кирпич 80 "скала" тычковой', size='230x80x65', amount_per_meter=52, facture_id=4, typee_id=1,
             weight=3.6, amount=330, color_id=3, price_no_package=56, price_package=58)
i188 = Items(name='Кирпич 80 "скала" тычковой', size='230x80x65', amount_per_meter=52, facture_id=4, typee_id=1,
             weight=3.6, amount=330, color_id=4, price_no_package=56, price_package=58)
i189 = Items(name='Кирпич 80 "скала" тычковой', size='230x80x65', amount_per_meter=52, facture_id=4, typee_id=1,
             weight=3.6, amount=330, color_id=5, price_no_package=57, price_package=59)

im81 = Photos(item_id=81, filepath='../static/uploads/items/81.png') #Кирпич 80 "скала"
im82 = Photos(item_id=82, filepath='../static/uploads/items/82.png')
im83 = Photos(item_id=83, filepath='../static/uploads/items/83.png')
im84 = Photos(item_id=84, filepath='../static/uploads/items/84.png')
im85 = Photos(item_id=85, filepath='../static/uploads/items/85.png')

im86 = Photos(item_id=86, filepath='../static/uploads/items/86.png') #Кирпич 80 "скала" тычковой
im87 = Photos(item_id=87, filepath='../static/uploads/items/87.png')
im88 = Photos(item_id=88, filepath='../static/uploads/items/88.png')
im89 = Photos(item_id=89, filepath='../static/uploads/items/89.png')
im90 = Photos(item_id=90, filepath='../static/uploads/items/90.png')

i190 = Items(name='Кирпич 50 "скала"', size='250x50x65', amount_per_meter=52, facture_id=4, typee_id=1,
             weight=2.0, amount=660, color_id=1, price_no_package=32, price_package=33)
i191 = Items(name='Кирпич 50 "скала"', size='250x50x65', amount_per_meter=52, facture_id=4, typee_id=1,
             weight=2.0, amount=660, color_id=2, price_no_package=36, price_package=37)
i192 = Items(name='Кирпич 50 "скала"', size='250x50x65', amount_per_meter=52, facture_id=4, typee_id=1,
             weight=2.0, amount=660, color_id=3, price_no_package=36, price_package=37)
i193 = Items(name='Кирпич 50 "скала"', size='250x50x65', amount_per_meter=52, facture_id=4, typee_id=1,
             weight=2.0, amount=660, color_id=4, price_no_package=36, price_package=37)
i194 = Items(name='Кирпич 50 "скала"', size='250x50x65', amount_per_meter=52, facture_id=4, typee_id=1,
             weight=2.0, amount=660, color_id=5, price_no_package=37, price_package=38)

i195 = Items(name='Кирпич 50 "скала" тычковой', size='230x50x65', amount_per_meter=52, facture_id=4, typee_id=1,
             weight=1.9, amount=660, color_id=1, price_no_package=34, price_package=35)
i196 = Items(name='Кирпич 50 "скала" тычковой', size='230x50x65', amount_per_meter=52, facture_id=4, typee_id=1,
             weight=1.9, amount=660, color_id=2, price_no_package=38, price_package=39)
i197 = Items(name='Кирпич 50 "скала" тычковой', size='230x50x65', amount_per_meter=52, facture_id=4, typee_id=1,
             weight=1.9, amount=660, color_id=3, price_no_package=38, price_package=39)
i198 = Items(name='Кирпич 50 "скала" тычковой', size='230x50x65', amount_per_meter=52, facture_id=4, typee_id=1,
             weight=1.9, amount=660, color_id=4, price_no_package=38, price_package=39)
i199 = Items(name='Кирпич 50 "скала" тычковой', size='230x50x65', amount_per_meter=52, facture_id=4, typee_id=1,
             weight=1.9, amount=660, color_id=5, price_no_package=39, price_package=40)

im91 = Photos(item_id=91, filepath='../static/uploads/items/91.png') #Кирпич 50 "скала"
im92 = Photos(item_id=92, filepath='../static/uploads/items/92.png')
im93 = Photos(item_id=93, filepath='../static/uploads/items/93.png')
im94 = Photos(item_id=94, filepath='../static/uploads/items/94.png')
im95 = Photos(item_id=95, filepath='../static/uploads/items/95.png')

im96 = Photos(item_id=96, filepath='../static/uploads/items/96.png') #Кирпич 50 "скала" тычковой
im97 = Photos(item_id=97, filepath='../static/uploads/items/97.png')
im98 = Photos(item_id=98, filepath='../static/uploads/items/98.png')
im99 = Photos(item_id=99, filepath='../static/uploads/items/99.png')
im100 = Photos(item_id=100, filepath='../static/uploads/items/100.png')

i200 = Items(name='Плитка "скала"', size='250x20x65', amount_per_meter=52, facture_id=4, typee_id=2,
             weight=0.9, amount=900, color_id=1, price_no_package=22, price_package=23)
i201 = Items(name='Плитка "скала"', size='250x20x65', amount_per_meter=52, facture_id=4, typee_id=2,
             weight=0.9, amount=900, color_id=2, price_no_package=26, price_package=27)
i202 = Items(name='Плитка "скала"', size='250x20x65', amount_per_meter=52, facture_id=4, typee_id=2,
             weight=0.9, amount=900, color_id=3, price_no_package=26, price_package=27)
i203 = Items(name='Плитка "скала"', size='250x20x65', amount_per_meter=52, facture_id=4, typee_id=2,
             weight=0.9, amount=900, color_id=4, price_no_package=26, price_package=27)
i204 = Items(name='Плитка "скала"', size='250x20x65', amount_per_meter=52, facture_id=4, typee_id=2,
             weight=0.9, amount=900, color_id=5, price_no_package=27, price_package=28)

i205 = Items(name='Кирпич 90 мраморный', size='250x90x65', amount_per_meter=52, facture_id=5, typee_id=1,
             weight=3.8, amount=330, color_id=1, price_no_package=50, price_package=52)
i206 = Items(name='Кирпич 90 мраморный', size='250x90x65', amount_per_meter=52, facture_id=5, typee_id=1,
             weight=3.8, amount=330, color_id=2, price_no_package=54, price_package=56)
i207 = Items(name='Кирпич 90 мраморный', size='250x90x65', amount_per_meter=52, facture_id=5, typee_id=1,
             weight=3.8, amount=330, color_id=3, price_no_package=54, price_package=56)
i208 = Items(name='Кирпич 90 мраморный', size='250x90x65', amount_per_meter=52, facture_id=5, typee_id=1,
             weight=3.8, amount=330, color_id=4, price_no_package=54, price_package=56)
i209 = Items(name='Кирпич 90 мраморный', size='250x90x65', amount_per_meter=52, facture_id=5, typee_id=1,
             weight=3.8, amount=330, color_id=5, price_no_package=55, price_package=57)

im101 = Photos(item_id=101, filepath='../static/uploads/items/101.png') #Плитка "скала"
im102 = Photos(item_id=102, filepath='../static/uploads/items/102.png')
im103 = Photos(item_id=103, filepath='../static/uploads/items/103.png')
im104 = Photos(item_id=104, filepath='../static/uploads/items/104.png')
im105 = Photos(item_id=105, filepath='../static/uploads/items/105.png')

im106 = Photos(item_id=106, filepath='../static/uploads/items/106.png') #Кирпич 90 мраморный
im107 = Photos(item_id=107, filepath='../static/uploads/items/107.png')
im108 = Photos(item_id=108, filepath='../static/uploads/items/108.png')
im109 = Photos(item_id=109, filepath='../static/uploads/items/109.png')
im110 = Photos(item_id=110, filepath='../static/uploads/items/110.png')

i210 = Items(name='Кирпич 90 мраморный тычковой', size='230x90x65', facture_id=5, typee_id=1,
             weight=3.7, amount=330, color_id=1, price_no_package=52, price_package=54)
i211 = Items(name='Кирпич 90 мраморный тычковой', size='230x90x65', facture_id=5, typee_id=1,
             weight=3.7, amount=330, color_id=2, price_no_package=56, price_package=58)
i212 = Items(name='Кирпич 90 мраморный тычковой', size='230x90x65', facture_id=5, typee_id=1,
             weight=3.7, amount=330, color_id=3, price_no_package=56, price_package=58)
i213 = Items(name='Кирпич 90 мраморный тычковой', size='230x90x65', facture_id=5, typee_id=1,
             weight=3.7, amount=330, color_id=4, price_no_package=56, price_package=58)
i214 = Items(name='Кирпич 90 мраморный тычковой', size='230x90x65', facture_id=5, typee_id=1,
             weight=3.7, amount=330, color_id=5, price_no_package=57, price_package=59)

i215 = Items(name='Кирпич 60 мраморный', size='250x60x65', facture_id=5, typee_id=1,
             weight=3.6, amount=660, color_id=1, price_no_package=26, price_package=27)
i216 = Items(name='Кирпич 60 мраморный', size='250x60x65', facture_id=5, typee_id=1,
             weight=3.6, amount=660, color_id=2, price_no_package=30, price_package=31)
i217 = Items(name='Кирпич 60 мраморный', size='250x60x65', facture_id=5, typee_id=1,
             weight=3.6, amount=660, color_id=3, price_no_package=30, price_package=31)
i218 = Items(name='Кирпич 60 мраморный', size='250x60x65', facture_id=5, typee_id=1,
             weight=3.6, amount=660, color_id=4, price_no_package=30, price_package=31)
i219 = Items(name='Кирпич 60 мраморный', size='250x60x65', facture_id=5, typee_id=1,
             weight=3.6, amount=660, color_id=5, price_no_package=31, price_package=32)

im111 = Photos(item_id=111, filepath='../static/uploads/items/111.png') #Кирпич 90 мраморный тычковой
im112 = Photos(item_id=112, filepath='../static/uploads/items/112.png')
im113 = Photos(item_id=113, filepath='../static/uploads/items/113.png')
im114 = Photos(item_id=114, filepath='../static/uploads/items/114.png')
im115 = Photos(item_id=115, filepath='../static/uploads/items/115.png')

im116 = Photos(item_id=116, filepath='../static/uploads/items/116.png') #Кирпич 60 мраморный
im117 = Photos(item_id=117, filepath='../static/uploads/items/117.png')
im118 = Photos(item_id=118, filepath='../static/uploads/items/118.png')
im119 = Photos(item_id=119, filepath='../static/uploads/items/119.png')
im120 = Photos(item_id=120, filepath='../static/uploads/items/120.png')

i220 = Items(name='Кирпич 60 мраморный тычковой', size='230x60x65', amount_per_meter=52, facture_id=5, typee_id=1,
             weight=2.2, amount=660, color_id=1, price_no_package=28, price_package=29)
i221 = Items(name='Кирпич 60 мраморный тычковой', size='230x60x65', amount_per_meter=52, facture_id=5, typee_id=1,
             weight=2.2, amount=660, color_id=2, price_no_package=32, price_package=33)
i222 = Items(name='Кирпич 60 мраморный тычковой', size='230x60x65', amount_per_meter=52, facture_id=5, typee_id=1,
             weight=2.2, amount=660, color_id=3, price_no_package=32, price_package=33)
i223 = Items(name='Кирпич 60 мраморный тычковой', size='230x60x65', amount_per_meter=52, facture_id=5, typee_id=1,
             weight=2.2, amount=660, color_id=4, price_no_package=32, price_package=33)
i224 = Items(name='Кирпич 60 мраморный тычковой', size='230x60x65', amount_per_meter=52, facture_id=5, typee_id=1,
             weight=2.2, amount=660, color_id=5, price_no_package=33, price_package=34)

i225 = Items(name='Плитка мраморная', size='250x30x65', amount_per_meter=52, facture_id=5, typee_id=2,
             weight=1.1, amount=960, color_id=1, price_no_package=18, price_package=19)
i226 = Items(name='Плитка мраморная', size='250x30x65', amount_per_meter=52, facture_id=5, typee_id=2,
             weight=1.1, amount=960, color_id=2, price_no_package=20, price_package=21)
i227 = Items(name='Плитка мраморная', size='250x30x65', amount_per_meter=52, facture_id=5, typee_id=2,
             weight=1.1, amount=960, color_id=3, price_no_package=20, price_package=21)
i228 = Items(name='Плитка мраморная', size='250x30x65', amount_per_meter=52, facture_id=5, typee_id=2,
             weight=1.1, amount=960, color_id=4, price_no_package=20, price_package=21)
i229 = Items(name='Плитка мраморная', size='250x30x65', amount_per_meter=52, facture_id=5, typee_id=2,
             weight=1.1, amount=960, color_id=5, price_no_package=21, price_package=22)

im121 = Photos(item_id=121, filepath='../static/uploads/items/121.png') #Кирпич 60 мраморный тычковой
im122 = Photos(item_id=122, filepath='../static/uploads/items/122.png')
im123 = Photos(item_id=123, filepath='../static/uploads/items/123.png')
im124 = Photos(item_id=124, filepath='../static/uploads/items/124.png')
im125 = Photos(item_id=125, filepath='../static/uploads/items/125.png')

im126 = Photos(item_id=126, filepath='../static/uploads/items/126.png') #Плитка мраморная
im127 = Photos(item_id=127, filepath='../static/uploads/items/127.png')
im128 = Photos(item_id=128, filepath='../static/uploads/items/128.png')
im129 = Photos(item_id=129, filepath='../static/uploads/items/129.png')
im130 = Photos(item_id=130, filepath='../static/uploads/items/130.png')

i230 = Items(name='Кирпич мраморный с фаской', size='250x100x65', amount_per_meter=52, facture_id=6, typee_id=1,
             weight=3.9, amount=330, color_id=1, price_no_package=50, price_package=52)
i231 = Items(name='Кирпич мраморный с фаской', size='250x100x65', amount_per_meter=52, facture_id=6, typee_id=1,
             weight=3.9, amount=330, color_id=2, price_no_package=54, price_package=56)
i232 = Items(name='Кирпич мраморный с фаской', size='250x100x65', amount_per_meter=52, facture_id=6, typee_id=1,
             weight=3.9, amount=330, color_id=3, price_no_package=54, price_package=56)
i233 = Items(name='Кирпич мраморный с фаской', size='250x100x65', amount_per_meter=52, facture_id=6, typee_id=1,
             weight=3.9, amount=330, color_id=4, price_no_package=54, price_package=56)
i234 = Items(name='Кирпич мраморный с фаской', size='250x100x65', amount_per_meter=52, facture_id=6, typee_id=1,
             weight=3.9, amount=330, color_id=5, price_no_package=55, price_package=57)

i235 = Items(name='Кирпич  мраморный гладкий тычковой с фаской', size='230x120x65', facture_id=6, typee_id=1,
             weight=4.0, amount=330, color_id=1, price_no_package=50, price_package=52)
i236 = Items(name='Кирпич  мраморный гладкий тычковой с фаской', size='230x120x65', facture_id=6, typee_id=1,
             weight=4.0, amount=330, color_id=2, price_no_package=54, price_package=56)
i237 = Items(name='Кирпич  мраморный гладкий тычковой с фаской', size='230x120x65', facture_id=6, typee_id=1,
             weight=4.0, amount=330, color_id=3, price_no_package=54, price_package=56)
i238 = Items(name='Кирпич  мраморный гладкий тычковой с фаской', size='230x120x65', facture_id=6, typee_id=1,
             weight=4.0, amount=330, color_id=4, price_no_package=54, price_package=56)
i239 = Items(name='Кирпич  мраморный гладкий тычковой с фаской', size='230x120x65', facture_id=6, typee_id=1,
             weight=4.0, amount=330, color_id=5, price_no_package=55, price_package=57)

im131 = Photos(item_id=131, filepath='../static/uploads/items/131.png') #Кирпич мраморный с фаской
im132 = Photos(item_id=132, filepath='../static/uploads/items/132.png')
im133 = Photos(item_id=133, filepath='../static/uploads/items/133.png')
im134 = Photos(item_id=134, filepath='../static/uploads/items/134.png')
im135 = Photos(item_id=135, filepath='../static/uploads/items/135.png')

im136 = Photos(item_id=136, filepath='../static/uploads/items/136.png') #Кирпич  мраморный гладкий тычковой с фаской
im137 = Photos(item_id=137, filepath='../static/uploads/items/137.png')
im138 = Photos(item_id=138, filepath='../static/uploads/items/138.png')
im139 = Photos(item_id=139, filepath='../static/uploads/items/139.png')
im140 = Photos(item_id=140, filepath='../static/uploads/items/140.png')

i240 = Items(name='Кирпич мраморный тычковой фрезерованный', size='230x100x65', facture_id=6, typee_id=1,
             weight=3.8, amount=330, color_id=1, price_no_package=54, price_package=56)
i241 = Items(name='Кирпич мраморный тычковой фрезерованный', size='230x100x65', facture_id=6, typee_id=1,
             weight=3.8, amount=330, color_id=2, price_no_package=60, price_package=62)
i242 = Items(name='Кирпич мраморный тычковой фрезерованный', size='230x100x65', facture_id=6, typee_id=1,
             weight=3.8, amount=330, color_id=3, price_no_package=60, price_package=62)
i243 = Items(name='Кирпич мраморный тычковой фрезерованный', size='230x100x65', facture_id=6, typee_id=1,
             weight=3.8, amount=330, color_id=4, price_no_package=60, price_package=62)
i244 = Items(name='Кирпич мраморный тычковой фрезерованный', size='230x100x65', facture_id=6, typee_id=1,
             weight=3.8, amount=330, color_id=5, price_no_package=61, price_package=63)

i245 = Items(name='Кирпич мраморный угловой с фаской', size='230x100x65', facture_id=6, typee_id=1,
             weight=3.7, amount=330, color_id=1, price_no_package=56, price_package=58)
i246 = Items(name='Кирпич мраморный угловой с фаской', size='230x100x65', facture_id=6, typee_id=1,
             weight=3.7, amount=330, color_id=2, price_no_package=62, price_package=64)
i247 = Items(name='Кирпич мраморный угловой с фаской', size='230x100x65', facture_id=6, typee_id=1,
             weight=3.7, amount=330, color_id=3, price_no_package=62, price_package=64)
i248 = Items(name='Кирпич мраморный угловой с фаской', size='230x100x65', facture_id=6, typee_id=1,
             weight=3.7, amount=330, color_id=4, price_no_package=62, price_package=64)
i249 = Items(name='Кирпич мраморный угловой с фаской', size='230x100x65', facture_id=6, typee_id=1,
             weight=3.7, amount=330, color_id=5, price_no_package=63, price_package=65)

im141 = Photos(item_id=141, filepath='../static/uploads/items/141.png') #Кирпич мраморный тычковой фрезерованный
im142 = Photos(item_id=142, filepath='../static/uploads/items/142.png')
im143 = Photos(item_id=143, filepath='../static/uploads/items/143.png')
im144 = Photos(item_id=144, filepath='../static/uploads/items/144.png')
im145 = Photos(item_id=145, filepath='../static/uploads/items/145.png')

im146 = Photos(item_id=146, filepath='../static/uploads/items/146.png') #Кирпич мраморный угловой с фаской
im147 = Photos(item_id=147, filepath='../static/uploads/items/147.png')
im148 = Photos(item_id=148, filepath='../static/uploads/items/148.png')
im149 = Photos(item_id=149, filepath='../static/uploads/items/149.png')
im150 = Photos(item_id=150, filepath='../static/uploads/items/150.png')

i250 = Items(name='Плитка мраморная с фаской', size='250x18x65', amount_per_meter=52, facture_id=6, typee_id=2,
             weight=0.7, amount=1200, color_id=1, price_no_package=20, price_package=21)
i251 = Items(name='Плитка мраморная с фаской', size='250x18x65', amount_per_meter=52, facture_id=6, typee_id=2,
             weight=0.7, amount=1200, color_id=2, price_no_package=22, price_package=23)
i252 = Items(name='Плитка мраморная с фаской', size='250x18x65', amount_per_meter=52, facture_id=6, typee_id=2,
             weight=0.7, amount=1200, color_id=3, price_no_package=22, price_package=23)
i253 = Items(name='Плитка мраморная с фаской', size='250x18x65', amount_per_meter=52, facture_id=6, typee_id=2,
             weight=0.7, amount=1200, color_id=4, price_no_package=22, price_package=23)
i254 = Items(name='Плитка мраморная с фаской', size='250x18x65', amount_per_meter=52, facture_id=6, typee_id=2,
             weight=0.7, amount=1200, color_id=5, price_no_package=22, price_package=23)

i255 = Items(name='Плитка мраморная тычковая с фаской', size='230x18x65', facture_id=6, typee_id=2,
             weight=0.6, amount=1200, color_id=1, price_no_package=21, price_package=22)
i256 = Items(name='Плитка мраморная тычковая с фаской', size='230x18x65', facture_id=6, typee_id=2,
             weight=0.6, amount=1200, color_id=2, price_no_package=23, price_package=24)
i257 = Items(name='Плитка мраморная тычковая с фаской', size='230x18x65', facture_id=6, typee_id=2,
             weight=0.6, amount=1200, color_id=3, price_no_package=23, price_package=24)
i258 = Items(name='Плитка мраморная тычковая с фаской', size='230x18x65', facture_id=6, typee_id=2,
             weight=0.6, amount=1200, color_id=4, price_no_package=23, price_package=24)
i259 = Items(name='Плитка мраморная тычковая с фаской', size='230x18x65', facture_id=6, typee_id=2,
             weight=0.6, amount=1200, color_id=5, price_no_package=23, price_package=24)

im151 = Photos(item_id=151, filepath='../static/uploads/items/151.png') #Плитка мраморная с фаской
im152 = Photos(item_id=152, filepath='../static/uploads/items/152.png')
im153 = Photos(item_id=153, filepath='../static/uploads/items/153.png')
im154 = Photos(item_id=154, filepath='../static/uploads/items/154.png')
im155 = Photos(item_id=155, filepath='../static/uploads/items/155.png')

im156 = Photos(item_id=156, filepath='../static/uploads/items/156.png') #Плитка мраморная тычковая с фаской
im157 = Photos(item_id=157, filepath='../static/uploads/items/157.png')
im158 = Photos(item_id=158, filepath='../static/uploads/items/158.png')
im159 = Photos(item_id=159, filepath='../static/uploads/items/159.png')
im160 = Photos(item_id=160, filepath='../static/uploads/items/160.png')

i260 = Items(name='Плитка мраморная с фаской mini', size='120x18x65', facture_id=6, typee_id=2,
             weight=0.4, amount=1200, color_id=1, price_no_package=12, price_package=23)
i261 = Items(name='Плитка мраморная с фаской mini', size='120x18x65', facture_id=6, typee_id=2,
             weight=0.4, amount=1200, color_id=2, price_no_package=12, price_package=23)
i262 = Items(name='Плитка мраморная с фаской mini', size='120x18x65', facture_id=6, typee_id=2,
             weight=0.4, amount=1200, color_id=3, price_no_package=12, price_package=23)
i263 = Items(name='Плитка мраморная с фаской mini', size='120x18x65', facture_id=6, typee_id=2,
             weight=0.4, amount=1200, color_id=4, price_no_package=12, price_package=23)
i264 = Items(name='Плитка мраморная с фаской mini', size='120x18x65', facture_id=6, typee_id=2,
             weight=0.4, amount=1200, color_id=5, price_no_package=12, price_package=23)

i265 = Items(name='Кирпич цокольный', size='250x35x120', amount_per_meter=27, facture_id=7, typee_id=1,
             weight=3.0, amount=440, color_id=1, price_no_package=60, price_package=62)
i266 = Items(name='Кирпич цокольный', size='250x35x120', amount_per_meter=27, facture_id=7, typee_id=1,
             weight=3.0, amount=440, color_id=2, price_no_package=64, price_package=66)
i267 = Items(name='Кирпич цокольный', size='250x35x120', amount_per_meter=27, facture_id=7, typee_id=1,
             weight=3.0, amount=440, color_id=3, price_no_package=64, price_package=66)
i268 = Items(name='Кирпич цокольный', size='250x35x120', amount_per_meter=27, facture_id=7, typee_id=1,
             weight=3.0, amount=440, color_id=4, price_no_package=64, price_package=66)
i269 = Items(name='Кирпич цокольный', size='250x35x120', amount_per_meter=27, facture_id=7, typee_id=1,
             weight=3.0, amount=440, color_id=5, price_no_package=64, price_package=66)

im161 = Photos(item_id=161, filepath='../static/uploads/items/161.png') #Плитка мраморная с фаской mini
im162 = Photos(item_id=162, filepath='../static/uploads/items/162.png')
im163 = Photos(item_id=163, filepath='../static/uploads/items/163.png')
im164 = Photos(item_id=164, filepath='../static/uploads/items/164.png')
im165 = Photos(item_id=165, filepath='../static/uploads/items/165.png')

im166 = Photos(item_id=166, filepath='../static/uploads/items/166.png') #Кирпич цокольный
im167 = Photos(item_id=167, filepath='../static/uploads/items/167.png')
im168 = Photos(item_id=168, filepath='../static/uploads/items/168.png')
im169 = Photos(item_id=169, filepath='../static/uploads/items/169.png')
im170 = Photos(item_id=170, filepath='../static/uploads/items/170.png')

i270 = Items(name='Плитка цокольная', size='250x20x120', amount_per_meter=27, facture_id=7, typee_id=2,
             weight=2.1, amount=440, color_id=1, price_no_package=40, price_package=42)
i271 = Items(name='Плитка цокольная', size='250x20x120', amount_per_meter=27, facture_id=7, typee_id=2,
             weight=2.1, amount=440, color_id=2, price_no_package=48, price_package=50)
i272 = Items(name='Плитка цокольная', size='250x20x120', amount_per_meter=27, facture_id=7, typee_id=2,
             weight=2.1, amount=440, color_id=3, price_no_package=48, price_package=50)
i273 = Items(name='Плитка цокольная', size='250x20x120', amount_per_meter=27, facture_id=7, typee_id=2,
             weight=2.1, amount=440, color_id=4, price_no_package=48, price_package=50)
i274 = Items(name='Плитка цокольная', size='250x20x120', amount_per_meter=27, facture_id=7, typee_id=2,
             weight=2.1, amount=440, color_id=5, price_no_package=48, price_package=50)

i275 = Items(name='Плитка тротуарная', size='250x32x120', amount_per_meter=34, facture_id=8, typee_id=2,
             weight=3.2, amount=420, color_id=1, price_no_package=38, price_package=39.5)
i276 = Items(name='Плитка тротуарная', size='250x32x120', amount_per_meter=34, facture_id=8, typee_id=2,
             weight=3.2, amount=420, color_id=2, price_no_package=41, price_package=42.5)
i277 = Items(name='Плитка тротуарная', size='250x32x120', amount_per_meter=34, facture_id=8, typee_id=2,
             weight=3.2, amount=420, color_id=3, price_no_package=41, price_package=42.5)
i278 = Items(name='Плитка тротуарная', size='250x32x120', amount_per_meter=34, facture_id=8, typee_id=2,
             weight=3.2, amount=420, color_id=4, price_no_package=41, price_package=42.5)
i279 = Items(name='Плитка тротуарная', size='250x32x120', amount_per_meter=34, facture_id=8, typee_id=2,
             weight=3.2, amount=420, color_id=5, price_no_package=42, price_package=43.5)

im171 = Photos(item_id=171, filepath='../static/uploads/items/171.png') #Плитка цокольная
im172 = Photos(item_id=172, filepath='../static/uploads/items/172.png')
im173 = Photos(item_id=173, filepath='../static/uploads/items/173.png')
im174 = Photos(item_id=174, filepath='../static/uploads/items/174.png')
im175 = Photos(item_id=175, filepath='../static/uploads/items/175.png')

im176 = Photos(item_id=176, filepath='../static/uploads/items/176.png') #Плитка тротуарная гиперпрессованная
im177 = Photos(item_id=177, filepath='../static/uploads/items/177.png')
im178 = Photos(item_id=178, filepath='../static/uploads/items/178.png')
im179 = Photos(item_id=179, filepath='../static/uploads/items/179.png')
im180 = Photos(item_id=180, filepath='../static/uploads/items/180.png')

i280 = Items(name='Плитка тротуарная', size='250x50x120', amount_per_meter=34, facture_id=8, typee_id=2,
             weight=3.2, amount=420, color_id=1, price_no_package=41, price_package=42.5)
i281 = Items(name='Плитка тротуарная', size='250x50x120', amount_per_meter=34, facture_id=8, typee_id=2,
             weight=3.2, amount=420, color_id=2, price_no_package=45, price_package=46.5)
i282 = Items(name='Плитка тротуарная', size='250x50x120', amount_per_meter=34, facture_id=8, typee_id=2,
             weight=3.2, amount=420, color_id=3, price_no_package=45, price_package=46.5)
i283 = Items(name='Плитка тротуарная', size='250x50x120', amount_per_meter=34, facture_id=8, typee_id=2,
             weight=3.2, amount=420, color_id=4, price_no_package=45, price_package=46.5)
i284 = Items(name='Плитка тротуарная', size='250x50x120', amount_per_meter=34, facture_id=8, typee_id=2,
             weight=3.2, amount=420, color_id=5, price_no_package=46, price_package=47.5)

im181 = Photos(item_id=181, filepath='../static/uploads/items/181.png') #Плитка тротуарная гиперпрессованная
im182 = Photos(item_id=182, filepath='../static/uploads/items/182.png')
im183 = Photos(item_id=183, filepath='../static/uploads/items/183.png')
im184 = Photos(item_id=184, filepath='../static/uploads/items/184.png')
im185 = Photos(item_id=185, filepath='../static/uploads/items/185.png')

for i in range(100, 285):
    session.add(eval(f'i{i}'))

for i in range(1, 186):
    session.add(eval(f'im{i}'))


session.commit()