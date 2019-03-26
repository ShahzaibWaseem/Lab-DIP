# Lab 08: Local Histogram Equalization

## Tasks

### Task 1
Perform Global histogram equalization to enhance this image. Save and show the original histogram and the processed histogram along with the input and resulting images.

|Original Image|Histogram|
|--|--|
|![](https://lh5.googleusercontent.com/3SQWtfDB_ASyTLlHekdik943zNFk2psqXoll50OqhsliEKZB4exZ_l1jEAUMtNXjg73SE3zrwpXYBjrLZ8pzc5plgUsfeAynJPwddQlZ5T1q7a1I4eCoOvaQTEy2BYTJRojfPoJ6)|![](https://lh6.googleusercontent.com/Di_-Lkqxr20_79hHKbxqRbDfhZ_COtXijflEj04Ft6Nk4mGHwmRAlTVf6-4bHgSx-RCr6Q3B-sEK4wlXfGSWcCxwNET2D7sw3EjszXtzlKDBJ8znT8_VcU2QDyCElj7j9YTgPKCv)|

|*Global* Histogram Enhancing|Histogram|
|--|--|
|![](https://lh6.googleusercontent.com/-zNUwZsBOOHCUrej_wbFbzBfzA-jEGoBZ5-YLagnL3bkxnYA4gyBSYVK1QR_fkoma1nJXhUUY76v5SemRVNXmzG2GFti7ZsQL8R2uCVABLRA6MIsGDLaOM2HzCfEq6rhVsUSY_Wm)|![](https://lh4.googleusercontent.com/IFuZtTmxTZ-ua8rQZZeJtqLFBwxnFXM4wmyCd5aUsJZkrwqRw-tdQzgvLAdPuRpLFGvMriEgfhW8YCc1qZmgFhcqpfmHbcV0pqnf2VT07nriucbgcxpK7_9zSTZbL9Kk-5cUpavD)|

### Task 2
##### Tiling Approach
Use least four tiles. Save and show the original histograms and the processed histogram from each tile, along with the final complete image.

|*Local* Histogram Enhancing - *Tiling Approach*|Histogram|
|--|--|
|![](https://lh4.googleusercontent.com/wzgF2aNfqYz4jUz7UpyKbsYgWUSgjdJh_7zfDamybRMZ3yAHw43mQ22K_pVb-RBU2aFIeufCtb3V_8tsSC2iMjzDYIXP7vw_K1fe5njrT13YemSgPx3SvfmiBpgZBiSO5FRVevVa)|![](https://lh5.googleusercontent.com/3VQFQeT_37KU8_lWdw6VpzM-JaAn4ThbbNiMO5onvBO5aPU--pLoA3uHwc1mcfC3zqHop2X7AjtBYJGLnhaGpzfuPlosbfZh9-70UKZfiOECcpckktpFbhXO-75I8ojdH5a-s4MY)|

##### Sliding Window Approach
displacement by one pixel size in each iteration. Save and show the original histograms and the processed histograms, along with the final complete image.

|*Local* Histogram Enhancing - *Sliding Window Approach*|Histogram|
|--|--|
|![](https://lh6.googleusercontent.com/kerkBPrvNDowAck4Goifwrl2PGJGyuA7LvIMwXYz07OGA21ua9_rAj8XDD3kU2Pd4e10G3JEIav8UgSQpE5ULtLcLUoyDQMCZWGaxUbxm2PDYhILXEDcL_WL38fzcWp_aP0rn_K5)|![](https://lh3.googleusercontent.com/5DgaIWEDiU7iej4bHRZTVvBzT0dhL1aA16kAfn0b55Eewq11q7qGRFeEsqXfG2cWywd1qa33nIOm3tm2YSIclcYc9Fl-93IsBis9NS_DNBwYD3q_VbYidM1GIHuOM2er9ogc4dPH)|

### Question
What artifacts/ effects are observed when applying equalization at different levels in an image?
#### Answer
I Observed that when Tiling Approach is used the Image has 4 steps, or there are 4 sections which show difference in shades (of gray) which is a unwanted effect. Sliding Window Approach yields better results. I observed that when the window size is lower the processing is done on more local image, which is not very good. So, I chose a window size of size 64, which equalizes on a much larger scale, which produces much better results.