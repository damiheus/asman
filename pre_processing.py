import rasterio
import numpy as np
import matplotlib.pyplot as plt

pre_fire_path = '/home/atalayb/Documents/nasa/spaceapps/islenmis_haritalar/S1A__IW___A_20210723T155034_VH_gamma0-rtc_db.tif'
post_fire_path = '/home/atalayb/Documents/nasa/spaceapps/islenmis_haritalar/S1A__IW___A_20210816T155035_VH_gamma0-rtc_db.tif'


with rasterio.open(pre_fire_path) as src_pre:
    pre_fire_img = src_pre.read(1) 
    profile = src_pre.profile 

with rasterio.open(post_fire_path) as src_post:
    post_fire_img = src_post.read(1)


pre_fire_img[pre_fire_img == 0] = np.nan
post_fire_img[post_fire_img == 0] = np.nan


shape_pre = pre_fire_img.shape
shape_post = post_fire_img.shape


target_rows = min(shape_pre[0], shape_post[0])
target_cols = min(shape_pre[1], shape_post[1])


pre_fire_clipped = pre_fire_img[:target_rows, :target_cols]
post_fire_clipped = post_fire_img[:target_rows, :target_cols]

print("Görüntüler aynı boyuta getirildi.")
print("Yeni Boyutlar:", pre_fire_clipped.shape)


print("Yangın öncesi ve sonrası görüntüleri başarıyla okundu.")
print("Görüntü Boyutları:", pre_fire_img.shape)


post_fire_db = post_fire_img
pre_fire_db= pre_fire_img

log_ratio_change = post_fire_db - pre_fire_db

print("Log Ratio değişim haritası oluşturuldu.")

plt.figure(figsize=(12, 10))


im = plt.imshow(log_ratio_change, cmap='RdYlGn_r', vmin=-10, vmax=5)

plt.title('SAR Log Ratio Değişim Haritası (Yangın Etkisi)', fontsize=16)
plt.xlabel('Piksel (Boylam)')
plt.ylabel('Piksel (Enlem)')

cbar = plt.colorbar(im, fraction=0.046, pad=0.04)
cbar.set_label('Geri Saçılım Değişimi (dB)', fontsize=12)

plt.savefig('yangin_etki_haritasi.png', dpi=300, bbox_inches='tight')

plt.show()

profile.update(dtype=rasterio.float32, count=1)

with rasterio.open('yangin_etki_haritasi.tif', 'w', **profile) as dst:
    dst.write(log_ratio_change.astype(rasterio.float32), 1)

