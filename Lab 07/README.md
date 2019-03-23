# Lab 07: Histogram Equalization

## Task
### Task 1
Write a program that shows the histogram for a given image. For displaying the histogram, you may use Matplotlib.

|Image|Histogram|
|--|--|
|![](https://lh3.googleusercontent.com/f_tK0_YjRXLYnmh2NVsyZwlZnK9QYMwGQZ91uiahjcl2MXsI1rE8yqxl9ZA9iXP03sx1PkRHywMuD2WrSqqRokG2I2LP9QuL340SK2PifeJN35Iyz8y9OH64kkuPEcRf5J2Hb9cT)|![](https://lh4.googleusercontent.com/tIMesv8_3sfmmLOKHC6SrJMzdjmf3LgUHGqY1Qwj5-_qf65wNDS2VlJeZNhl8_xoWM1ezAoGO27WqBnsiNgyVE8xtUKyMtQNhIsI0ubFdsMOaSYvOXpndqumiQd0zq5e2Zg707r_)|

### Task 2
Write a program that equalizes the histogram of a given image. Consider the formula,

s<sub>k</sub> = T(r<sub>k</sub>) = &Sum;<sup>k</sup><sub>j=0</sub> p<sub>in</sub>(r<sub>k</sub>) = (L-1)/MN &Sum;<sup>k</sup><sub>j=0</sub> n<sub>j</sub>

|Enhanced Image|Histogram|
|--|--|
|![](https://lh3.googleusercontent.com/fN8k-Nhcdua1InHvbu_yGO4KpgzB89Q54zs-Q9XfoaEn70VoTculxtZif-29PDbqjkb3Uo_bw0fT2w7wQmVKRaFzort2I8RtqWpTlpkTmQ_VyCDD5BYpAtedkYO-L5AZVY3XZGEZ)|![](https://lh5.googleusercontent.com/JWQuxd3i5k_AhjtekCEudyjbknKnogdvRAvY5yjqlhUOSN-sJohrXAqf5JwaDt38e0DKxYVwowpVM2yIeFQwH0XiOyJWfVXzebj8O9Woul3WmAqrb3d-xtlYgTBfDH9Ny0WATEKa)|

### Task 3
**Does the equalized histogram has a uniform distribution?**
No. The image does not have uniform distribution, because a digital image is a discrete entity not an uniform entity, that is why we do not get a uniform distribution.