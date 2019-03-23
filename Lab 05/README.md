# Lab 05: Bit Plane Slicing

## Tasks
### Task 1
Implement a function for displaying negative of an input image. Note that the function must handle binary, grayscale, and RGB images. Example of RGB negative:

|Lenna|Negative Lenna|
|--|--|
|![](https://lh3.googleusercontent.com/RfM6TgNS2N77FE0nBGokRr8mnndUiD0X3jaXJyV9giQW6eWNnFdpaVSTd6Po-eBJmFe-33AbkJYL60HwSlhG9tg1M9GLemn7sj6svf87V37ykoyOrKUFWGpkatJb7yAZrIeC4Ati =300x300)|![](https://lh5.googleusercontent.com/43S0IoUJ38l4EiTAde_vKKZrF5uUFdY1y6Om2ClEAYxVjJ_BXgOmnxXo2MA8RunEK5fpscO5PS2RZ858piCtBelSAXfklw81-kvs0Sa6Fr5tXBhT2UQyNkdJnSbhsEYuZ6QzrQdT =300x300)|

### Task 2
The horizontal gradient image can be used to detect vertical edges in an image. How, do you think? Implement a function for displaying the horizontal gradient of a grayscale image. The gradient can be approximated by forward differences:

I<sub>gradient</sub>(x, y) = I (x + 1, y) - I (x, y)

|Lenna|Horizontal Derivative|
|---|---|
|![](https://lh3.googleusercontent.com/RfM6TgNS2N77FE0nBGokRr8mnndUiD0X3jaXJyV9giQW6eWNnFdpaVSTd6Po-eBJmFe-33AbkJYL60HwSlhG9tg1M9GLemn7sj6svf87V37ykoyOrKUFWGpkatJb7yAZrIeC4Ati =300x300)|![](https://lh3.googleusercontent.com/QDHER1S5CLbhEILZw0MGFzdzt6lXLXRlsfT_6oVemdEvExZ0z2zkYnaQe0m2dVcmr-nvKGPQEJ5prli9ywatEUdy35UbMuu18-uk7WGuA22Hz5WkbmsHziI2X7m3knkKz2btDCM3 =300x300)|

### Task 3
Perform bit slicing of an 8 bit grey-scale image as discussed in the lecture. Start from the least significant bit and move towards the most significant bit. You will get eight binary images of the input image as demonstrated below.
|Bit Plane 1|Bit Plane 2|Bit Plane 3|Bit Plane 4|
|--|--|--|--|
|![](https://lh4.googleusercontent.com/B5foP1tslSlf_0Dn9wb9JeIctYc16gEKSvRv95AvEw9QnR8SP8mQBh9Kff112po_t7gOLRKXreW-n657pD3xMaDmDJd1eCuP29ftp_cdELfGxD3prpARGok7cH_G5fu8Is7OrSae)|![](https://lh4.googleusercontent.com/ELuo2siXYisVzER0AWh9LorBOCz8mv2R_ly2sddiJ3wOEctW-PEhMpIZD-zwv9rKC8vaNOHdad4iHIHqSSSA_spisku_Ng8pD_9hCyYarlTcYt-ehreqMhhi3W_TnUzw61E5O-n2)|![](https://lh5.googleusercontent.com/Mzy3PezE6QBRjFhK8umhiLTRRUYHgi106puUMaPiIfvZeMnqVQMTQtNsDLjmc-xmBzuSfRtD1btSLZtjN4C8SYMaMWFQt92deF7JSx-lJqctVu8NcJnn4CPTrKK41wCDmLWxth7h)|![](https://lh5.googleusercontent.com/bnBvHIHopnEnnS8SlPgxyuw_U4_afot6B8qV1ZyIhGO8R6Wo7AuVkGu2N82IL5A0YGbYQHPEj1SAyJjBUczxuqttUmO1cN-InkXxEOLEufOn9zPKESW7NKpOTj1TlgDMt-Q3kLwT)|

|Bit Plane 5|Bit Plane 6|Bit Plane 7|Bit Plane 8|
|--|--|--|--|
|![](https://lh3.googleusercontent.com/tZOqXqeAkjO_HyJNeqzWPp-KKT8g6YGlzUpkT0GC54nGdRpZ6BTwwLNDGbgfqKXNmZj35y_A0cN3zpscWEgBYqG59Vebyy6lXeN-2pgi9XhTvug-X42_x0dU6-vXEqsiFkGsuip_)|![](https://lh6.googleusercontent.com/74MlQVGz-CJp0ql-SusdT34gItWHIkb2AoF_68Nexp5LUfvk0F_ErklErqRb474mnpw7bcIiULMqwaMgVHcUcXPUmSR5a1trF7jPsvLzw2cidbRTQ-k6M6_VFSytMaxrOSFI-NBP)|![](https://lh4.googleusercontent.com/1OhixaTVc9VGFPXJjVC062S2NahH7JZuPFOmkskso8RJVkq4UGVnzKsMbNvtPcYf3_0LirQykM2EV5c00t2H16C2apEJlHQCDDo-veOTPqmNl1DVsxFD5KehDhDwlqPDISOWfi_X)|![](https://lh4.googleusercontent.com/LzMtaczuWW4wLJwH9yE5sYF-bqJE4Lmo30wxabxDSdI6DWVOloU9KHrD3rQxFMLkS_2yufyVSNWzw3RG8Yb-Cyxc2TivZ5IOhbh65s4Lj3YXPT6MepA43Y7v1abPzkFaorEma-I9)|